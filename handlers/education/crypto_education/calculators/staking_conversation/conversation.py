from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from .states import (
    AMOUNT,
    APY,
    MONTH,
)


# -------------------------
# شروع
# -------------------------

async def staking_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "⚡ ماشین حساب سود استیکینگ\n\n"
        "🪙 مقدار ارز استیک شده را وارد کنید:"
    )

    return AMOUNT


# -------------------------
# مرحله اول
# -------------------------

async def staking_amount(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["amount"] = float(
            update.message.text.replace(",", "")
        )

    except:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return AMOUNT

    await update.message.reply_text(
        "📈 درصد سود سالانه APY را وارد کنید:"
    )

    return APY


# -------------------------
# مرحله دوم
# -------------------------

async def staking_apy(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["apy"] = float(
            update.message.text
        )

    except:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return APY

    await update.message.reply_text(
        "⏳ مدت استیکینگ (ماه):"
    )

    return MONTH


# -------------------------
# مرحله سوم
# -------------------------

async def staking_month(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        months = float(update.message.text)

    except:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return MONTH


    amount = context.user_data["amount"]

    apy = context.user_data["apy"]


    profit = amount * (apy / 100) * (months / 12)

    final_amount = amount + profit


    await update.message.reply_text(

        f"""
📊 نتیجه استیکینگ

━━━━━━━━━━━━

🪙 سرمایه اولیه:
{amount}

📈 سود سالانه:
{apy}%

⏳ مدت:
{months} ماه

━━━━━━━━━━━━

💰 سود:

{profit:.6f}

🪙 موجودی نهایی:

{final_amount:.6f}
"""
    )

    context.user_data.clear()

    return ConversationHandler.END


# -------------------------
# لغو
# -------------------------

async def staking_cancel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(
        "❌ عملیات لغو شد."
    )

    return ConversationHandler.END


# -------------------------
# ConversationHandler
# -------------------------

staking_handler = ConversationHandler(

    entry_points=[

        MessageHandler(
            filters.Regex(r"^⚡ سود استیکینگ$"),
            staking_start,
        )

    ],

    states={

        AMOUNT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                staking_amount,
            )

        ],

        APY: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                staking_apy,
            )

        ],

        MONTH: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                staking_month,
            )

        ],

    },

    fallbacks=[

        CommandHandler(
            "cancel",
            staking_cancel,
        )

    ],

)