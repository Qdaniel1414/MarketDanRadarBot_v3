from telegram import Update
from telegram.ext import ContextTypes

from keyboards.compound_interest_keyboard import (
    compound_interest_keyboard,
)

from handlers.education.financial_literacy.compound_interest.calculator import (
    compound_interest_handler,
)

async def compound_interest(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "💹 آموزش بهره مرکب\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=compound_interest_keyboard,
    )