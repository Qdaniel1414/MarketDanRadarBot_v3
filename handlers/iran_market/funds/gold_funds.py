from telegram import Update
from telegram.ext import ContextTypes

import json
from pathlib import Path

from keyboards.fund_keyboard import fund_keyboard


DATA_FILE = Path("data/gold_funds.json")


async def gold_funds(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    with open(DATA_FILE, encoding="utf-8") as f:
        funds = json.load(f)

    await update.message.reply_text(
        "🥇 صندوق‌های طلا\n\n"
        "لطفاً صندوق موردنظر را انتخاب کنید:",
        reply_markup=fund_keyboard(funds),
    )