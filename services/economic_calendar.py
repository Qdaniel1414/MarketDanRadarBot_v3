import feedparser


RSS_URL = "https://www.investing.com/rss/news_25.rss"


def get_economic_news(limit=10):
    """
    دریافت آخرین اخبار اقتصادی
    """

    feed = feedparser.parse(RSS_URL)

    results = []

    for item in feed.entries[:limit]:

        results.append(
            {
                "title": item.title,
                "link": item.link,
                "published": item.published,
            }
        )

    return results
if __name__ == "__main__":

    news = get_economic_news()

    for item in news:
        print(item["published"])
        print(item["title"])
        print(item["link"])
        print("-" * 60)