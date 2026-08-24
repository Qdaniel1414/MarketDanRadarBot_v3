from telegram import KeyboardButton, ReplyKeyboardMarkup


international_market_keyboard = ReplyKeyboardMarkup(
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