from telegram import Update
from telegram.ext import ContextTypes

from keyboards.support_resistance_keyboard import (
    support_resistance_keyboard,
)

from .intro import support_resistance_intro
from .calculator import support_resistance_calculator
from .example import support_resistance_example


async def support_resistance_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🧱 آموزش حمایت و مقاومت\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=support_resistance_keyboard,
    )


async def support_resistance_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 حمایت و مقاومت چیست؟":
        return await support_resistance_intro(update, context)

    elif text == "🧮 ماشین حساب حمایت و مقاومت":
        return await support_resistance_calculator(update, context)

    elif text == "📈 مثال واقعی":
        return await support_resistance_example(update, context)