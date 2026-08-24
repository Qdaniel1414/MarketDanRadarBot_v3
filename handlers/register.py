from telegram import Update
from telegram.ext import ContextTypes

from keyboards.register_keyboard import register_keyboard


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📱 برای ادامه ثبت‌نام، لطفاً شماره موبایل خود را ارسال کنید.",
        reply_markup=register_keyboard,
    )