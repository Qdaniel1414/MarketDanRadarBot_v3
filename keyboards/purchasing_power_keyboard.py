from telegram import ReplyKeyboardMarkup

purchasing_power_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 قدرت خرید چیست؟"],
        ["🧮 ماشین حساب قدرت خرید"],
        ["📈 مثال واقعی قدرت خرید"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)