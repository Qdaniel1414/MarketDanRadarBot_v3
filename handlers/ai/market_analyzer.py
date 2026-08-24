from telegram import Update
from telegram.ext import ContextTypes

from keyboards.market_analyzer_keyboard import market_analyzer_keyboard


async def market_analyzer_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📊 تحلیلگر هوشمند بازار\n\n"
        "لطفاً بازار موردنظر برای تحلیل را انتخاب کنید:",
        reply_markup=market_analyzer_keyboard,
    )