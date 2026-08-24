from telegram import Update
from telegram.ext import ContextTypes

from keyboards.iran_market_keyboard import (
    iran_market_keyboard,
)


async def iran_market_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🇮🇷 بازار ایران\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=iran_market_keyboard,
    )