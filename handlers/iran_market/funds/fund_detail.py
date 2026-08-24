from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.gold_funds_service import (
    get_tala,
    get_ayar,
    get_gohar,
    get_zar,
    get_kahraba,
    get_nafis,
    get_javaher,
)


async def fund_detail(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("FUND DETAIL CALLED")

    if update.message is None:
        return

    text = update.message.text

    if text == "طلا":
        data = get_tala()

    elif text == "عیار":
        data = get_ayar()

    elif text == "گوهر":
        data = get_gohar()

    elif text == "زر":
        data = get_zar()

    elif text == "کهربا":
        data = get_kahraba()

    elif text == "نفیس":
        data = get_nafis()

    elif text == "جواهر":
        data = get_javaher()

    else:
        return

    if data is None:
        await update.message.reply_text(
            "❌ اطلاعات صندوق پیدا نشد."
        )
        return

    message = f"""
🥇 <b>صندوق {data["name"]}</b>

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