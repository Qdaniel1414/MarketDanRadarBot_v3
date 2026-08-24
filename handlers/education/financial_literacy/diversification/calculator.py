from telegram import Update
from telegram.ext import ContextTypes


async def diversification_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
🧮 ماشین حساب تنوع‌بخشی سرمایه

فرض کنید:

💰 سرمایه کل:
1,000,000,000 تومان

━━━━━━━━━━━━━━━━━━

تقسیم پیشنهادی:

🥇 طلا:
30٪
= 300,000,000 تومان

💵 دلار:
25٪
= 250,000,000 تومان

₿ بیت‌کوین:
20٪
= 200,000,000 تومان

📈 سهام:
15٪
= 150,000,000 تومان

🏦 سپرده نقد:
10٪
= 100,000,000 تومان

━━━━━━━━━━━━━━━━━━

📌 نتیجه:

هیچ دارایی بیش از حد بزرگ نیست
و ریسک کل سرمایه کاهش پیدا می‌کند.
"""
    )