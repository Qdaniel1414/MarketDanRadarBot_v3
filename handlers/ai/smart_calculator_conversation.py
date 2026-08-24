from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.ai.smart_calculator import (
    smart_calculator,
    smart_calculator_input,
)


# ============================================================
# STATES
# ============================================================

SMART_CALCULATOR_INPUT = 1


# ============================================================
# SMART CALCULATOR CONVERSATION
# ============================================================

smart_calculator_conversation = ConversationHandler(

    # ========================================================
    # ENTRY POINT
    # ========================================================

    entry_points=[
        MessageHandler(
            filters.Regex(r"^🧮 محاسبه‌گر هوشمند$"),
            smart_calculator,
        ),
    ],

    # ========================================================
    # STATES
    # ========================================================

    states={

        SMART_CALCULATOR_INPUT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                smart_calculator_input,
            ),

        ],

    },

    # ========================================================
    # FALLBACKS
    # ========================================================

    fallbacks=[],

    allow_reentry=True,
)