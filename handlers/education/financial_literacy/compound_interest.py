from telegram import Update
from telegram.ext import ContextTypes

from keyboards.compound_interest_keyboard import compound_interest_keyboard


async def compound_interest(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "💹 آموزش بهره مرکب ✅\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=compound_interest_keyboard,
    )


async def compound_interest_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = """
📘 بهره مرکب چیست؟

بهره مرکب یعنی:

سودی که علاوه بر اصل سرمایه،
روی سودهای قبلی نیز محاسبه می‌شود.

فرمول:

A = P × (1 + r/n)^(nt)

اگر سود به سرمایه اضافه شود،
در دوره‌های بعدی سود روی سود نیز محاسبه می‌شود.

به همین دلیل به آن:

💰 سود روی سود

می‌گویند.

آلبرت اینشتین درباره بهره مرکب گفته است:

«بهره مرکب هشتمین عجایب دنیاست.»
"""

    await update.message.reply_text(text)


async def compound_interest_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = """
📈 مثال واقعی بهره مرکب

فرض کنید:

💰 سرمایه اولیه:
100 میلیون تومان

📈 سود سالانه:
30%

⏳ مدت:
10 سال

بدون برداشت سود:

سال اول:
130 میلیون

سال دوم:
169 میلیون

سال سوم:
219 میلیون

...

سال دهم:
بیش از 1.37 میلیارد تومان

در حالی که اگر سودها را برداشت می‌کردید:

فقط 300 میلیون سود می‌گرفتید.

🎯 تفاوت:

بهره مرکب باعث چند برابر شدن سرمایه در بلندمدت می‌شود.
"""

    await update.message.reply_text(text)