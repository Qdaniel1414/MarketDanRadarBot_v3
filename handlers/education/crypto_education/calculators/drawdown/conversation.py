from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from .states import (
    PEAK,
    CURRENT,
)


# =====================================
# شروع
# =====================================

async def drawdown_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        """
📉 ماشین حساب افت سرمایه Drawdown

مرحله ۱ از ۲

🔝 بالاترین قیمت یا سقف سرمایه را وارد کنید:

مثال:

70000
"""
    )

    return PEAK


# =====================================
# مرحله اول
# =====================================

async def drawdown_peak(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        peak = float(
            update.message.text.replace(",", "")
        )

        if peak <= 0:

            await update.message.reply_text(
                "❌ مقدار سقف باید بیشتر از صفر باشد."
            )

            return PEAK

        context.user_data["peak"] = peak

        await update.message.reply_text(
            """
مرحله ۲ از ۲

📍 قیمت یا مقدار فعلی را وارد کنید:

مثال:

50000
"""
        )

        return CURRENT

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return PEAK


# =====================================
# مرحله دوم
# =====================================

async def drawdown_current(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        current = float(
            update.message.text.replace(",", "")
        )

        if current < 0:

            await update.message.reply_text(
                "❌ مقدار فعلی نمی‌تواند منفی باشد."
            )

            return CURRENT

        peak = context.user_data["peak"]

        drawdown = (
            (peak - current)
            / peak
        ) * 100

        recovery = (
            (peak - current)
            / current
        ) * 100 if current != 0 else 0

        await update.message.reply_text(
f"""
📉 نتیجه محاسبه Drawdown

━━━━━━━━━━━━

🔝 سقف قبلی:
{peak:,.2f}

📍 مقدار فعلی:
{current:,.2f}

━━━━━━━━━━━━

📉 افت سرمایه:

{drawdown:.2f}%

📈 رشد لازم برای بازگشت:

{recovery:.2f}%

━━━━━━━━━━━━

💡 نکته

افت 50٪

نیازمند رشد 100٪ برای بازگشت است.
"""
        )

        context.user_data.clear()

        return ConversationHandler.END

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return CURRENT


# =====================================
# Handler
# =====================================

drawdown_handler = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(
                r"^📉 محاسبه افت سرمایه Drawdown$"
            ),
            drawdown_intro,
        )
    ],

    states={

        PEAK: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                drawdown_peak,
            )
        ],

        CURRENT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                drawdown_current,
            )
        ],

    },

    fallbacks=[],

)