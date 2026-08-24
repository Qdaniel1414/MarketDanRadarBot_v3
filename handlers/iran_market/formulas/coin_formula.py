from telegram import Update
from telegram.ext import ContextTypes


async def coin_formula(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🥇 فرمول محاسبه سکه\n\n"
        "🚧 این بخش به‌زودی تکمیل می‌شود."
    )