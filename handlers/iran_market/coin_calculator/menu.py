import json

from telegram import Update
from telegram.ext import ContextTypes

from keyboards.iran_market.coin_calculator_keyboard import (
    coin_calculator_keyboard,
)


async def coin_calculator_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    with open(
        "data/iran_market/coin_calculator/menu.json",
        encoding="utf-8",
    ) as file:

        items = json.load(file)

    text = "🥇 محاسبه سکه\n\n"

    text += "لطفاً نوع سکه را انتخاب کنید:"

    await update.message.reply_text(

        text,

        reply_markup=coin_calculator_keyboard(items),

    )