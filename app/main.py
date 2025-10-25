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

@app.get("/news")
def get_news(topic: str):
    try:
        # URL encode the topic to handle spaces
        encoded_topic = urllib.parse.quote(topic)

        # Google News RSS feed
        feed_url = f"https://news.google.com/rss/search?q={encoded_topic}"

        feed = feedparser.parse(feed_url)

        articles = []
        for entry in feed.entries[:10]:  # limit 10 articles
            articles.append({"title": entry.title, "link": entry.link})
        return {"articles": articles}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
