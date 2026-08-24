from telegram import Update
from telegram.ext import ContextTypes

from keyboards.trend_keyboard import trend_keyboard

from .intro import trend_intro
from .calculator import trend_calculator
from .example import trend_example


async def trend_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📊 آموزش روند\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=trend_keyboard,
    )


async def trend_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 روند چیست؟":
        return await trend_intro(update, context)

    elif text == "🧮 ابزار تشخیص روند":
        return await trend_calculator(update, context)

    elif text == "📈 مثال واقعی روند":
        return await trend_example(update, context)