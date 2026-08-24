from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_tp_sl(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["entry"] = None
    context.user_data["tp_percent"] = None
    context.user_data["sl_percent"] = None

    await update.message.reply_text(
        "🎯 ماشین حساب حد سود و ضرر\n\n"
        "💰 قیمت ورود را وارد کنید:"
    )

    return 5


async def tp_sl_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:

        value = float(
            update.message.text.replace(",", "")
        )

    except:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return 5


    if context.user_data["entry"] is None:

        context.user_data["entry"] = value

        await update.message.reply_text(
            "📈 درصد سود (TP) را وارد کنید:"
        )

        return 5


    if context.user_data["tp_percent"] is None:

        context.user_data["tp_percent"] = value

        await update.message.reply_text(
            "📉 درصد ضرر (SL) را وارد کنید:"
        )

        return 5


    context.user_data["sl_percent"] = value

    entry = context.user_data["entry"]
    tp = context.user_data["tp_percent"]
    sl = context.user_data["sl_percent"]

    take_profit = entry * (1 + tp / 100)
    stop_loss = entry * (1 - sl / 100)

    await update.message.reply_text(
        f"""🎯 نتیجه TP / SL

💰 قیمت ورود:
{entry:,.2f}

━━━━━━━━━━━━━━

📈 درصد سود:
{tp:.2f}%

🎯 Take Profit:
{take_profit:,.2f}

━━━━━━━━━━━━━━

📉 درصد ضرر:
{sl:.2f}%

🛑 Stop Loss:
{stop_loss:,.2f}
"""
    )

    context.user_data.clear()

    return ConversationHandler.END