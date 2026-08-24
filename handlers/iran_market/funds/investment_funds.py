from telegram import Update
from telegram.ext import ContextTypes

from keyboards.investment_funds_keyboard import (
    investment_funds_keyboard,
)


async def investment_funds(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🏦 بخش صندوق‌های سرمایه‌گذاری\n\n"
        "لطفاً نوع صندوق را انتخاب کنید:",
        reply_markup=investment_funds_keyboard,
    )