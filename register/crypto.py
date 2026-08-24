from telegram.ext import MessageHandler, filters

from handlers.education.crypto_education.calculators import (
    crypto_calculators_menu,
    crypto_calculators_router,
)


def register_crypto(app):

    app.add_handler(
        MessageHandler(
            filters.Regex("^🪙 ماشین حساب کریپتو$"),
            crypto_calculators_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            crypto_calculators_router,
            block=True,
        ),
        group=2,
    )