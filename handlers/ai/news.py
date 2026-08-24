from telegram import Update
from telegram.ext import ContextTypes

from keyboards.news_keyboard import news_keyboard

from services.news_rss import (
    get_economic_news,
    get_iran_economic_news,
    get_global_economic_news,
    get_currency_news,
    get_gold_coin_news,
    get_crypto_news,
)


# ============================================================
# 📰 منوی اخبار
# ============================================================

async def news_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📰 تحلیل اخبار اقتصادی\n\n"
        "لطفاً یکی از بخش‌های اخبار را انتخاب کنید:",
        reply_markup=news_keyboard,
    )


# ============================================================
# 📰 اخبار مهم اقتصادی
# ============================================================

async def important_economic_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت آخرین اخبار اقتصادی..."
    )

    news = await get_economic_news(5)

    if not news:
        await update.message.reply_text(
            "❌ در حال حاضر دریافت اخبار امکان‌پذیر نیست."
        )
        return

    message = "📰 اخبار مهم اقتصادی\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(message)


# ============================================================
# 🇮🇷 اخبار اقتصاد ایران
# ============================================================

async def iran_economic_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت آخرین اخبار اقتصاد ایران..."
    )

    news = await get_iran_economic_news(5)

    if not news:
        await update.message.reply_text(
            "❌ در حال حاضر دریافت اخبار اقتصاد ایران امکان‌پذیر نیست."
        )
        return

    message = "🇮🇷 اخبار اقتصاد ایران\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(message)


# ============================================================
# 🌍 اخبار اقتصاد جهان
# ============================================================

async def global_economic_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت آخرین اخبار اقتصاد جهان..."
    )

    news = await get_global_economic_news(5)

    if not news:
        await update.message.reply_text(
            "❌ در حال حاضر دریافت اخبار اقتصاد جهان امکان‌پذیر نیست."
        )
        return

    message = "🌍 اخبار اقتصاد جهان\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(message)


# ============================================================
# 💵 اخبار دلار و ارز
# ============================================================

async def currency_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت آخرین اخبار دلار و ارز..."
    )

    news = await get_currency_news(5)

    if not news:
        await update.message.reply_text(
            "❌ در حال حاضر دریافت اخبار دلار و ارز امکان‌پذیر نیست."
        )
        return

    message = "💵 اخبار دلار و ارز\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(message)


# ============================================================
# 🥇 اخبار طلا و سکه
# ============================================================

async def gold_coin_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت آخرین اخبار طلا و سکه..."
    )

    news = await get_gold_coin_news(5)

    if not news:
        await update.message.reply_text(
            "❌ در حال حاضر دریافت اخبار طلا و سکه امکان‌پذیر نیست."
        )
        return

    message = "🥇 اخبار طلا و سکه\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(message)


# ============================================================
# ₿ اخبار کریپتو
# ============================================================

async def crypto_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت آخرین اخبار کریپتو..."
    )

    news = await get_crypto_news(5)

    if not news:
        await update.message.reply_text(
            "❌ در حال حاضر دریافت اخبار کریپتو امکان‌پذیر نیست."
        )
        return

    message = "₿ اخبار کریپتو\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(message)