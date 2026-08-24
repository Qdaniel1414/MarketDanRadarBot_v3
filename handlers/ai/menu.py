from telegram import Update
from telegram.ext import ContextTypes

from keyboards.ai_keyboard import ai_keyboard


async def ai_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    await update.message.reply_text(
        "🤖 دستیار هوشمند\n\n"
        "لطفاً یکی از قابلیت‌های دستیار را انتخاب کنید:",
        reply_markup=ai_keyboard,
    )