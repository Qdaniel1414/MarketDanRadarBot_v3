from handlers.international_market.economic_calendar.scraper import get_calendar

events = get_calendar()

for event in events[:5]:

    print(event)