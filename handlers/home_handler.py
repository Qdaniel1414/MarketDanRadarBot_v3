from telegram import Update
from telegram.ext import ContextTypes

from handlers.start import start


async def home_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message is None:
        return

    # پاک کردن تمام وضعیت‌های Conversation
    context.user_data.clear()

    # اگر state سراسری داری
    context.chat_data.clear()

    return await start(update, context)