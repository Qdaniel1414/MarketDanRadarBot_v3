from telegram import Update
from telegram.ext import ContextTypes


async def real_return_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
📊 مثال واقعی بازده واقعی

فرض کنید:

💰 سود سرمایه‌گذاری:

40٪

📉 نرخ تورم:

25٪

━━━━━━━━━━━━━━━━━━

بازده واقعی:

15٪

━━━━━━━━━━━━━━━━━━

یعنی:

اگر امروز

100 میلیون تومان

سرمایه‌گذاری کنید

و بعد از یک سال

140 میلیون تومان

داشته باشید

اما تورم

25٪

باشد،

قدرت خرید واقعی شما

فقط

15٪

افزایش پیدا کرده است.

📌 بنابراین همیشه
بازده واقعی مهم‌تر از
بازده اسمی است.
"""
    )