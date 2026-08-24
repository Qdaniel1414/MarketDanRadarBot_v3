from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_risk_reward(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["entry"] = None
    context.user_data["stop"] = None
    context.user_data["target"] = None

    await update.message.reply_text(
        "⚖️ ماشین حساب ریسک به ریوارد\n\n"
        "💰 قیمت ورود را وارد کنید:"
    )

    return 6


async def risk_reward_handler(
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

        return 6


    if context.user_data["entry"] is None:

        context.user_data["entry"] = value

        await update.message.reply_text(
            "🛑 قیمت حد ضرر را وارد کنید:"
        )

        return 6


    if context.user_data["stop"] is None:

        context.user_data["stop"] = value

        await update.message.reply_text(
            "🎯 قیمت حد سود را وارد کنید:"
        )

        return 6


    context.user_data["target"] = value

    entry = context.user_data["entry"]
    stop = context.user_data["stop"]
    target = context.user_data["target"]

    risk = abs(entry - stop)
    reward = abs(target - entry)

    if risk == 0:

        rr = 0

    else:

        rr = reward / risk

    await update.message.reply_text(
        f"""⚖️ نتیجه ریسک به ریوارد

💰 قیمت ورود:
{entry:,.2f}

🛑 حد ضرر:
{stop:,.2f}

🎯 حد سود:
{target:,.2f}

━━━━━━━━━━━━━━

📉 ریسک:
{risk:,.2f}

📈 ریوارد:
{reward:,.2f}

⚖️ نسبت ریسک به ریوارد:

1 : {rr:.2f}
"""
    )

    context.user_data.clear()

    return ConversationHandler.END