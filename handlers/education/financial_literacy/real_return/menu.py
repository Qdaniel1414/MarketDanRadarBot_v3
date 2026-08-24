from telegram import Update
from telegram.ext import ContextTypes

from keyboards.real_return_keyboard import (
    real_return_keyboard,
)

from .intro import real_return_intro
from .calculator import real_return_calculator
from .example import real_return_example


async def real_return_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "📊 آموزش بازده واقعی\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=real_return_keyboard,
    )


async def real_return_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 بازده واقعی چیست؟":
        return await real_return_intro(update, context)

    elif text == "🧮 ماشین حساب بازده واقعی":
        return await real_return_calculator(update, context)

    elif text == "📈 مثال واقعی بازده واقعی":
        return await real_return_example(update, context)