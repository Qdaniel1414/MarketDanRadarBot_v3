from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from .dca_states import CAPITAL, COUNT, INTERVAL


async def dca_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        """
🪙 ماشین حساب DCA

💰 مرحله ۱ از ۳

مقدار سرمایه کل را وارد کنید:

مثال:
50000000
"""
    )

    return CAPITAL



async def dca_capital(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:
        capital = float(
            update.message.text.replace(",", "")
        )

        context.user_data["dca_capital"] = capital

        await update.message.reply_text(
            """
📈 مرحله ۲ از ۳

تعداد دفعات خرید را وارد کنید:

مثال:
10
"""
        )

        return COUNT


    except:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return CAPITAL



async def dca_count(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        count = int(update.message.text)

        if count <= 0:
            raise ValueError


        context.user_data["dca_count"] = count


        await update.message.reply_text(
            """
⏳ مرحله ۳ از ۳

بازه زمانی خرید را وارد کنید:

مثال:
ماهانه
"""
        )

        return INTERVAL


    except:

        await update.message.reply_text(
            "❌ عدد معتبر وارد کنید."
        )

        return COUNT



async def dca_interval(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    capital = context.user_data["dca_capital"]
    count = context.user_data["dca_count"]


    each = capital / count


    await update.message.reply_text(
f"""
📊 نتیجه DCA

━━━━━━━━━━━━

💰 سرمایه:
{capital:,.0f} تومان

📆 تعداد خرید:
{count} مرحله

💵 مبلغ هر خرید:
{each:,.0f} تومان

━━━━━━━━━━━━

✅ کاهش ریسک ورود
✅ حذف تصمیم احساسی
✅ مناسب سرمایه‌گذاری بلندمدت
"""
    )


    return ConversationHandler.END