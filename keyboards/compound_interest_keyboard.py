from telegram import ReplyKeyboardMarkup

compound_interest_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 بهره مرکب چیست؟"],
        ["🧮 ماشین حساب بهره مرکب"],
        ["📈 مثال واقعی"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)