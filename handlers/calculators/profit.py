from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_profit(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["buy"] = None
    context.user_data["sell"] = None

    await update.message.reply_text(
        "💰 ماشین حساب سود و زیان\n\n"
        "قیمت خرید را وارد کنید:"
    )

    return 2


async def profit_handler(
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

        return 2


    if context.user_data["buy"] is None:

        context.user_data["buy"] = value

        await update.message.reply_text(
            "💵 قیمت فروش را وارد کنید:"
        )

        return 2


    if context.user_data["sell"] is None:

        context.user_data["sell"] = value

        await update.message.reply_text(
            "📦 تعداد را وارد کنید:"
        )

        return 2


    buy = context.user_data["buy"]
    sell = context.user_data["sell"]
    qty = value

    profit = (sell - buy) * qty
    percent = ((sell - buy) / buy) * 100

    if profit >= 0:
        status = "📈 سود"
    else:
        status = "📉 زیان"

    await update.message.reply_text(
        f"""💰 نتیجه معامله

📌 قیمت خرید:
{buy:,.0f}

📌 قیمت فروش:
{sell:,.0f}

📌 تعداد:
{qty:,.2f}

━━━━━━━━━━━━━━

{status}:
{profit:,.2f}

📊 درصد:
{percent:.2f}%
"""
    )

    context.user_data.clear()

    return ConversationHandler.END