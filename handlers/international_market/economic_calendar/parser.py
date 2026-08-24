import feedparser

from .scraper import get_calendar


# ==========================
# اخبار اقتصادی
# ==========================

NEWS_RSS = "https://www.forexlive.com/feed/"


def get_latest_news(limit=10):

    feed = feedparser.parse(NEWS_RSS)

    if feed.bozo:
        return []

    news = []

    for item in feed.entries[:limit]:

        news.append(
            {
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "published": item.get("published", ""),
            }
        )

    return news


# ==========================
# تقویم اقتصادی
# ==========================

def get_today_calendar():

    return get_calendar()