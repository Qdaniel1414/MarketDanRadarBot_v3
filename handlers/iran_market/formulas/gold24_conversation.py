from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.formulas.gold_24_calculator import (
    gold24_start,
    get_weight,
    get_ojrat,
    get_sood,
    get_tax,
)

from handlers.iran_market.formulas.gold_18_states import (
    WEIGHT,
    OJRAT,
    SOOD,
    TAX,
)


gold24_conversation = ConversationHandler(

    entry_points=[

        MessageHandler(
            filters.Regex(r"^🥈 طلای ۲۴ عیار$"),
            gold24_start,
        ),

    ],

    states={

        WEIGHT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_weight,
            )

        ],

        OJRAT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_ojrat,
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