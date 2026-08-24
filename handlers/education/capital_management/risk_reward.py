from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from states.education_states import (
    RR_ENTRY,
    RR_STOP,
    RR_TARGET,
)


async def risk_reward_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("⚠️ CAPITAL MANAGEMENT RISK REWARD START CALLED:", repr(update.message.text))
    await update.message.reply_text(
        "💵 قیمت ورود را وارد کنید:"
    )

    return RR_ENTRY


async def rr_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        context.user_data["entry"] = float(update.message.text)
    except ValueError:
        await update.message.reply_text("❌ فقط عدد وارد کنید.")
        return RR_ENTRY

    await update.message.reply_text(
        "🛑 حد ضرر را وارد کنید:"
    )

    return RR_STOP


async def rr_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        context.user_data["stop"] = float(update.message.text)
    except ValueError:
        await update.message.reply_text("❌ فقط عدد وارد کنید.")
        return RR_STOP

    await update.message.reply_text(
        "🎯 حد سود را وارد کنید:"
    )

    return RR_TARGET


async def rr_target(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        target = float(update.message.text)
    except ValueError:
        await update.message.reply_text("❌ فقط عدد وارد کنید.")
        return RR_TARGET

    entry = context.user_data["entry"]
    stop = context.user_data["stop"]

    risk = abs(entry - stop)
    reward = abs(target - entry)

    if risk == 0:
        await update.message.reply_text("❌ حد ضرر نمی‌تواند برابر قیمت ورود باشد.")
        return ConversationHandler.END

    rr = reward / risk

    await update.message.reply_text(
        f"✅ نتیجه\n\n"
        f"ریسک: {risk:.2f}\n"
        f"سود: {reward:.2f}\n\n"
        f"📈 نسبت ریسک به ریوارد:\n"
        f"1 : {rr:.2f}"
    )

    context.user_data.clear()

    return ConversationHandler.END


risk_reward_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex(r"^⚖️ ریسک به ریوارد$"),
            risk_reward_start,
        )
    ],
    states={
        RR_ENTRY: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, rr_entry)
        ],
        RR_STOP: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, rr_stop)
        ],
        RR_TARGET: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, rr_target)
        ],
    },
    fallbacks=[],
)