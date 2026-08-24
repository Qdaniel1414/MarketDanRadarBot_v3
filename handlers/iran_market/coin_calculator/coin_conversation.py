from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from handlers.iran_market.coin_calculator.coin_calculator import (
    get_coin_type,
    get_dollar,
    get_ounce,
    get_coin_price,
)

from handlers.iran_market.coin_calculator.coin_states import (
    COIN_TYPE,
    DOLLAR,
    OUNCE,
    COIN_PRICE,
    RESULT,
)


# =========================================================
# شروع محاسبه سکه
# =========================================================

async def coin_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    # پاک کردن اطلاعات محاسبه قبلی
    context.user_data.pop("coin_type", None)
    context.user_data.pop("dollar", None)
    context.user_data.pop("ounce", None)
    context.user_data.pop("coin_price", None)

    # =====================================================
    # منوی انتخاب نوع سکه
    # =====================================================

    coin_keyboard = ReplyKeyboardMarkup(
        [
            [
                "🥇 سکه امامی",
                "🥈 نیم سکه",
            ],
            [
                "🥉 ربع سکه",
                "🪙 سکه گرمی",
            ],
            [
                "🚪 خروج از محاسبه",
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )

    await update.message.reply_text(
        "🥇 محاسبه سکه\n\n"
        "لطفاً نوع سکه را انتخاب کنید:",
        reply_markup=coin_keyboard,
    )

    return COIN_TYPE


# =========================================================
# خروج از محاسبه
# =========================================================

async def coin_exit(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    # پاک کردن اطلاعات
    context.user_data.pop("coin_type", None)
    context.user_data.pop("dollar", None)
    context.user_data.pop("ounce", None)
    context.user_data.pop("coin_price", None)

    await update.message.reply_text(
        "🚪 محاسبه سکه بسته شد."
    )

    return ConversationHandler.END


# =========================================================
# Conversation Handler
# =========================================================

coin_conversation = ConversationHandler(

    # =====================================================
    # شروع Conversation
    # =====================================================

    entry_points=[
        MessageHandler(
            filters.Regex(
                r"^🥇 محاسبه سکه$"
            ),
            coin_start,
        ),
    ],

    # =====================================================
    # States
    # =====================================================

    states={

        # -------------------------------------------------
        # انتخاب نوع سکه
        # -------------------------------------------------

        COIN_TYPE: [

            MessageHandler(
                filters.Regex(
                    r"^(🥇 سکه امامی|🥈 نیم سکه|🥉 ربع سکه|🪙 سکه گرمی)$"
                ),
                get_coin_type,
            ),

            MessageHandler(
                filters.Regex(
                    r"^🚪 خروج از محاسبه$"
                ),
                coin_exit,
            ),
        ],

        # -------------------------------------------------
        # قیمت دلار
        # -------------------------------------------------

        DOLLAR: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_dollar,
            ),

            MessageHandler(
                filters.Regex(
                    r"^🚪 خروج از محاسبه$"
                ),
                coin_exit,
            ),
        ],

        # -------------------------------------------------
        # قیمت اونس جهانی
        # -------------------------------------------------

        OUNCE: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_ounce,
            ),

            MessageHandler(
                filters.Regex(
                    r"^🚪 خروج از محاسبه$"
                ),
                coin_exit,
            ),
        ],

        # -------------------------------------------------
        # قیمت روز سکه
        # -------------------------------------------------

        COIN_PRICE: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_coin_price,
            ),

            MessageHandler(
                filters.Regex(
                    r"^🚪 خروج از محاسبه$"
                ),
                coin_exit,
            ),
        ],

        # -------------------------------------------------
        # نتیجه
        # -------------------------------------------------

        RESULT: [

            # محاسبه مجدد
            MessageHandler(
                filters.Regex(
                    r"^🔄 محاسبه مجدد$"
                ),
                coin_start,
            ),

            # خروج
            MessageHandler(
                filters.Regex(
                    r"^🚪 خروج از محاسبه$"
                ),
                coin_exit,
            ),
        ],
    },

    # =====================================================
    # Fallback
    # =====================================================

    fallbacks=[

        MessageHandler(
            filters.Regex(
                r"^🚪 خروج از محاسبه$"
            ),
            coin_exit,
        ),
    ],

    allow_reentry=True,
)