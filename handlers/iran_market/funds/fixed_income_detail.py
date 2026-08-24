from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.fixed_income_service import (
    get_yak,
    get_kar,
    get_aman,
)


async def fixed_income_detail(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text

    if text == "یکم":
        data = get_yak()

    elif text == "کارا":
        data = get_kar()

    elif text == "امان":
        data = get_aman()

    else:
        return

    if data is None:

        await update.message.reply_text(
            "❌ اطلاعات صندوق پیدا نشد."
        )

        return

    message = f"""
🏦 <b>صندوق {data["name"]}</b>

━━━━━━━━━━━━━━

💰 قیمت بازار

<b>{data["market"]:,}</b> تومان

💎 NAV

<b>{data["nav"]:,}</b> تومان

━━━━━━━━━━━━━━

🫧 حباب

<b>{data["bubble"]:,}</b> تومان

📊 درصد حباب

<b>{data["bubble_percent"]:.2f}%</b>

━━━━━━━━━━━━━━

📈 بازده روزانه

<b>{data["daily"]:.2f}%</b>

📈 بازده هفتگی

<b>{data["weekly"]:.2f}%</b>

📈 بازده ماهانه

<b>{data["monthly"]:.2f}%</b>

━━━━━━━━━━━━━━

💵 ارزش معاملات

<b>{data["value"]:,}</b> تومان
"""

    await update.message.reply_text(
        message,
        parse_mode=ParseMode.HTML,
    )