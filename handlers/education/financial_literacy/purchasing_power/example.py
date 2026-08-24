from telegram import Update
from telegram.ext import ContextTypes


async def purchasing_power_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = """
📈 مثال واقعی قدرت خرید

فرض کنید:

💰 امروز:
100 میلیون تومان دارید.

📈 تورم سالانه:
40٪

اگر این پول را 5 سال نگه دارید
و هیچ سودی نگیرید:

━━━━━━━━━━━━━━

قدرت خرید واقعی:

سال اول:
71.4 میلیون

سال دوم:
51 میلیون

سال سوم:
36.4 میلیون

سال چهارم:
26 میلیون

سال پنجم:
18.6 میلیون

━━━━━━━━━━━━━━

یعنی:

100 میلیون تومان شما
بعد از 5 سال

فقط معادل
18.6 میلیون تومان امروز ارزش خواهد داشت.

📌 نتیجه:

اگر سرمایه شما
کمتر از نرخ تورم رشد کند،

قدرت خریدتان هر سال کمتر می‌شود.
"""

    await update.message.reply_text(text)