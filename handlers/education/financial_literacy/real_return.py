from telegram import Update
from telegram.ext import ContextTypes


async def real_return(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📊 بخش بازده واقعی\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )