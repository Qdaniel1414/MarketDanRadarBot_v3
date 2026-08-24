from telegram import Update
from telegram.ext import ContextTypes

from keyboards.bitcoin_keyboard import bitcoin_keyboard

from handlers.education.crypto_education.bitcoin.intro import (
    bitcoin_intro,
)

from handlers.education.crypto_education.bitcoin.example import (
    bitcoin_example,
)

from handlers.education.crypto_education.bitcoin.calculator import (
    bitcoin_calculator,
)


async def bitcoin_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "₿ آموزش بیت کوین\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=bitcoin_keyboard,
    )


async def bitcoin_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 بیت کوین چیست؟":
        return await bitcoin_intro(update, context)

    elif text == "📈 مثال واقعی":
        return await bitcoin_example(update, context)

    elif text == "🧮 ماشین حساب بیت کوین":
        return await bitcoin_calculator(update, context)

    elif text == "🔙 آموزش ارزهای دیجیتال":
        from handlers.education.crypto_education.menu import (
            crypto_education_menu,
        )

        return await crypto_education_menu(update, context)