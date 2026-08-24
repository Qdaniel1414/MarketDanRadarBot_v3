from telegram import Update
from telegram.ext import ContextTypes

from keyboards.diversification_keyboard import (
    diversification_keyboard,
)

from .intro import diversification_intro
from .calculator import diversification_calculator
from .example import diversification_example


async def diversification_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🧺 آموزش تنوع‌بخشی سرمایه\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=diversification_keyboard,
    )


async def diversification_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 تنوع‌بخشی سرمایه چیست؟":
        return await diversification_intro(update, context)

    elif text == "🧮 ماشین حساب تنوع‌بخشی":
        return await diversification_calculator(update, context)

    elif text == "📈 مثال واقعی تنوع‌بخشی":
        return await diversification_example(update, context)