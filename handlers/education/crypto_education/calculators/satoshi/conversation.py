from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from .states import (
    SATOSHI,
    MODE,
)


# ==========================================
# شروع
# ==========================================

async def satoshi_converter_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        """
₿ ماشین حساب ساتوشی

مرحله ۱ از ۲

یکی از گزینه‌های زیر را انتخاب کنید:

1️⃣ BTC ➜ Satoshi

2️⃣ Satoshi ➜ BTC

فقط عدد 1 یا 2 را وارد کنید.
"""
    )

    return MODE


# ==========================================
# انتخاب حالت
# ==========================================

async def satoshi_mode(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = update.message.text.strip()

    if text not in ("1", "2"):

        await update.message.reply_text(
            "❌ فقط عدد 1 یا 2 را وارد کنید."
        )

        return MODE

    context.user_data["mode"] = int(text)

    if text == "1":

        await update.message.reply_text(
            """
مرحله ۲ از ۲

🪙 مقدار BTC را وارد کنید.

مثال:

0.005
"""
        )

    else:

        await update.message.reply_text(
            """
مرحله ۲ از ۲

💰 مقدار ساتوشی را وارد کنید.

مثال:

500000
"""
        )

    return SATOSHI


# ==========================================
# محاسبه
# ==========================================

async def satoshi_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        value = float(
            update.message.text.replace(",", "")
        )

        mode = context.user_data["mode"]

        if mode == 1:

            satoshi = value * 100000000

            await update.message.reply_text(
f"""
📊 نتیجه تبدیل

━━━━━━━━━━━━

🪙 مقدار BTC:

{value:.8f}

━━━━━━━━━━━━

💰 ساتوشی:

{satoshi:,.0f}

━━━━━━━━━━━━

📌 هر BTC

100,000,000 Satoshi
"""
            )

        else:

            btc = value / 100000000

            await update.message.reply_text(
f"""
📊 نتیجه تبدیل

━━━━━━━━━━━━

💰 مقدار ساتوشی:

{value:,.0f}

━━━━━━━━━━━━

🪙 BTC:

{btc:.8f}

━━━━━━━━━━━━

📌 هر BTC

100,000,000 Satoshi
"""
            )

        context.user_data.clear()

        return ConversationHandler.END

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return SATOSHI


# ==========================================
# Handler
# ==========================================

satoshi_handler = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(r"^₿ ساتوشی ↔ بیت کوین$"),
            satoshi_converter_intro,
        )
    ],

    states={

        MODE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                satoshi_mode,
            )
        ],

        SATOSHI: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                satoshi_input,
            )
        ],

    },

    fallbacks=[],

)