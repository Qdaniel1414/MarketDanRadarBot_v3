from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.formulas.gold_melted_calculator import (
    gold_melted_start,
    get_weight,
    get_sood,
    get_tax,
)

from handlers.iran_market.formulas.gold_melted_states import (
    WEIGHT,
    SOOD,
    TAX,
)


# ==========================================
# Conversation محاسبه طلای آب‌شده
# ==========================================

gold_melted_conversation = ConversationHandler(

    # ======================================
    # شروع محاسبه
    # ======================================

    entry_points=[
        MessageHandler(
            filters.Regex(r"^🌙 طلای آب‌شده$"),
            gold_melted_start,
        ),
    ],

    # ======================================
    # دریافت وزن
    # ======================================

    states={

        WEIGHT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_weight,
            )
        ],

        # ==================================
        # دریافت سود
        # ==================================

        SOOD: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_sood,
            )
        ],

        # ==================================
        # دریافت مالیات
        # ==================================

        TAX: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_tax,
            )
        ],
    },

    # ======================================
    # خروج از محاسبه
    # ======================================

    fallbacks=[
        MessageHandler(
            filters.Regex(r"^⬅️ بازگشت$"),
            lambda update, context: ConversationHandler.END,
        ),
    ],

    allow_reentry=True,
)