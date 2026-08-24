from telegram import Update
from telegram.ext import (
    ContextTypes,
    MessageHandler,
    filters,
)


async def one_percent(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message is None:
        return

    text = """
📏 قانون ۱٪ چیست؟

قانون ۱٪ یعنی:

در هر معامله حداکثر فقط ۱٪ از کل سرمایه خود را در معرض ریسک قرار دهید.

━━━━━━━━━━━━━━

مثال:

💰 سرمایه شما:
100,000,000 تومان

حداکثر ریسک هر معامله:

1,000,000 تومان

یعنی اگر حد ضرر فعال شود،
بیش از یک میلیون تومان ضرر نمی‌کنید.

━━━━━━━━━━━━━━

🎯 مزایای قانون ۱٪

✅ جلوگیری از نابودی حساب
✅ کنترل احساسات
✅ دوام بیشتر در بازار
✅ امکان جبران ضررها

━━━━━━━━━━━━━━

📌 معامله‌گران حرفه‌ای

اول مقدار ریسک را مشخص می‌کنند،
بعد وارد معامله می‌شوند.
"""

    await update.message.reply_text(text)


one_percent_router = MessageHandler(
    filters.Regex(r"^📏 قانون ۱٪$"),
    one_percent,
)