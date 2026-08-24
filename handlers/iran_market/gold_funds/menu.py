import json

from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import ContextTypes


async def gold_funds_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    with open(
        "data/iran_market/gold_funds/gold_funds.json",
        encoding="utf-8",
    ) as file:

        funds = json.load(file)

    keyboard = []

    row = []

    for fund in funds:

        row.append(fund["symbol"])

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append(["🔙 بازار ایران"])

    await update.message.reply_text(

        "🥇 صندوق‌های طلا\n\n"
        "لطفاً صندوق موردنظر را انتخاب کنید:",

        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
        ),
    )