from telegram import Update
from telegram.ext import ContextTypes


async def goal_saving(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "🎯 بخش پس‌انداز هدف\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )