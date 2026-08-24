from telegram.ext import MessageHandler, filters

from handlers.education.menu import education_menu

from handlers.education.financial_literacy.menu import (
    financial_literacy_menu,
)

from handlers.education.technical_analysis.menu import (
    technical_analysis_menu,
)

from handlers.education.crypto_education.menu import (
    crypto_education_menu,
)

from handlers.education.macroeconomics.menu import (
    macroeconomics_menu,
)


def register_education(app):

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📚 آموزش‌ها$"),
            education_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💰 آموزش سواد مالی$"),
            financial_literacy_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📈 آموزش تحلیل تکنیکال$"),
            technical_analysis_menu,
        )
    )

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🪙 آموزش ارزهای دیجیتال$"),
        crypto_education_menu,
    )
)

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🌍 آموزش اقتصاد کلان$"),
            macroeconomics_menu,
        )
    )