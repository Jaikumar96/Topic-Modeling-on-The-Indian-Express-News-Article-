from flask import Flask, render_template, request, redirect, url_for
from app.scraper import scrape_headlines, scrape_headlines_custom
from app.nlp_utils import preprocess, get_topics
from app.openrouter_api import get_smart_label
from dotenv import load_dotenv
import os

load_dotenv()

# Ensure the API key is set
if not os.getenv("OPENROUTER_API_KEY"):
    print("WARNING: OPENROUTER_API_KEY environment variable is not set.")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    custom_url = ""
    results = []
    error_message = None
    num_topics = 5  # Default number of topics
    
    if request.method == "POST":
        custom_url = request.form.get("custom_url", "")
        num_topics = int(request.form.get("num_topics", 5))
        
        try:
            if custom_url:
                headlines = scrape_headlines_custom(custom_url)
            else:
                headlines = scrape_headlines()
                
            if not headlines:
                error_message = "No headlines found. Please try a different URL."
            else:
                # Filter out duplicate headlines and very short ones
                unique_headlines = []
                seen = set()
                for headline in headlines:
                    cleaned = headline.strip()
                    if cleaned and len(cleaned) > 15 and cleaned not in seen:
                        seen.add(cleaned)
                        unique_headlines.append(cleaned)
                
                if not unique_headlines:
                    error_message = "No valid headlines found after filtering."
                else:
                    processed = preprocess(unique_headlines)
                    lda_topics = get_topics(processed, num_topics=num_topics)
                    
                    for i, headline in enumerate(unique_headlines[:min(len(unique_headlines), 20)]):  # Limit to 20 headlines
                        topic_text = lda_topics[i % num_topics][1] if i < len(lda_topics) else "N/A"
                        smart_label = get_smart_label(headline)
                        results.append({
                            "headline": headline,
                            "lda_topic": topic_text,
                            "smart_label": smart_label
                        })
        except Exception as e:
            error_message = f"Error processing request: {str(e)}"
    else:
        try:
            headlines = scrape_headlines()
            processed = preprocess(headlines)
            lda_topics = get_topics(processed, num_topics=num_topics)
            
            for i, headline in enumerate(headlines[:min(len(headlines), 20)]):  # Limit to 20 headlines
                topic_text = lda_topics[i % num_topics][1] if i < len(headlines) else "N/A"
                smart_label = get_smart_label(headline)
                results.append({
                    "headline": headline,
                    "lda_topic": topic_text,
                    "smart_label": smart_label
                })
        except Exception as e:
            error_message = f"Error processing request: {str(e)}"
    
    return render_template(
        "index.html", 
        results=results, 
        custom_url=custom_url, 
        error_message=error_message,
        num_topics=num_topics
    )

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)