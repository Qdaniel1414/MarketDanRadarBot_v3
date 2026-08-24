from telegram import Update
from telegram.ext import ContextTypes


async def diversification(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "🌳 بخش تنوع‌بخشی سرمایه\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )