from telegram import Update
from telegram.ext import ContextTypes

from keyboards.market_keyboard import market_keyboard


async def market_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📊 بخش قیمت‌های لحظه‌ای بازار\n\nلطفاً یکی از گزینه‌ها را انتخاب کنید.",
        reply_markup=market_keyboard,
    )