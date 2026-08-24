from telegram import ReplyKeyboardMarkup

currency_keyboard = ReplyKeyboardMarkup(
    [
        [
            "دلار",
            "یورو",
        ],
        [
            "درهم",
            "تتر",
        ],
        [
            "⬅️ بازگشت",
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)