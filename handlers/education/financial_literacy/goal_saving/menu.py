from telegram import Update
from telegram.ext import ContextTypes

from keyboards.goal_saving_keyboard import (
    goal_saving_keyboard,
)

from .intro import goal_saving_intro
from .calculator import goal_saving_calculator
from .example import goal_saving_example


async def goal_saving_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🎯 آموزش پس‌انداز هدف\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=goal_saving_keyboard,
    )


async def goal_saving_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 پس‌انداز هدف چیست؟":
        return await goal_saving_intro(update, context)

    elif text == "🧮 ماشین حساب پس‌انداز هدف":
        return await goal_saving_calculator(update, context)

    elif text == "📈 مثال واقعی پس‌انداز هدف":
        return await goal_saving_example(update, context)