import feedparser
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse  # for encoding spaces

app = FastAPI()

# Allow frontend to fetch
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root route for testing
@app.get("/")
def home():
    return {"message": "NIEO.AI backend is running successfully 🚀"}

@app.get("/news")
def get_news(topic: str):
    try:
        # Encode topic (handle spaces and special chars)
        encoded_topic = urllib.parse.quote(topic)

        # Google News RSS feed URL
        feed_url = f"https://news.google.com/rss/search?q={encoded_topic}"

        # Parse the feed
        feed = feedparser.parse(feed_url)

        # If no entries found, return error
        if not feed.entries:
            raise HTTPException(status_code=404, detail="No news found for this topic")

        # Collect top 10 articles
        articles = []
        for entry in feed.entries[:10]:
            articles.append({
                "title": entry.title,
                "link": entry.link
            })
        return {"articles": articles}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
