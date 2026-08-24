from telegram import Update
from telegram.ext import ContextTypes


async def roi(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📈 بخش ROI\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )