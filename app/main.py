from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import feedparser

app = FastAPI()

# Allow all origins (frontend + mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "✅ NIEO.AI Backend Live on Vercel"}

@app.get("/news")
def get_news():
    feed_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(feed_url)
    articles = [{"title": entry.title, "link": entry.link} for entry in feed.entries[:10]]
    return {"articles": articles}
