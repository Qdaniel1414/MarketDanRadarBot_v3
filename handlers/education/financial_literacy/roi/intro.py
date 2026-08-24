from telegram import Update
from telegram.ext import ContextTypes


async def roi_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📈 ROI چیست؟\n\n"

        "ROI مخفف Return On Investment است.\n\n"

        "یعنی:\n"
        "بازده سرمایه‌گذاری\n\n"

        "ROI نشان می‌دهد یک سرمایه‌گذاری چقدر سود یا زیان ایجاد کرده است.\n\n"

        "فرمول:\n\n"

        "ROI = (سود خالص ÷ سرمایه اولیه) × 100\n\n"

        "اگر ROI مثبت باشد یعنی سرمایه‌گذاری سودآور بوده است.\n"
        "اگر منفی باشد یعنی سرمایه‌گذاری زیان‌ده بوده است."
    )