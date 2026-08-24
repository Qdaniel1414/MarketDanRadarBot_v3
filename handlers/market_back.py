from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_keyboard import main_keyboard



async def market_back_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    await update.message.reply_text(
        "🏠 منوی اصلی",
        reply_markup=main_keyboard
    )