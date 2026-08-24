from telegram import Update
from telegram.ext import ContextTypes

from keyboards.crypto_calculator_keyboard import (
    crypto_calculator_keyboard,
)

from .staking import (
    staking_intro,
)


async def crypto_calculators_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🧮 ماشین حساب‌های کریپتو\n\n"
        "یکی از ابزارهای زیر را انتخاب کنید:",
        reply_markup=crypto_calculator_keyboard,
    )


async def crypto_calculators_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    print(f"Clicked: {repr(text)}")

    # =========================
    # Staking
    # =========================

    if text == "⚡ سود استیکینگ":

        return await staking_intro(
            update,
            context,
        )


    # =========================
    # بازگشت
    # =========================

    elif text == "⬅️ بازگشت":

        from handlers.education.crypto_education.menu import (
            crypto_education_menu,
        )

        return await crypto_education_menu(
            update,
            context,
        )
