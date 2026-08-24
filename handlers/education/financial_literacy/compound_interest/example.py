from telegram import Update
from telegram.ext import ContextTypes


async def compound_interest_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
📈 مثال واقعی بهره مرکب

فرض کنید:

💰 سرمایه اولیه:
100,000,000 تومان

💵 سود سالانه:
30٪

📅 مدت:
10 سال

اگر سود را برداشت نکنید و دوباره سرمایه‌گذاری کنید:

سال اول:
130 میلیون

سال دوم:
169 میلیون

سال سوم:
219.7 میلیون

...

سال دهم:
1,378,584,918 تومان

یعنی:

✨ سرمایه شما بیش از 13 برابر می‌شود.

📌 این قدرت بهره مرکب است.
"""
    )