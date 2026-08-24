from telegram import ReplyKeyboardMarkup


market_keyboard = ReplyKeyboardMarkup(
    [
        [
            "💵 ارز",
            "🥇 طلا و سکه",
        ],
        [
            "₿ ارزهای دیجیتال",
            "🌍 بازارهای جهانی",
        ],
        [
            "🔄 بروزرسانی",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)