import requests
from bs4 import BeautifulSoup


URL = "https://www.investing.com/economic-calendar/Service/getCalendarFilteredData"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    ),
    "X-Requested-With": "XMLHttpRequest",
}


def get_calendar():

    payload = {
        "country[]": "5",
        "importance[]": "1",
        "importance[]": "2",
        "importance[]": "3",
        "timeZone": "55",
        "timeFilter": "timeRemain",
        "currentTab": "today",
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        data=payload,
        timeout=20,
    )

    html = response.json()["data"]

    soup = BeautifulSoup(html, "html.parser")

    events = []

    rows = soup.find_all("tr", class_="js-event-item")

    for row in rows:

        try:

            time = row.find("td", class_="time").get_text(strip=True)

            country = row.find("span")["title"]

            currency = row.find(
                "td",
                class_="left flagCur noWrap",
            ).get_text(strip=True)

            title = row.find(
                "td",
                class_="left event",
            ).get_text(" ", strip=True)

            impact = len(
                row.select("td.sentiment i.grayFullBullishIcon")
            )

            actual = row.find(
                "td",
                class_="bold",
            )

            forecast = row.find(
                "td",
                class_="fore",
            )

            previous = row.find(
                "td",
                class_="prev",
            )

            events.append(
                {
                    "time": time,
                    "country": country,
                    "currency": currency,
                    "title": title,
                    "impact": "⭐" * impact,
                    "actual": actual.get_text(strip=True)
                    if actual
                    else "-",
                    "forecast": forecast.get_text(strip=True)
                    if forecast
                    else "-",
                    "previous": previous.get_text(strip=True)
                    if previous
                    else "-",
                }
            )

        except Exception:
            continue

    return events