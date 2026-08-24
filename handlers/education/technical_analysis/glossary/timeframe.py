from telegram import Update
from telegram.ext import ContextTypes


async def timeframe_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "⏰ تایم‌فریم (Time Frame)\n\n"

        "تایم‌فریم یعنی بازه زمانی که هر کندل نشان می‌دهد.\n\n"

        "مثال:\n\n"

        "🕐 تایم‌فریم 1 دقیقه\n"
        "هر کندل = 1 دقیقه\n\n"

        "🕔 تایم‌فریم 5 دقیقه\n"
        "هر کندل = 5 دقیقه\n\n"

        "🕒 تایم‌فریم 1 ساعت\n"
        "هر کندل = 1 ساعت\n\n"

        "📅 تایم‌فریم روزانه\n"
        "هر کندل = 1 روز\n\n"

        "📆 تایم‌فریم هفتگی\n"
        "هر کندل = 1 هفته\n\n"

        "📈 هرچه تایم‌فریم بزرگ‌تر باشد:\n"
        "✔ نویز کمتر\n"
        "✔ اعتبار تحلیل بیشتر\n"
        "✔ مناسب سرمایه‌گذاری\n\n"

        "⚡ هرچه تایم‌فریم کوچک‌تر باشد:\n"
        "✔ نوسان بیشتر\n"
        "✔ فرصت‌های بیشتر\n"
        "✔ ریسک بیشتر\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "ابتدا روند را در تایم‌فریم بزرگ پیدا کن، سپس در تایم‌فریم کوچک وارد معامله شو."
    )

    await update.message.reply_text(text)