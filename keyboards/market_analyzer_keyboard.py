from telegram import ReplyKeyboardMarkup


market_analyzer_keyboard = ReplyKeyboardMarkup(
    [
        [
            "💵 تحلیل دلار و ارز",
            "🥇 تحلیل طلا و سکه",
        ],
        [
            "₿ تحلیل کریپتو",
            "📈 تحلیل بازارهای جهانی",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="نوع تحلیل بازار را انتخاب کنید...",
)