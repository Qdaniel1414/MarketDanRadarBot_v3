import json

from telegram import Update
from telegram.ext import ContextTypes


async def real_estate_funds(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    with open(
        "data/iran_market/funds/real_estate_funds.json",
        encoding="utf-8",
    ) as file:

        funds = json.load(file)

    text = "🏠 صندوق‌های املاک و مستغلات\n\n"

    for fund in funds:

        text += (
            f"🔹 {fund['symbol']}\n"
            f"{fund['name']}\n\n"
        )

    await update.message.reply_text(text)