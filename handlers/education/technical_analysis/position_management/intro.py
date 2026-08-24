from telegram import Update
from telegram.ext import ContextTypes


async def position_management_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "⚖️ مدیریت پوزیشن چیست؟\n\n"

        "مدیریت پوزیشن یعنی قبل از ورود به معامله مشخص کنید:\n\n"

        "• چند درصد سرمایه را ریسک می‌کنید.\n"
        "• حد ضرر کجاست.\n"
        "• حجم معامله چقدر باشد.\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "🎯 هدف مدیریت پوزیشن:\n"
        "حفظ سرمایه و جلوگیری از ضررهای سنگین.\n\n"

        "معامله‌گران حرفه‌ای همیشه قبل از ورود، "
        "حجم معامله را بر اساس میزان ریسک محاسبه می‌کنند."
    )

    await update.message.reply_text(text)