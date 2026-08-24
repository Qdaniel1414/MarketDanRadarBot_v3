from telegram import Update
from telegram.ext import ContextTypes

from keyboards.position_management_keyboard import (
    position_management_keyboard,
)

from .intro import position_management_intro
from .calculator import position_management_calculator
from .example import position_management_example
from .mistakes import position_management_mistakes


async def position_management_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⚖️ مدیریت پوزیشن\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=position_management_keyboard,
    )


async def position_management_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 مدیریت پوزیشن چیست؟":
        return await position_management_intro(update, context)

    elif text == "🧮 ماشین حساب مدیریت پوزیشن":
        return await position_management_calculator(update, context)

    elif text == "📈 مثال واقعی مدیریت پوزیشن":
        return await position_management_example(update, context)

    elif text == "💡 اشتباهات رایج مدیریت پوزیشن":
        return await position_management_mistakes(update, context)

    elif text == "⬅️ بازگشت":
        from handlers.education.technical_analysis.menu import technical_analysis_menu
        return await technical_analysis_menu(update, context)