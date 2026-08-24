from telegram import Update
from telegram.ext import ContextTypes

from keyboards.market_keyboard import market_keyboard


async def back_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    await update.message.reply_text(
        "📊 برگشت به منوی قیمت‌های بازار",
        reply_markup=market_keyboard
    )