from telegram import Update
from telegram.ext import ContextTypes


async def budget_50_30_20_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        """
📈 مثال واقعی قانون 50/30/20

فرض کنید:

💰 درآمد:

100 میلیون تومان

━━━━━━━━━━━━━━

🏠 نیازها

50 میلیون

━━━━━━━━━━━━━━

🎯 خواسته‌ها

30 میلیون

━━━━━━━━━━━━━━

📈 سرمایه‌گذاری

20 میلیون

━━━━━━━━━━━━━━

اگر هر ماه

20 میلیون

را سرمایه‌گذاری کنید،

بعد از چند سال

سرمایه بزرگی خواهید داشت.

📌 رمز موفقیت

اول سرمایه‌گذاری کنید،

بعد خرج کنید.
"""
    )