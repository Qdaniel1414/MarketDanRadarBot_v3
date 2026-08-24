from telegram import Update
from telegram.ext import ContextTypes


async def volume_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "📦 حجم معاملات چیست؟\n\n"
        "حجم معاملات (Volume) تعداد دارایی معامله‌شده در یک بازه زمانی را نشان می‌دهد.\n\n"
        "اگر قیمت همراه با حجم بالا حرکت کند، آن حرکت معمولاً اعتبار بیشتری دارد.\n\n"
        "اگر قیمت رشد کند اما حجم پایین باشد، احتمال ضعف روند وجود دارد.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 اولین مهارت هر معامله‌گر:\n"
        "بررسی همزمان قیمت و حجم معاملات است."
    )

    await update.message.reply_text(text)