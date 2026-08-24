from telegram import Update
from telegram.ext import ContextTypes

user_states = {}


async def trend_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📊 ابزار تشخیص روند\n\n"
        "🚧 این ابزار به زودی اضافه می‌شود."
    )


async def trend_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    return