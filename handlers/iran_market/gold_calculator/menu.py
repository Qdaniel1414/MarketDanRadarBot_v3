from telegram import Update
from telegram.ext import ContextTypes

from keyboards.iran_market.gold_calculator_keyboard import (
    gold_calculator_keyboard,
)


async def gold_calculator_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("gold_calculator_menu called")

    if update.message is None:
        return

    await update.message.reply_text(
        "🪙 محاسبه طلا\n\n"
        "لطفاً نوع محاسبه را انتخاب کنید:",
        reply_markup=gold_calculator_keyboard,
    )