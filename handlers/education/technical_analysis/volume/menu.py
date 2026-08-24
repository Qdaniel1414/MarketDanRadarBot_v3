from telegram import Update
from telegram.ext import ContextTypes

from keyboards.volume_keyboard import volume_keyboard

from .intro import volume_intro
from .calculator import volume_calculator
from .example import volume_example


async def volume_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📦 آموزش حجم معاملات\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=volume_keyboard,
    )


async def volume_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 حجم معاملات چیست؟":
        return await volume_intro(update, context)

    elif text == "🧮 ماشین حساب حجم معاملات":
        return await volume_calculator(update, context)

    elif text == "📈 مثال واقعی حجم معاملات":
        return await volume_example(update, context)