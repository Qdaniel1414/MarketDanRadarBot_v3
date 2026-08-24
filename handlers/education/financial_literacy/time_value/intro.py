from telegram import Update
from telegram.ext import ContextTypes


async def time_value_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = """
📘 ارزش زمانی پول چیست؟

ارزش زمانی پول (Time Value of Money) یعنی:

یک تومان امروز،
از یک تومان در آینده باارزش‌تر است.

چرا؟

✅ امکان سرمایه‌گذاری
✅ دریافت سود
✅ تورم
✅ کاهش قدرت خرید

مثال:

اگر امروز 100 میلیون تومان داشته باشید
و سالانه 30٪ سود بگیرید،

سال بعد:

130 میلیون تومان خواهید داشت.

اما اگر یک سال صبر کنید
و همان 100 میلیون را دریافت کنید،

در واقع ارزش واقعی پول شما کمتر شده است.

🎯 بنابراین:

پول امروز همیشه ارزشمندتر از همان پول در آینده است.
"""

    await update.message.reply_text(text)