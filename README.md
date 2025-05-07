
# 📰 Real-Time Topic Modeling on The Indian Express News Articles

This project performs **real-time topic modeling** and generates **AI-based labels** on Indian Express news headlines using:

- 🧠 LDA (Latent Dirichlet Allocation) for topic extraction
- 🤖 OpenRouter AI for generating contextual smart labels
- 🌐 Flask for web interface
- 🛠️ Web scraping for fetching the latest news


## 🚀 Features

- Fetches latest headlines from [indianexpress.com](https://indianexpress.com/)
- Allows user to enter **custom news URLs** or input their own headline
- Uses NLP preprocessing and topic modeling (LDA)
- Generates AI-based topic labels using OpenRouter API
- Clean, browser-based interface


## 📂 Project Structure

 ``` bash 
Topic-Modeling-on-The-Indian-Express-News-Article
├── app/
│   ├── scraper.py             # Web scraper for headlines
│   ├── nlp\_utils.py           # Preprocessing and topic modeling
│   └── openrouter\_api.py      # AI label generator using OpenRouter API
├── templates/
│   └── index.html             # Main UI template
├── main.py                    # Flask server and app logic
├── requirements.txt           # Python dependencies
├── .env                       # Stores your OpenRouter API key
└── README.md                  # Project documentation

````


## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Jaikumar96/Topic-Modeling-on-The-Indian-Express-News-Article.git
cd Topic-Modeling-on-The-Indian-Express-News-Article
````

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenRouter API Key

Create a `.env` file in the root directory and add your API key:

```bash
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> 💡 You can get a free API key from [https://openrouter.ai/](https://openrouter.ai/)


## 🧪 Run the App

```bash
python main.py
```

Then open your browser and go to [http://localhost:5000](http://localhost:5000)


## 🌐 Usage

* By default, it fetches and analyzes headlines from Indian Express.
* You can enter your own **custom URL** or manually input a news **headline or paragraph**.
* The app returns:

  * 🔍 Preprocessed topic keywords via LDA
  * 💬 Smart AI-generated label via OpenRouter

---

## 🧠 Example Output

```text
Headline: India’s space sector created 22,000 job in last decade
LDA Topic: 0.016*"mission" + 0.016*"india" + 0.016*"launched" + ...
AI Label: Space jobs and economic boost in India
```

## 📌 Requirements

* Python 3.7+
* Flask
* BeautifulSoup
* NLTK
* Gensim
* Requests
* dotenv

All required packages are listed in `requirements.txt`.


## 📄 License

This project is for educational and academic use only.

