from telegram import Update
from telegram.ext import ContextTypes

import json
from pathlib import Path


PRICE_FILE = Path("data/manual_prices.json")


def load_prices():

    with open(
        PRICE_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def format_price(price):

    if not price:
        return "نامشخص"

    return f"{price:,} تومان"



async def currency_prices(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("CURRENCY HANDLER EXECUTED")

    if update.message is None:
        return


    data = load_prices()


    prices = data.get(
        "currency",
        {}
    )


    text = f"""
💵 قیمت لحظه‌ای ارز 🇮🇷

━━━━━━━━━━━━━━

🇺🇸 دلار آمریکا:
{format_price(prices.get("usd"))}

💲 تتر:
{format_price(prices.get("usdt"))}

🇦🇪 درهم امارات:
{format_price(prices.get("aed"))}

🇪🇺 یورو:
{format_price(prices.get("eur"))}

🇬🇧 پوند انگلیس:
{format_price(prices.get("gbp"))}

🇹🇷 لیر ترکیه:
{format_price(prices.get("try"))}

━━━━━━━━━━━━━━

📌 اطلاعات به صورت دستی بروزرسانی می‌شود.
"""


    await update.message.reply_text(text)