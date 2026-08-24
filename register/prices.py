from telegram.ext import MessageHandler, filters

from handlers.currency import currency_prices
from handlers.gold import gold_prices
from handlers.global_prices import global_prices

from handlers.crypto import crypto_prices
from handlers.crypto_pages import (
    crypto_page_1,
    crypto_page_2,
)
from handlers.crypto_search import (
    crypto_search_start,
    crypto_search_result,
)


def register_price_handlers(app):

    # --------------------------------------------------------
    # ارز
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 ارز$"),
            currency_prices,
        )
    )

    # --------------------------------------------------------
    # طلا و سکه
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 طلا و سکه$"),
            gold_prices,
        )
    )

    # --------------------------------------------------------
    # بازارهای جهانی
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🌍 بازارهای جهانی$"),
            global_prices,
        )
    )

    # --------------------------------------------------------
    # ارزهای دیجیتال
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^₿ ارزهای دیجیتال$"),
            crypto_prices,
        )
    )

    # --------------------------------------------------------
    # صفحه ۱ کریپتو
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📄 صفحه ۱$"),
            crypto_page_1,
        )
    )

    # --------------------------------------------------------
    # صفحه ۲ کریپتو
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📄 صفحه ۲$"),
            crypto_page_2,
        )
    )

    # --------------------------------------------------------
    # شروع جستجوی ارز
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🔍 جستجوی ارز$"),
            crypto_search_start,
        )
    )

    # --------------------------------------------------------
    # نتیجه جستجوی ارز
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            crypto_search_result,
        ),
        group=8,
    )

    # --------------------------------------------------------
    # بروزرسانی
    # --------------------------------------------------------

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🔄 بروزرسانی$"),
            gold_prices,
        )
    )