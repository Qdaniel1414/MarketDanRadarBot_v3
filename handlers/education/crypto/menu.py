from telegram import Update
from telegram.ext import ContextTypes


async def crypto_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🪙 آموزش ارزهای دیجیتال\n\n"
        "🚧 این بخش به زودی تکمیل خواهد شد."
    )