from telegram import Update
from telegram.ext import ContextTypes


async def volume_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "📈 مثال واقعی حجم معاملات\n\n"

        "فرض کنید قیمت بیت‌کوین از:\n\n"

        "100,000\n"
        "⬆️\n"
        "105,000\n\n"

        "افزایش پیدا کرده است.\n\n"

        "اگر این رشد با حجم معاملات بالا همراه باشد،\n"
        "احتمال ادامه روند بیشتر است.\n\n"

        "اما اگر همین رشد با حجم پایین اتفاق بیفتد،\n"
        "ممکن است صرفاً یک حرکت موقتی باشد.\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 معامله‌گران حرفه‌ای همیشه قیمت را همراه حجم بررسی می‌کنند."
    )

    await update.message.reply_text(text)