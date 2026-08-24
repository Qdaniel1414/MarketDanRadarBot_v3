from telegram import Update
from telegram.ext import ContextTypes

from keyboards.time_value_keyboard import (
    time_value_keyboard,
)

from .intro import (
    time_value_intro,
)

from .example import (
    time_value_example,
)

from .calculator import (
    time_value_calculator,
)


async def time_value_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ آموزش ارزش زمانی پول\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=time_value_keyboard,
    )


async def time_value_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 ارزش زمانی پول چیست؟":
        return await time_value_intro(update, context)

    elif text == "📈 مثال واقعی ارزش زمانی پول":
        return await time_value_example(update, context)

    elif text == "🧮 ماشین حساب ارزش زمانی پول":
        return await time_value_calculator(update, context)

    return