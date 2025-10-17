from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import feedparser

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all frontends
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "NIEO backend running successfully"}

@app.get("/news")
def get_news(topic: str = "general", lang: str = "en"):
    """
    Fetch live news from Google RSS.
    topic: search keyword
    lang: language code (e.g., 'ml' for Malayalam, 'zh-CN' for Chinese)
    """
    url = f"https://news.google.com/rss/search?q={topic}&hl={lang}&gl=GLOBAL&ceid=GLOBAL:{lang}"
    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:10]:  # Top 10 articles
        articles.append({
            "title": entry.title,
            "link": entry.link
        })
    return {"articles": articles}
