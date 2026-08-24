from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.formulas.mesghal_calculator import (
    mesghal_start,
    get_weight,
    get_sood,
    get_tax,
)

from handlers.iran_market.formulas.mesghal_states import (
    WEIGHT,
    SOOD,
    TAX,
)


mesghal_conversation = ConversationHandler(

    entry_points=[

        MessageHandler(
            filters.Regex("^🏅 مثقال طلا$"),
            mesghal_start,
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

    fallbacks=[
        MessageHandler(
            filters.Regex("^⬅️ بازگشت$"),
            lambda update, context: ConversationHandler.END,
        ),
    ],

    allow_reentry=True,

)