from telegram import ReplyKeyboardMarkup

goal_saving_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 پس‌انداز هدف چیست؟"],
        ["🧮 ماشین حساب پس‌انداز هدف"],
        ["📈 مثال واقعی پس‌انداز هدف"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)