from telegram import Update
from telegram.ext import ContextTypes


async def goal_saving_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = """
📈 مثال واقعی پس‌انداز هدف

فرض کنید:

🎯 هدف:
5,000,000,000 تومان

💰 سرمایه اولیه:
500,000,000 تومان

💵 پس‌انداز ماهانه:
20,000,000 تومان

📈 سود سالانه:
30٪

📅 مدت:
10 سال

━━━━━━━━━━━━━━━━━━

نتیجه:

💰 سرمایه نهایی:

حدود

6,200,000,000 تومان

━━━━━━━━━━━━━━━━━━

یعنی:

✅ حدود
1.2 میلیارد تومان
بیشتر از هدف خود سرمایه خواهید داشت.

📌 اگر مبلغ پس‌انداز ماهانه را کمتر کنید،
سرمایه نهایی نیز کاهش پیدا می‌کند.

به همین دلیل برنامه‌ریزی صحیح
اهمیت زیادی دارد.
"""

    await update.message.reply_text(text)