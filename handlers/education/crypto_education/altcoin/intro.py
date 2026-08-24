from telegram import Update
from telegram.ext import ContextTypes


async def altcoin_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🪙 آلت‌کوین چیست؟\n\n"

        "آلت‌کوین (Altcoin) به تمام ارزهای دیجیتال به‌جز بیت‌کوین گفته می‌شود.\n\n"

        "Alt = Alternative\n"
        "Coin = ارز\n\n"

        "یعنی:\n"
        "«ارز جایگزین بیت‌کوین»\n\n"

        "هدف آلت‌کوین‌ها:\n\n"

        "✅ سرعت بیشتر\n"
        "✅ کارمزد کمتر\n"
        "✅ امکانات جدید\n"
        "✅ قرارداد هوشمند\n"
        "✅ دیفای\n"
        "✅ NFT\n\n"

        "نمونه آلت‌کوین‌ها:\n\n"

        "🔹 Ethereum\n"
        "🔹 BNB\n"
        "🔹 Solana\n"
        "🔹 Cardano\n"
        "🔹 Avalanche\n"
        "🔹 Polkadot\n"
        "🔹 XRP\n\n"

        "مزایا:\n"
        "✔ رشد زیاد در بازار صعودی\n"
        "✔ فناوری‌های جدید\n\n"

        "ریسک‌ها:\n"
        "❌ نوسان شدیدتر از بیت‌کوین\n"
        "❌ احتمال شکست پروژه\n"
        "❌ نقدشوندگی کمتر در برخی پروژه‌ها\n\n"

        "🎯 همه ارزهای دیجیتال غیر از بیت‌کوین را آلت‌کوین می‌نامند."
    )

    await update.message.reply_text(text)
    from telegram import Update
from telegram.ext import ContextTypes


async def altcoin_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🪙 آلت‌کوین چیست؟\n\n"

        "آلت‌کوین به تمام ارزهای دیجیتال به‌جز بیت‌کوین گفته می‌شود.\n\n"

        "بعد از موفقیت بیت‌کوین، هزاران پروژه جدید ایجاد شدند که هرکدام هدف خاصی دارند.\n\n"

        "نمونه‌های معروف:\n\n"

        "🟣 Ethereum (ETH)\n"
        "🔵 Solana (SOL)\n"
        "🟡 BNB\n"
        "🟢 Cardano (ADA)\n"
        "⚪ Avalanche (AVAX)\n\n"

        "مزایا:\n"
        "✅ نوآوری بیشتر\n"
        "✅ سرعت بالاتر برخی شبکه‌ها\n"
        "✅ امکانات متنوع\n\n"

        "ریسک‌ها:\n"
        "❌ نوسان شدید\n"
        "❌ احتمال شکست پروژه\n"
        "❌ نقدشوندگی کمتر نسبت به بیت‌کوین\n\n"

        "💡 همه آلت‌کوین‌ها ارزش سرمایه‌گذاری ندارند و باید قبل از خرید، پروژه بررسی شود."
    )

    await update.message.reply_text(text)