from telegram import ReplyKeyboardMarkup


news_keyboard = ReplyKeyboardMarkup(
    [
        [
            "📰 اخبار مهم اقتصادی",
            "🇮🇷 اخبار اقتصاد ایران",
        ],
        [
            "🌍 اخبار اقتصاد جهان",
            "💵 اخبار دلار و ارز",
        ],
        [
            "🥇 اخبار طلا و سکه",
            "₿ اخبار کریپتو",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="نوع اخبار را انتخاب کنید...",
)