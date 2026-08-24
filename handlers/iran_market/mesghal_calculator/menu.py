from telegram import Update
from telegram.ext import ContextTypes

from keyboards.formulas.gold_18_keyboard import (
    cancel_keyboard,
)

from handlers.iran_market.formulas.mesghal_states import (
    WEIGHT,
)


async def mesghal_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(

        "🏵 محاسبه مثقال طلا\n\n"
        "وزن را وارد کنید (مثقال):",

        reply_markup=cancel_keyboard,

    )

    return WEIGHT