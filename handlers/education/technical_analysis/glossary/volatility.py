from telegram import Update
from telegram.ext import ContextTypes


async def volatility_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "📊 نوسان (Volatility)\n\n"

        "نوسان یعنی میزان شدت تغییرات قیمت در یک بازه زمانی.\n\n"

        "اگر قیمت با سرعت زیاد بالا و پایین شود:\n"
        "📈 نوسان زیاد است.\n\n"

        "اگر قیمت آرام حرکت کند:\n"
        "📉 نوسان کم است.\n\n"

        "🔹 نوسان زیاد:\n"
        "✅ فرصت سود بیشتر\n"
        "❌ ریسک بیشتر\n\n"

        "🔹 نوسان کم:\n"
        "✅ ریسک کمتر\n"
        "❌ سود کمتر\n\n"

        "ابزارهای اندازه‌گیری نوسان:\n\n"

        "📌 ATR\n"
        "📌 Bollinger Bands\n"
        "📌 Historical Volatility\n\n"

        "مثال:\n"
        "اگر بیت‌کوین در یک روز ۱۰٪ حرکت کند، بازار بسیار پرنوسان است.\n"
        "اگر فقط ۱٪ حرکت کند، بازار کم‌نوسان محسوب می‌شود.\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "هرچه نوسان بیشتر باشد، حجم معامله باید کمتر باشد."
    )

    await update.message.reply_text(text)