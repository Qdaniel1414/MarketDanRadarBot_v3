from telegram.ext import MessageHandler, filters

from handlers.international_market.menu import (
    international_market_menu,
)

from handlers.international_market.economic_calendar.calendar import (
    economic_calendar,
    economic_news,
)


def register_international_market(app):

    # منوی بازارهای بین‌المللی
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🌍 بازارهای بین‌المللی$"),
            international_market_menu,
        )
    )

    # تقویم اقتصادی
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📅 تقویم اقتصادی$"),
            economic_calendar,
        )
    )

    # اخبار اقتصادی
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📰 اخبار اقتصادی$"),
            economic_news,
        )
    )