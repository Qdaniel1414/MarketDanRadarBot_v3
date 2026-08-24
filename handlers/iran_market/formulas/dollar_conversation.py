from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.formulas.dollar_calculator import (
    dollar_start,
    get_weight,
    get_sood,
    get_tax,
)

from handlers.iran_market.formulas.dollar_states import (
    WEIGHT,
    SOOD,
    TAX,
)

dollar_conversation = ConversationHandler(

    entry_points=[

        MessageHandler(
            filters.Regex("^💵 دلار آمریکا$"),
            dollar_start,
        ),

        MessageHandler(
            filters.Regex("^₮ تتر$"),
            dollar_start,
        ),

    ],

    states={

        WEIGHT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_weight,
            )
        ],

        SOOD: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_sood,
            )
        ],

        TAX: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_tax,
            )
        ],

    },

    fallbacks=[],

    allow_reentry=True,

)