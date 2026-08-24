from telegram import Update
from telegram.ext import ContextTypes


async def trading_psychology_mistakes(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "💡 اشتباهات رایج روانشناسی معامله\n\n"

        "❌ انتقام از بازار\n\n"

        "❌ معامله بیش از حد (Over Trading)\n\n"

        "❌ ترس از جا ماندن (FOMO)\n\n"

        "❌ فروش از روی ترس\n\n"

        "❌ خرید از روی هیجان\n\n"

        "❌ اعتماد به نفس بیش از حد\n\n"

        "❌ نداشتن نظم معاملاتی\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "احساسات دشمن معامله‌گر هستند.\n"
        "همیشه طبق برنامه معامله کنید، نه احساس."
    )

    await update.message.reply_text(text)