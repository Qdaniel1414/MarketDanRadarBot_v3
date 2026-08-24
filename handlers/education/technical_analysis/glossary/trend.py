from telegram import Update
from telegram.ext import ContextTypes


async def glossary_trend_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "📈 روند (Trend)\n\n"

        "روند یعنی جهت کلی حرکت قیمت در بازار.\n\n"

        "سه نوع روند وجود دارد:\n\n"

        "🟢 روند صعودی (Uptrend)\n"
        "قیمت سقف‌ها و کف‌های بالاتری می‌سازد.\n\n"

        "🔴 روند نزولی (Downtrend)\n"
        "قیمت سقف‌ها و کف‌های پایین‌تری می‌سازد.\n\n"

        "🟡 روند خنثی (Sideway)\n"
        "قیمت در یک محدوده مشخص نوسان می‌کند.\n\n"

        "نشانه‌های روند صعودی:\n"
        "✔ Higher High (HH)\n"
        "✔ Higher Low (HL)\n\n"

        "نشانه‌های روند نزولی:\n"
        "✔ Lower High (LH)\n"
        "✔ Lower Low (LL)\n\n"

        "❌ بزرگ‌ترین اشتباه معامله‌گران:\n"
        "معامله برخلاف روند.\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "Trend is Your Friend\n"
        "روند دوست شماست؛ تا زمانی که نشانه‌ای از پایان آن دیده نشود، برخلاف آن معامله نکن."
    )

    await update.message.reply_text(text)