from telegram import Update
from telegram.ext import ContextTypes

from keyboards.iran_market.dollar_calculator_keyboard import (
    dollar_calculator_keyboard,
)


async def dollar_calculator_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("dollar_calculator_menu called")

    if update.message is None:
        return

    await update.message.reply_text(
        "💵 محاسبه دلار\n\n"
        "لطفاً نوع محاسبه را انتخاب کنید:",
        reply_markup=dollar_calculator_keyboard,
    )