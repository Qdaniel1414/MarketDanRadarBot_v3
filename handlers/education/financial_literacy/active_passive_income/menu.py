from telegram import Update
from telegram.ext import ContextTypes

from keyboards.active_passive_income_keyboard import (
    active_passive_income_keyboard,
)

from .intro import active_passive_income_intro
from .calculator import active_passive_income_calculator
from .example import active_passive_income_example


async def active_passive_income_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "💼 آموزش درآمد فعال و غیرفعال\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=active_passive_income_keyboard,
    )


async def active_passive_income_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 درآمد فعال و غیرفعال چیست؟":
        return await active_passive_income_intro(update, context)

    elif text == "🧮 ماشین حساب درآمد":
        return await active_passive_income_calculator(update, context)

    elif text == "📈 مثال واقعی درآمد":
        return await active_passive_income_example(update, context)