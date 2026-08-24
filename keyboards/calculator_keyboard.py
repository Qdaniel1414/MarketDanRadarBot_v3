from telegram import ReplyKeyboardMarkup

calculator_keyboard = ReplyKeyboardMarkup(
    [
        [
            "🧮 درصد",
            "💰 سود و زیان",
        ],
        [
            "📈 سود مرکب",
            "📊 میانگین خرید",
        ],
        [
            "🎯 حد سود و ضرر",
            "⚖️ ریسک به ریوارد",
        ],
        [
            "🔀 تبدیل ارز",
            "⚪ تبدیل طلا",
        ],
        [
            "🏦 قسط و وام",
        ],
        [
            
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)