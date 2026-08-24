from telegram import Update
from telegram.ext import ContextTypes


async def volume_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🧮 ماشین حساب حجم معاملات\n\n"
        "🚧 این ابزار به‌زودی اضافه می‌شود.\n\n"
        "در نسخه حرفه‌ای ربات می‌توانید:\n"
        "• میانگین حجم\n"
        "• حجم نسبی (Relative Volume)\n"
        "• حجم مشکوک\n"
        "• حجم ورود پول هوشمند\n"
        "را محاسبه کنید."
    )


async def volume_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    return