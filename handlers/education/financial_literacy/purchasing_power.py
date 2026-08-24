from telegram import Update
from telegram.ext import ContextTypes

from keyboards.purchasing_power_keyboard import (
    purchasing_power_keyboard,
)

from handlers.education.financial_literacy.purchasing_power.intro import (
    purchasing_power_intro,
)

from handlers.education.financial_literacy.purchasing_power.calculator import (
    purchasing_power_calculator,
)

from handlers.education.financial_literacy.purchasing_power.example import (
    purchasing_power_example,
)


async def purchasing_power(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "💵 آموزش قدرت خرید\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=purchasing_power_keyboard,
    )


async def purchasing_power_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 قدرت خرید چیست؟":
        return await purchasing_power_intro(update, context)

    elif text == "🧮 ماشین حساب قدرت خرید":
        return await purchasing_power_calculator(update, context)

    elif text == "📈 مثال واقعی قدرت خرید":
        return await purchasing_power_example(update, context)