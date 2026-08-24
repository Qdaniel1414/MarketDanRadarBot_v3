from telegram import ReplyKeyboardMarkup


precious_metals_keyboard = ReplyKeyboardMarkup(
    [
        [
            "🏛 LBMA",
            "🌐 World Gold Council",
        ],
        [
            "📊 Kitco",
            "🏦 CME Group",
        ],
        [
            "🔙 بازگشت",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="سایت موردنظر را انتخاب کنید...",
)