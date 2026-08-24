from telegram import Update
from telegram.ext import ContextTypes

from .parser import (
    get_latest_news,
    get_today_calendar,
)


# ==========================
# اخبار اقتصادی
# ==========================

async def economic_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    news = get_latest_news(5)

    if not news:
        await update.message.reply_text(
            "❌ دریافت اخبار امکان‌پذیر نبود."
        )
        return

    text = "📰 آخرین اخبار اقتصادی\n\n"

    for i, item in enumerate(news, start=1):

        text += (
            f"{i}. {item['title']}\n"
            f"{item['published']}\n"
            f"{item['link']}\n\n"
        )

    await update.message.reply_text(text)


# ==========================
# تقویم اقتصادی
# ==========================

async def economic_calendar(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    events = get_today_calendar()

    if not events:

        await update.message.reply_text(
            "📅 امروز رویداد مهمی وجود ندارد."
        )
        return

    text = "📅 تقویم اقتصادی امروز\n\n"

    for event in events:

        text += (
            f"🕒 ساعت: {event.get('time','-')}\n"
            f"🌍 کشور: {event.get('country','-')} ({event.get('currency','-')})\n"
            f"📌 رویداد: {event.get('title','-')}\n"
            f"⭐ اهمیت: {event.get('impact','-')}\n"
            f"🎯 پیش‌بینی: {event.get('forecast','-') or '-'}\n"
            f"📊 قبلی: {event.get('previous','-') or '-'}\n"
            f"✅ واقعی: {event.get('actual','-') or '-'}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

    await update.message.reply_text(text)