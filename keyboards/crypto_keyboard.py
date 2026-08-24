from telegram import ReplyKeyboardMarkup


crypto_keyboard = ReplyKeyboardMarkup(
    [
        [
            "📄 صفحه ۱",
            "📄 صفحه ۲",
        ],
        [
            "🔍 جستجوی ارز",
            "🔄 بروزرسانی",
        ],
        [
            "⬅️ بازگشت",
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)