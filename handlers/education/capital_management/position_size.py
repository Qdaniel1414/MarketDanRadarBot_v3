from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from states.capital_management_states import UNIT, CAPITAL, RISK


async def position_size_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💱 واحد سرمایه را انتخاب کنید:\n\n"
        "1️⃣ تومان\n"
        "2️⃣ دلار\n\n"
        "فقط یکی را ارسال کنید."
    )
    return UNIT


async def get_unit(update: Update, context: ContextTypes.DEFAULT_TYPE):

    unit = update.message.text.strip()

    if unit not in ["تومان", "دلار"]:
        await update.message.reply_text("❌ فقط «تومان» یا «دلار» را وارد کنید.")
        return UNIT

    context.user_data["unit"] = unit

    await update.message.reply_text(
        f"💰 سرمایه خود را به {unit} وارد کنید:"
    )

    return CAPITAL


async def get_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        capital = float(update.message.text.replace(",", ""))

    except:
        await update.message.reply_text("❌ فقط عدد وارد کنید.")
        return CAPITAL

    context.user_data["capital"] = capital

    await update.message.reply_text(
        "⚠️ درصد ریسک هر معامله را وارد کنید.\n\n"
        "مثال:\n"
        "1\n"
        "2\n"
        "0.5"
    )

    return RISK


async def calculate_position(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        risk_percent = float(update.message.text)

    except:
        await update.message.reply_text("❌ فقط عدد وارد کنید.")
        return RISK

    capital = context.user_data["capital"]
    unit = context.user_data["unit"]

    risk_amount = capital * risk_percent / 100

    await update.message.reply_text(
        f"✅ نتیجه\n\n"
        f"سرمایه: {capital:,.0f} {unit}\n"
        f"ریسک: {risk_percent}%\n\n"
        f"💰 حداکثر ریسک هر معامله:\n"
        f"{risk_amount:,.0f} {unit}"
    )

    return ConversationHandler.END


position_size_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex(r"^🧮 محاسبه اندازه پوزیشن$"),
            position_size_start,
        )
    ],
    states={
        UNIT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_unit)
        ],
        CAPITAL: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_capital)
        ],
        RISK: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_position)
        ],
    },
    fallbacks=[
        CommandHandler("cancel", lambda u, c: ConversationHandler.END),
    ],
)