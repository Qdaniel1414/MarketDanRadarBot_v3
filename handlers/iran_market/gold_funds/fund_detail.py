from telegram import Update
from telegram.ext import ContextTypes

from keyboards.iran_market.gold_fund_keyboard import (
    gold_fund_keyboard,
)


async def gold_fund_detail(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    symbol = update.message.text

    text = f"""
🥇 صندوق {symbol}

💰 قیمت:
بزودی...

📈 NAV:
بزودی...

🔥 حباب:
بزودی...

📊 بازده روزانه:
بزودی...

📅 بازده هفتگی:
بزودی...

📅 بازده ماهانه:
بزودی...

💵 ارزش معاملات:
بزودی...

────────────────
"""

    await update.message.reply_text(
        text,
        reply_markup=gold_fund_keyboard(),
    )