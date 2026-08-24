from telegram import Update
from telegram.ext import ContextTypes


async def active_passive_income(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "💼 بخش درآمد فعال و غیرفعال\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )