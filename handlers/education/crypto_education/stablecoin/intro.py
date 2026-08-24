from telegram import Update
from telegram.ext import ContextTypes


async def stablecoin_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🏦 استیبل‌کوین چیست؟\n\n"

        "استیبل‌کوین (Stablecoin) ارز دیجیتالی است که قیمت آن به یک دارایی ثابت متصل است.\n\n"

        "معمولاً به:\n"
        "💵 دلار آمریکا\n"
        "🥇 طلا\n"
        "💶 یورو\n\n"

        "معروف‌ترین استیبل‌کوین‌ها:\n\n"

        "💵 USDT (Tether)\n"
        "💵 USDC\n"
        "💵 DAI\n"
        "💵 FDUSD\n\n"

        "مزایا:\n"
        "✅ نوسان بسیار کم\n"
        "✅ انتقال سریع پول\n"
        "✅ مناسب برای معامله‌گران\n"
        "✅ حفظ ارزش سرمایه در بازار کریپتو\n\n"

        "ریسک‌ها:\n"
        "❌ ریسک شرکت صادرکننده\n"
        "❌ ریسک قوانین دولتی\n"
        "❌ امکان از دست دادن پشتوانه در برخی پروژه‌ها\n\n"

        "🎯 استیبل‌کوین‌ها پلی بین دنیای ارزهای سنتی و ارزهای دیجیتال هستند."
    )

    await update.message.reply_text(text)