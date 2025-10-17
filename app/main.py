from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import feedparser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def get_news(topic: str = "general"):
    rss_url = f"https://news.google.com/rss/search?q={topic}+when:24h&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:10]:  # top 10 news
        articles.append({"title": entry.title, "link": entry.link})
    return {"articles": articles}
