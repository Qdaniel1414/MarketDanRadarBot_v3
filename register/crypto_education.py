from telegram.ext import (
    MessageHandler,
    ConversationHandler,
    filters,
)


from handlers.education.crypto_education.menu import (
    crypto_education_menu,
    crypto_education_router,
)


from handlers.education.crypto_education.bitcoin import (
    bitcoin_intro,
    bitcoin_example,
    bitcoin_calculator,
)


from handlers.crypto_search import (
    crypto_search_result,
)


# =========================
# DCA
# =========================

from handlers.education.crypto_education.calculators.dca import (
    dca_start,
    dca_capital,
    dca_count,
    dca_interval,
)


from handlers.education.crypto_education.calculators.dca_states import (
    CAPITAL,
    COUNT,
    INTERVAL,
)


# =========================
# BTC
# =========================

from handlers.education.crypto_education.calculators.btc_converter import (
    btc_converter_handler,
)


# =========================
# ETH
# =========================

from handlers.education.crypto_education.calculators.eth_converter import (
    eth_converter_intro,
    ethereum_input,
)


# =========================
# Other Calculators
# =========================

from handlers.education.crypto_education.calculators.satoshi import (
    satoshi_converter_intro,
    satoshi_input,
)


from handlers.education.crypto_education.calculators.staking_conversation.conversation import (
    staking_handler,
)


from handlers.education.crypto_education.calculators.profit_loss import (
    profit_loss_handler,
)


from handlers.education.crypto_education.calculators.drawdown import (
    drawdown_handler,
)


# =========================
# Router
# =========================

from handlers.education.crypto_education.calculators import (
    crypto_calculators_router,
)
from handlers.education.crypto_education.calculators.eth_converter import (
    eth_converter_handler,
)
from handlers.education.crypto_education.calculators.satoshi import (
    satoshi_handler,
)

def register_crypto_education(app):


    # =========================
    # Crypto Menu
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^🌑 آموزش ارزهای دیجیتال$"
            ),
            crypto_education_menu,
        )
    )



    # =========================
    # Crypto Education Router
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(₿ بیت کوین چیست؟|"
                r"⛓ بلاکچین چیست؟|"
                r"🪙 آلت کوین چیست؟|"
                r"🏦 استیبل کوین چیست؟|"
                r"💵 تتر USDT|"
                r"🧠 اسمارت کانترکت|"
                r"💳 دیفای DeFi|"
                r"🎨 NFT|"
                r"⚡ ماینینگ|"
                r"🧾 واژه نامه کریپتو|"
                r"🪙 ماشین حساب کریپتو)$"
            ),
            crypto_education_router,
        )
    )



    # =========================
    # Bitcoin Education
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^📘 بیت کوین چیست؟$"
            ),
            bitcoin_intro,
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^📈 مثال واقعی$"
            ),
            bitcoin_example,
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^🧮 ماشین حساب بیت کوین$"
            ),
            bitcoin_calculator,
        )
    )



    # =========================
    # DCA
    # =========================

    app.add_handler(
        ConversationHandler(

            entry_points=[
                MessageHandler(
                    filters.Regex(
                        r"^🪙 میانگین خرید DCA$"
                    ),
                    dca_start,
                )
            ],


            states={

                CAPITAL: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        dca_capital,
                    )
                ],


                COUNT: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        dca_count,
                    )
                ],


                INTERVAL: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        dca_interval,
                    )
                ],
            },


            fallbacks=[],
        )
    )



    # =========================
    # BTC
    # =========================

    app.add_handler(btc_converter_handler)



    # =========================
    # ETH
    # =========================

    app.add_handler(eth_converter_handler)



    # =========================
    # Satoshi
    # =========================
    app.add_handler(satoshi_handler)


# =========================
# Staking
# =========================

    app.add_handler(staking_handler)



    # =========================
    # Profit Loss
    # =========================

    app.add_handler(profit_loss_handler)



    # =========================
    # Drawdown
    # =========================

    app.add_handler(drawdown_handler)




    # =========================
    # Crypto Search
    # =========================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            crypto_search_result,
        ),
        group=8,
    )