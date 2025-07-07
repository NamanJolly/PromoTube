<h1 align="center">🕵️‍♂️ PromoTube</h1>
<p align="center">
  <i>Sniff out hidden promo codes and affiliate links from YouTube videos using AI.</i><br>
  <strong>Built with 🔍 Streamlit + Transformers + YouTube Data API</strong>
</p>

---

## 🚀 Live Demo

🔗 [PromoTube on Streamlit Cloud](https://promo-tube.streamlit.app)  


---

## ✨ What It Does

PromoTube is a **minimalist AI tool** focused on **one job** — extracting **useful promo codes and affiliate links** from YouTube video descriptions. No clutter, no distractions — just fast, focused functionality.

🔍 Type a product name  
🎯 It searches YouTube for related promo content  
📦 It extracts real, usable links and codes (not every random link)  
🧠 AI filters the noise so you only get value


---

## 🎨 Features

✅ Auto-searches YouTube for Promo Codes for your desired product  
✅ AI-powered content filtering using **Zero-shot LLM**   
✅ 🔄 **One-click Refresh**  
✅ Collapsible link categories  
✅ Supports redirect links like:  
`mydomain.com/go/product → targetsite.com`

---

## 🧠 Tech Stack

| Layer         | Tech Used                                     |
|---------------|-----------------------------------------------|
| UI            | Streamlit                                     |
| LLM           | 🤖 `joeddav/xlm-roberta-large-xnli` (Hugging Face) |
| NLP           | NLTK, regex parsing                           |
| YouTube       | `google-api-python-client`                    |
| Scraping      | `requests`                    |
| Styling       | Streamlit themes + custom CSS                 |

---

## 🖼️ Preview

<p align="center">
  <img src="/assets/landing.png" width="700" alt="Preview">
</p>

---

## 📂 Folder Structure
```
PromoTube/
├── app.py # Main Streamlit app
├── extractor.py # Promo link/code classifier
├── searcher.py # YouTube search logic
├── youtube_fetcher.py # Get video descriptions
├── models/
│ └── classifier.py # HuggingFace pipeline setup
├── requirements.txt # Dependencies
└── README.md # This file

```

---

## 🧪 Local Setup

```bash
git clone https://github.com/yourusername/PromoTube.git
cd PromoTube
python -m venv .venv
# Activate virtual env:
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```