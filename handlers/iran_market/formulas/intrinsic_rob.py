from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.coin_service import (
    get_rob_intrinsic,
)


async def intrinsic_rob(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    data = get_rob_intrinsic()

    text = f"""
🥉 <b>ارزش ذاتی ربع سکه</b>

━━━━━━━━━━━━━━

⚖️ وزن سکه

<b>{data["weight"]}</b> گرم

🌍 اونس جهانی

<b>{data["ounce"]}</b> دلار

💵 نرخ دلار

<b>{data["dollar"]:,}</b> تومان

━━━━━━━━━━━━━━

💰 ارزش ذاتی

<b>{data["intrinsic"]:,}</b> تومان

🏪 قیمت بازار

<b>{data["market"]:,}</b> تومان

🫧 حباب

<b>{data["bubble"]:,}</b> تومان

📊 درصد حباب

<b>{data["bubble_percent"]:.2f}%</b>

━━━━━━━━━━━━━━
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )