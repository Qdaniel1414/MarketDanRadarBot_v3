from telegram import Update
from telegram.ext import ContextTypes

from keyboards.budget_50_30_20_keyboard import (
    budget_50_30_20_keyboard,
)

from .intro import budget_50_30_20_intro
from .calculator import budget_50_30_20_calculator
from .example import budget_50_30_20_example


async def budget_50_30_20_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "📋 قانون بودجه 50/30/20",
        reply_markup=budget_50_30_20_keyboard,
    )


async def budget_50_30_20_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = update.message.text

    if text == "📘 قانون 50/30/20 چیست؟":
        return await budget_50_30_20_intro(update, context)

    elif text == "🧮 ماشین حساب بودجه":
        return await budget_50_30_20_calculator(update, context)

    elif text == "📈 مثال واقعی بودجه":
        return await budget_50_30_20_example(update, context)