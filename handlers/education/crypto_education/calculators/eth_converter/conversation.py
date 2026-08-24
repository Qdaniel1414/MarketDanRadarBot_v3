from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from .states import (
    AMOUNT,
    PRICE,
)

import json
from pathlib import Path


PRICE_FILE = Path("data/manual_prices.json")


def load_prices():
    with open(
        PRICE_FILE,
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)


# =====================================
# شروع
# =====================================

async def eth_converter_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        """
💎 ماشین حساب اتریوم

مرحله ۱ از ۲

💎 مقدار اتریوم را وارد کنید:

مثال:

2.5
"""
    )

    return AMOUNT


# =====================================
# مرحله اول
# =====================================

async def ethereum_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("ETH AMOUNT HANDLER RUN")

    try:

        amount = float(
            update.message.text.replace(",", "")
        )

        context.user_data["eth_amount"] = amount

        await update.message.reply_text(
            """
مرحله ۲ از ۲

💰 قیمت هر ETH را وارد کنید.

اگر عددی وارد نکنید،
از قیمت لحظه‌ای ربات استفاده می‌شود.

مثال:

3500
"""
        )

        return PRICE

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return AMOUNT


# =====================================
# مرحله دوم
# =====================================

async def eth_converter_price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        text = update.message.text.strip()

        amount = context.user_data["eth_amount"]

        # خواندن آخرین قیمت‌های دستی
        data = load_prices()

        # اگر کاربر قیمت ETH وارد نکند،
        # قیمت ETH از فایل قیمت‌های دستی خوانده می‌شود.
        if text == "":
            eth_price = data["global"]["ethereum"]
        else:
            eth_price = float(
                text.replace(",", "")
            )

        # نرخ دلار همیشه از قیمت دستی روز خوانده می‌شود.
        dollar_price = data["currency"]["usd"]

        usd_value = amount * eth_price

        toman_value = usd_value * dollar_price

        await update.message.reply_text(
            f"""
📊 نتیجه تبدیل اتریوم

━━━━━━━━━━━━

💎 مقدار:

{amount} ETH

💵 ارزش دلاری:

{usd_value:,.2f}$

🇮🇷 ارزش تومانی:

{toman_value:,.0f} تومان

━━━━━━━━━━━━

📌 قیمت هر ETH:

{eth_price:,.2f}$

💵 نرخ دلار:

{dollar_price:,.0f} تومان
"""
        )

        context.user_data.clear()

        return ConversationHandler.END

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return PRICE


# =====================================
# Handler
# =====================================

eth_converter_handler = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(
                r"^💎 تبدیل ETH ↔ دلار / تومان$"
            ),
            eth_converter_intro,
        )
    ],

    states={

        AMOUNT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                ethereum_input,
            )
        ],

        PRICE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                eth_converter_price,
            )
        ],

    },

    fallbacks=[],

)