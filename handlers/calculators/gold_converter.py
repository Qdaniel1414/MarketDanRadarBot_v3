from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_gold_converter(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["price"] = None
    context.user_data["weight"] = None

    await update.message.reply_text(
        "🪙 ماشین حساب تبدیل طلا\n\n"
        "💰 قیمت هر گرم طلا را وارد کنید:"
    )

    return 8


async def gold_converter_handler(
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

        return 8


    if context.user_data["price"] is None:

        context.user_data["price"] = value

        await update.message.reply_text(
            "⚖️ وزن طلا (گرم) را وارد کنید:"
        )

        return 8


    context.user_data["weight"] = value

    price = context.user_data["price"]
    weight = context.user_data["weight"]

    total = price * weight

    await update.message.reply_text(
        f"""🪙 نتیجه تبدیل طلا

💰 قیمت هر گرم:
{price:,.0f} تومان

⚖️ وزن:
{weight:.2f} گرم

━━━━━━━━━━━━━━

💵 ارزش کل:

{total:,.0f} تومان
"""
    )

    context.user_data.clear()

    return ConversationHandler.END