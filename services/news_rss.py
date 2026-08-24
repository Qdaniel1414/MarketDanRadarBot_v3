import asyncio
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


def _fetch_rss(url: str, limit: int = 10):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        data = response.read()

    root = ET.fromstring(data)

    news = []

    for item in root.findall(".//item")[:limit]:
        title = item.findtext("title", default="").strip()
        link = item.findtext("link", default="").strip()
        description = item.findtext("description", default="").strip()
        pub_date = item.findtext("pubDate", default="").strip()

        if not title or not link:
            continue

        news.append(
            {
                "title": title,
                "link": link,
                "description": description,
                "pub_date": pub_date,
            }
        )

    return news


# ============================================================
# 📰 اخبار مهم اقتصادی
# ============================================================

async def get_economic_news(limit: int = 10):
    query = urllib.parse.quote(
        "economy OR inflation OR interest rates OR central bank OR markets"
    )

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    try:
        return await asyncio.to_thread(
            _fetch_rss,
            url,
            limit,
        )

    except Exception as e:
        print("❌ NEWS RSS ERROR:", e)
        return []


# ============================================================
# 🇮🇷 اخبار اقتصاد ایران
# ============================================================

async def get_iran_economic_news(limit: int = 5):
    query = urllib.parse.quote(
        "Iran economy OR Iran inflation OR Iran rial OR Iran dollar "
        "OR Iran central bank OR Iran oil OR Iran sanctions"
    )

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    try:
        return await asyncio.to_thread(
            _fetch_rss,
            url,
            limit,
        )

    except Exception as e:
        print("❌ IRAN NEWS RSS ERROR:", e)
        return []


# ============================================================
# 🌍 اخبار اقتصاد جهان
# ============================================================

async def get_global_economic_news(limit: int = 5):
    query = urllib.parse.quote(
        "global economy OR US economy OR Europe economy OR China economy "
        "OR Federal Reserve OR ECB OR Bank of England OR Bank of Japan "
        "OR global inflation OR global GDP OR global PMI"
    )

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    try:
        return await asyncio.to_thread(
            _fetch_rss,
            url,
            limit,
        )

    except Exception as e:
        print("❌ GLOBAL NEWS RSS ERROR:", e)
        return []

    # ============================================================
# 💵 اخبار دلار و ارز
# ============================================================

async def get_currency_news(limit: int = 5):
    query = urllib.parse.quote(
        "Iran dollar OR Iranian rial OR USD IRR OR Iran currency "
        "OR foreign exchange Iran OR EUR USD OR GBP USD "
        "OR dollar index OR DXY OR forex market"
    )

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    try:
        return await asyncio.to_thread(
            _fetch_rss,
            url,
            limit,
        )

    except Exception as e:
        print("❌ CURRENCY NEWS RSS ERROR:", e)
        return []

    # ============================================================
# 🥇 اخبار طلا و سکه
# ============================================================

async def get_gold_coin_news(limit: int = 5):
    query = urllib.parse.quote(
        "gold price OR gold market OR XAU USD OR gold ounce "
        "OR Iran gold OR Iran gold coin OR Emami coin "
        "OR Bahar Azadi coin OR Iran gold market"
    )

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    try:
        return await asyncio.to_thread(
            _fetch_rss,
            url,
            limit,
        )

    except Exception as e:
        print("❌ GOLD COIN NEWS RSS ERROR:", e)
        return []

    # ============================================================
# ₿ اخبار کریپتو
# ============================================================

async def get_crypto_news(limit: int = 5):
    query = urllib.parse.quote(
        "Bitcoin OR Ethereum OR cryptocurrency OR crypto market "
        "OR crypto regulation OR blockchain OR BTC OR ETH "
        "OR crypto ETF OR Bitcoin ETF"
    )

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    try:
        return await asyncio.to_thread(
            _fetch_rss,
            url,
            limit,
        )

    except Exception as e:
        print("❌ CRYPTO NEWS RSS ERROR:", e)
        return []