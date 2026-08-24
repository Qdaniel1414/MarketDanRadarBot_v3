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

async def btc_converter_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("BTC CONVERSATION START")

    await update.message.reply_text(
        """
₿ ماشین حساب بیت کوین

مرحله ۱ از ۲

🪙 مقدار بیت کوین را وارد کنید:

مثال:

0.5
"""
    )

    return AMOUNT


# =====================================
# مرحله اول
# =====================================

async def btc_converter_amount(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("BTC AMOUNT HANDLER RUN")

    try:

        amount = float(
            update.message.text.replace(",", "")
        )

        context.user_data["btc_amount"] = amount

        await update.message.reply_text(
            """
مرحله ۲ از ۲

💰 قیمت هر BTC را وارد کنید.

اگر عددی وارد نکنی،
قیمت لحظه‌ای ربات استفاده می‌شود.

مثال:

65000
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

async def btc_converter_price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("BTC PRICE HANDLER RUN")

    try:

        text = update.message.text.replace(
            ",",
            "",
        ).strip()

        amount = context.user_data["btc_amount"]

        # خواندن آخرین قیمت‌های دستی
        data = load_prices()

        # اگر کاربر قیمت BTC وارد نکرد،
        # قیمت BTC از فایل قیمت‌های دستی خوانده می‌شود.
        if text == "":
            btc_price = data["global"]["bitcoin"]
        else:
            btc_price = float(text)

        # نرخ دلار همیشه از قیمت دستی روز خوانده می‌شود.
        dollar_price = data["currency"]["usd"]

        usd_value = amount * btc_price
        toman_value = usd_value * dollar_price

        await update.message.reply_text(
            f"""
📊 نتیجه تبدیل بیت کوین

━━━━━━━━━━━━

🪙 مقدار:

{amount} BTC

💵 ارزش دلاری:

{usd_value:,.2f}$

🇮🇷 ارزش تومانی:

{toman_value:,.0f} تومان

━━━━━━━━━━━━

📌 قیمت هر BTC:

{btc_price:,.2f}$

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

btc_converter_handler = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(
                r"^💵 تبدیل BTC ↔ دلار / تومان$"
            ),
            btc_converter_intro,
        )
    ],

    states={

        AMOUNT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                btc_converter_amount,
            )
        ],

        PRICE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                btc_converter_price,
            )
        ],

    },

    fallbacks=[],

)