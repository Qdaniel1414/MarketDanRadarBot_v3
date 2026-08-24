from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_average(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["price1"] = None
    context.user_data["qty1"] = None
    context.user_data["price2"] = None
    context.user_data["qty2"] = None

    await update.message.reply_text(
        "📊 ماشین حساب میانگین خرید\n\n"
        "💰 قیمت خرید اول را وارد کنید:"
    )

    return 4


async def average_handler(
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

        return 4


    if context.user_data["price1"] is None:

        context.user_data["price1"] = value

        await update.message.reply_text(
            "📦 تعداد خرید اول:"
        )

        return 4


    if context.user_data["qty1"] is None:

        context.user_data["qty1"] = value

        await update.message.reply_text(
            "💰 قیمت خرید دوم:"
        )

        return 4


    if context.user_data["price2"] is None:

        context.user_data["price2"] = value

        await update.message.reply_text(
            "📦 تعداد خرید دوم:"
        )

        return 4


    context.user_data["qty2"] = value

    p1 = context.user_data["price1"]
    q1 = context.user_data["qty1"]
    p2 = context.user_data["price2"]
    q2 = context.user_data["qty2"]

    total_cost = (p1 * q1) + (p2 * q2)
    total_qty = q1 + q2
    average = total_cost / total_qty

    await update.message.reply_text(
        f"""📊 نتیجه میانگین خرید

💰 خرید اول:
{p1:,.0f}

📦 تعداد اول:
{q1:,.2f}

━━━━━━━━━━━━━━

💰 خرید دوم:
{p2:,.0f}

📦 تعداد دوم:
{q2:,.2f}

━━━━━━━━━━━━━━

📦 مجموع دارایی:
{total_qty:,.2f}

💵 ارزش کل:
{total_cost:,.2f}

🎯 میانگین خرید:
{average:,.2f}
"""
    )

    context.user_data.clear()

    return ConversationHandler.END