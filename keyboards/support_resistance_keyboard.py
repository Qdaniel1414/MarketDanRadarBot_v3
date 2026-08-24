from telegram import ReplyKeyboardMarkup

support_resistance_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 حمایت و مقاومت چیست؟"],
        ["🧮 ماشین حساب حمایت و مقاومت"],
        ["📈 مثال واقعی"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)