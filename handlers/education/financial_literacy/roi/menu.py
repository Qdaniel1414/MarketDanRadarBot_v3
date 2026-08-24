from telegram import Update
from telegram.ext import ContextTypes

from keyboards.roi_keyboard import roi_keyboard

from .intro import roi_intro
from .calculator import roi_calculator
from .example import roi_example


async def roi_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "📈 آموزش ROI\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=roi_keyboard,
    )


async def roi_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 ROI چیست؟":
        return await roi_intro(update, context)

    elif text == "🧮 ماشین حساب ROI":
        return await roi_calculator(update, context)

    elif text == "📈 مثال واقعی ROI":
        return await roi_example(update, context)