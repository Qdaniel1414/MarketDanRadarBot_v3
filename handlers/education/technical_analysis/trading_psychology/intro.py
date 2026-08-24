from telegram import Update
from telegram.ext import ContextTypes


async def trading_psychology_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🧠 روانشناسی معامله چیست؟\n\n"

        "روانشناسی معامله یعنی کنترل احساسات هنگام خرید و فروش.\n\n"

        "بیشتر معامله‌گران به خاطر نداشتن استراتژی ضرر نمی‌کنند؛\n"
        "بلکه به خاطر احساسات خود ضرر می‌کنند.\n\n"

        "مهم‌ترین احساسات:\n\n"

        "😱 ترس\n"
        "😈 طمع\n"
        "😡 انتقام از بازار\n"
        "😎 اعتماد به نفس کاذب\n"
        "😵 FOMO (ترس از جا ماندن)\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "معامله‌گر موفق اول ذهن خود را کنترل می‌کند، سپس بازار را."
    )

    await update.message.reply_text(text)