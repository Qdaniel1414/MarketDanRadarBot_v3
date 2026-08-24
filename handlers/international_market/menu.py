from telegram import Update
from telegram.ext import ContextTypes

from keyboards.international_market_keyboard import (
    international_market_keyboard,
)


async def international_market_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🌍 بازارهای بین‌المللی\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=international_market_keyboard,
    )