from telegram import Update
from telegram.ext import ContextTypes


async def trend_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
📈 مثال واقعی روند

فرض کنید:

بیت‌کوین

100000

⬆️

105000

⬆️

112000

⬆️

118000

━━━━━━━━━━━━━━

هر سقف
بالاتر از سقف قبلی است.

هر کف
بالاتر از کف قبلی است.

✅ نتیجه:

روند صعودی است.

━━━━━━━━━━━━━━

در روند صعودی

اولویت معامله

خرید است.
"""
    )