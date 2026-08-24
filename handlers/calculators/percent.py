from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_percent(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["number"] = None

    await update.message.reply_text(
        "🧮 ماشین حساب درصد\n\n"
        "عدد اصلی را وارد کن:"
    )

    return 1


async def percent_handler(
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
            "❌ لطفاً فقط عدد وارد کن."
        )

        return 1


    if context.user_data["number"] is None:

        context.user_data["number"] = value

        await update.message.reply_text(
            "چند درصد را حساب کنم؟"
        )

        return 1


    number = context.user_data["number"]

    percent = value

    result = (number * percent) / 100

    await update.message.reply_text(
        f"""✅ نتیجه محاسبه

📌 عدد:
{number:,.2f}

📌 درصد:
{percent:.2f}%

🎯 حاصل:
{result:,.2f}
"""
    )

    context.user_data.clear()

    return ConversationHandler.END