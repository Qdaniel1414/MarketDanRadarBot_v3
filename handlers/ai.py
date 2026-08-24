from telegram import Update
from telegram.ext import ContextTypes

from keyboards.news_keyboard import news_keyboard
from services.news_rss import get_economic_news


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

    message = "📰 **اخبار مهم اقتصادی**\n\n"

    for index, item in enumerate(news, start=1):
        message += (
            f"{index}️⃣ {item['title']}\n"
            f"🔗 {item['link']}\n\n"
        )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )