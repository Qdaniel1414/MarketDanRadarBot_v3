from telegram import Update
from telegram.ext import ContextTypes


async def glossary_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "📚 واژه‌نامه کریپتو\n\n"

        "چند اصطلاح مهم در بازار ارزهای دیجیتال:\n\n"

        "🟢 Bull Market\n"
        "بازار صعودی\n\n"

        "🔴 Bear Market\n"
        "بازار نزولی\n\n"

        "💎 HODL\n"
        "نگهداری بلندمدت دارایی\n\n"

        "🚀 Pump\n"
        "رشد سریع قیمت\n\n"

        "📉 Dump\n"
        "سقوط شدید قیمت\n\n"

        "🐋 Whale\n"
        "نهنگ؛ سرمایه‌گذار بزرگ بازار\n\n"

        "💧 Liquidity\n"
        "نقدشوندگی\n\n"

        "🏦 Market Cap\n"
        "ارزش کل بازار یک ارز\n\n"

        "⚖️ Volatility\n"
        "نوسان قیمت\n\n"

        "💼 Portfolio\n"
        "سبد سرمایه‌گذاری\n\n"

        "🔑 Private Key\n"
        "کلید خصوصی\n\n"

        "📬 Public Key\n"
        "کلید عمومی\n\n"

        "💰 Wallet\n"
        "کیف پول ارز دیجیتال\n\n"

        "⛽ Gas Fee\n"
        "کارمزد شبکه\n\n"

        "🎯 این واژه‌ها پایه‌ی یادگیری بازار کریپتو هستند."
    )

    await update.message.reply_text(text)