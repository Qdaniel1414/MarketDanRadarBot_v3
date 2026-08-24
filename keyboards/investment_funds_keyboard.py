from telegram import ReplyKeyboardMarkup


investment_funds_keyboard = ReplyKeyboardMarkup(
    [
        [
            "🏦 درآمد ثابت",
            "📈 سهامی",
        ],
        [
            "⚖️ مختلط",
            "🚀 اهرمی",
        ],
        [
            "📊 شاخصی",
            "🏠 املاک و مستغلات",
        ],
        [
            "🥇 صندوق‌های طلا",
        ],
        [
            "⬅️ بازگشت",
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)