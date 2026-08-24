from telegram import Update
from telegram.ext import ContextTypes


async def breakout_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🚀 بریک اوت (Breakout)\n\n"

        "بریک اوت یعنی شکسته شدن یک سطح مهم "
        "حمایت یا مقاومت.\n\n"

        "وقتی قیمت از یک مقاومت عبور می‌کند:\n"
        "📈 Breakout صعودی رخ می‌دهد.\n\n"

        "وقتی قیمت یک حمایت را می‌شکند:\n"
        "📉 Breakout نزولی رخ می‌دهد.\n\n"

        "ویژگی‌های یک بریک اوت معتبر:\n\n"

        "✔ حجم معاملات بالا\n"
        "✔ بسته شدن کندل پشت سطح\n"
        "✔ ادامه حرکت قیمت\n\n"

        "❌ اشتباه رایج:\n"
        "ورود قبل از بسته شدن کندل.\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "همیشه منتظر تأیید بریک اوت بمان، "
        "نه فقط لمس سطح."
    )

    await update.message.reply_text(text)