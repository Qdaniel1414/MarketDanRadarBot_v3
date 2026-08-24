from telegram import Update
from telegram.ext import ContextTypes


async def position_management_mistakes(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "💡 اشتباهات رایج مدیریت پوزیشن\n\n"

        "❌ ورود با تمام سرمایه\n\n"

        "❌ نداشتن حد ضرر\n\n"

        "❌ افزایش حجم معامله بعد از ضرر\n\n"

        "❌ جابجا کردن حد ضرر\n\n"

        "❌ ریسک بیش از ۲٪ سرمایه در یک معامله\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "اول از سرمایه محافظت کن، بعد به فکر سود باش."
    )