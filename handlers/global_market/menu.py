from telegram import Update
from telegram.ext import ContextTypes

from telegram import KeyboardButton, ReplyKeyboardMarkup


global_market_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("📅 تقویم اقتصادی"),
        ],
        [
            KeyboardButton("📰 اخبار اقتصادی"),
        ],
        [
            KeyboardButton("🌐 معرفی سایت‌های کاربردی"),
        ],
        [
            KeyboardButton("🏠 خانه"),
        ],
    ],
    resize_keyboard=True,
)


async def global_market_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🌍 بازارهای بین‌المللی\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=global_market_keyboard,
    )