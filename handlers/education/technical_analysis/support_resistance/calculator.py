from telegram import Update
from telegram.ext import ContextTypes


async def support_resistance_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "🧮 ماشین حساب حمایت و مقاومت\n\n"
        "🚧 به زودی اضافه می‌شود."
    )


async def support_resistance_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    return