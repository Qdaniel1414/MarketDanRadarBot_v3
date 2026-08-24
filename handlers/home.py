from telegram import Update
from telegram.ext import ContextTypes

from handlers.start import start


async def home(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    print("HOME HANDLER EXECUTED")

    # پاک کردن وضعیت‌های موقت
    context.user_data.clear()
    context.chat_data.clear()

    return await start(update, context)