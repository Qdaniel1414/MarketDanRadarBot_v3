from telegram import ReplyKeyboardMarkup


us_stocks_keyboard = ReplyKeyboardMarkup(
    [
        [
            "🟢 Nvidia",
            "🍎 Apple",
        ],
        [
            "🪟 Microsoft",
            "🔎 Google",
        ],
        [
            "📦 Amazon",
            "🚗 Tesla",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="سهم موردنظر برای اسکن تکنیکال را انتخاب کنید...",
)