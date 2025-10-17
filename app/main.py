from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import feedparser

app = FastAPI()

# Allow frontend to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "NIEO backend running successfully"}

@app.get("/news")
def get_news(topic: str = "general", lang: str = "en"):
    # Google RSS URL with language
    rss_url = f"https://news.google.com/rss/search?q={topic}&hl={lang}"
    feed = feedparser.parse(rss_url)
    articles = []

    for entry in feed.entries[:10]:  # top 10 news
        articles.append({
            "title": entry.title,
            "link": entry.link
        })

    return {"articles": articles}
