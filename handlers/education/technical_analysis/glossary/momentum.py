from telegram import Update
from telegram.ext import ContextTypes


async def momentum_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "⚡ مومنتوم (Momentum)\n\n"

        "مومنتوم یعنی قدرت و سرعت حرکت قیمت.\n\n"

        "ممکن است قیمت صعودی باشد، اما قدرت حرکت آن کم شده باشد.\n\n"

        "یا قیمت نزولی باشد، اما فروشندگان قدرت زیادی داشته باشند.\n\n"

        "📈 مومنتوم قوی:\n"
        "✔ کندل‌های بزرگ\n"
        "✔ حجم معاملات بالا\n"
        "✔ حرکت سریع قیمت\n\n"

        "📉 مومنتوم ضعیف:\n"
        "✔ کندل‌های کوچک\n"
        "✔ کاهش حجم معاملات\n"
        "✔ حرکت کند قیمت\n\n"

        "ابزارهای بررسی مومنتوم:\n\n"

        "📊 RSI\n"
        "📊 MACD\n"
        "📊 Momentum Indicator\n"
        "📊 ROC\n\n"

        "❌ اشتباه رایج:\n"
        "معامله در روندی که مومنتوم آن از بین رفته است.\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "جهت روند مهم است، اما قدرت روند مهم‌تر است."
    )

    await update.message.reply_text(text)