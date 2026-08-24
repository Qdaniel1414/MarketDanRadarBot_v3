from telegram import ReplyKeyboardMarkup


technical_indices_keyboard = ReplyKeyboardMarkup(
    [
        [
            "📈 S&P 500",
            "💻 Nasdaq",
        ],
        [
            "🏦 Dow Jones",
            "📉 VIX",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="شاخص موردنظر را انتخاب کنید...",
)