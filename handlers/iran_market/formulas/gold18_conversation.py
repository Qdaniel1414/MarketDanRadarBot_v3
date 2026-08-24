from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.formulas.gold_18_calculator import (
    gold18_start,
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

gold18_conversation = ConversationHandler(

    entry_points=[

        MessageHandler(

            filters.Regex("^🥇 طلای ۱۸ عیار$"),

            gold18_start,

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