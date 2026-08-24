from telegram import Update
from telegram.ext import ContextTypes


async def time_value(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "⏳ بخش ارزش زمانی پول\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )