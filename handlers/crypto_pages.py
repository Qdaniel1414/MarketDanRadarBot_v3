from telegram import Update
from telegram.ext import ContextTypes

from keyboards.crypto_keyboard import crypto_keyboard


async def crypto_page_1(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    prices = context.user_data.get(
        "crypto_prices",
        []
    )

    text = "₿ قیمت صفحه ۱\n\n"

    for coin, price in prices[:9]:

        text += f"• {coin}: ${price}\n"


    await update.message.reply_text(
        text,
        reply_markup=crypto_keyboard,
    )



async def crypto_page_2(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    prices = context.user_data.get(
        "crypto_prices",
        []
    )

    text = "₿ قیمت صفحه ۲\n\n"


    for coin, price in prices[9:]:

        text += f"• {coin}: ${price}\n"


    if text == "₿ قیمت صفحه ۲\n\n":

        text += "❌ ارز دیگری موجود نیست."


    await update.message.reply_text(
        text,
        reply_markup=crypto_keyboard,
    )