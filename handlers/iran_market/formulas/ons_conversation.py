from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.formulas.ons_calculator import (
    ons_start,
    get_weight,
    get_sood,
    get_tax,
)

from handlers.iran_market.formulas.ons_states import (
    WEIGHT,
    SOOD,
    TAX,
)

ons_conversation = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex("^🌍 انس جهانی$"),
            ons_start,
        )
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

)