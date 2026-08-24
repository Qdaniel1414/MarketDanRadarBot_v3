import json

from telegram import Update
from telegram.ext import ContextTypes


async def stock_funds(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    with open(
        "data/iran_market/funds/stock_funds.json",
        "r",
        encoding="utf-8",
    ) as file:

        funds = json.load(file)

    text = "📈 صندوق‌های سهامی\n\n"

    for fund in funds:

        text += (
            f"🔹 {fund['symbol']}\n"
            f"{fund['name']}\n\n"
        )

    await update.message.reply_text(text)