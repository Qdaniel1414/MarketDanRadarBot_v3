from telegram import Update
from telegram.ext import ContextTypes

from services.provider_crypto import get_crypto_prices


async def crypto_prices(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    print("🔥 CRYPTO HANDLER EXECUTED")

    if update.message is None:
        print("❌ CRYPTO: update.message is None")
        return

    print("✅ CRYPTO MESSAGE EXISTS")

    try:
        print("🔍 GETTING CRYPTO PRICES...")

        prices = get_crypto_prices()

        print("✅ CRYPTO PRICES RESULT:", repr(prices))

    except Exception as e:
        print("❌ CRYPTO PROVIDER ERROR:", repr(e))

        await update.message.reply_text(
            f"❌ خطا در دریافت قیمت ارزهای دیجیتال:\n\n{e}"
        )

        return

    if not prices:
        print("❌ CRYPTO PRICES EMPTY")

        await update.message.reply_text(
            "❌ قیمت‌های ارزهای دیجیتال در حال حاضر در دسترس نیست."
        )

        return

    text = (
        "₿ قیمت لحظه‌ای ارزهای دیجیتال\n\n"
    )

    for coin, price in prices.items():

        text += f"• {coin}: ${price}\n"

    print("📤 SENDING CRYPTO MESSAGE")

    try:

        await update.message.reply_text(
            text
        )

        print("✅ CRYPTO MESSAGE SENT")

    except Exception as e:

        print("❌ TELEGRAM SEND ERROR:", repr(e))