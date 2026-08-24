from telegram import Update
from telegram.ext import ContextTypes


async def budget_50_30_20(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📋 قانون بودجه 50/30/20\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )