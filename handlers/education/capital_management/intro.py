from telegram import Update
from telegram.ext import ContextTypes


async def capital_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = """
💰 مدیریت سرمایه چیست؟

مدیریت سرمایه یعنی:

🔹 قبل از ورود به معامله مشخص کنید
چقدر از سرمایه‌تان را حاضر هستید ریسک کنید.

هدف مدیریت سرمایه:

✅ جلوگیری از نابودی حساب
✅ حفظ سرمایه
✅ رشد تدریجی سرمایه
✅ کنترل احساسات

یادت باشد:

هیچ معامله‌ای نباید باعث از بین رفتن بخش بزرگی از سرمایه‌ات شود.

📌 معامله‌گران حرفه‌ای
اول سرمایه را حفظ می‌کنند،
بعد به فکر سود هستند.
"""

    await update.message.reply_text(text)