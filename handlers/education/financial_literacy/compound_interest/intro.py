from telegram import Update
from telegram.ext import ContextTypes


async def compound_interest_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = """
💹 بهره مرکب چیست؟

بهره مرکب یعنی:

سود فقط روی سرمایه اولیه محاسبه نمی‌شود،
بلکه روی سودهای قبلی نیز دوباره سود تعلق می‌گیرد.

━━━━━━━━━━━━━━

مثال:

سرمایه اولیه:
100 میلیون تومان

سود سالانه:
30٪

سال اول:

100 ➜ 130 میلیون

سال دوم:

130 ➜ 169 میلیون

سال سوم:

169 ➜ 219.7 میلیون

━━━━━━━━━━━━━━

📌 آلبرت اینشتین گفته است:

«بهره مرکب هشتمین عجایب دنیاست.»

━━━━━━━━━━━━━━

هرچه زمان بیشتر باشد،
قدرت بهره مرکب بیشتر می‌شود.
"""

    await update.message.reply_text(text)