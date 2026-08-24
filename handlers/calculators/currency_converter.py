from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_currency_converter(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["rate"] = None
    context.user_data["amount"] = None

    await update.message.reply_text(
        "💱 ماشین حساب تبدیل ارز\n\n"
        "💵 نرخ دلار را وارد کنید:"
    )

    return 7


async def currency_converter_handler(
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

        return 7


    if context.user_data["rate"] is None:

        context.user_data["rate"] = value

        await update.message.reply_text(
            "💰 مقدار دلار را وارد کنید:"
        )

        return 7


    context.user_data["amount"] = value

    rate = context.user_data["rate"]
    amount = context.user_data["amount"]

    result = rate * amount

    await update.message.reply_text(
        f"""💱 نتیجه تبدیل ارز

💵 نرخ دلار:
{rate:,.0f}

💰 مقدار دلار:
{amount:,.2f}

━━━━━━━━━━━━━━

🇮🇷 ارزش ریالی:

{result:,.0f} تومان
"""
    )

    context.user_data.clear()

    return ConversationHandler.END