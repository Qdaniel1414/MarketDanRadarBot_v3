from telegram import Update
from telegram.ext import ContextTypes

from keyboards.formulas.gold_formula_keyboard import (
    gold_formula_keyboard,
)


async def gold_formula(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(

        "🌕 فرمول محاسبه طلا\n\n"
        "لطفاً نوع محاسبه را انتخاب کنید:",

        reply_markup=gold_formula_keyboard,

    )