from telegram import ReplyKeyboardMarkup

position_management_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 مدیریت پوزیشن چیست؟"],
        ["🧮 ماشین حساب مدیریت پوزیشن"],
        ["📈 مثال واقعی مدیریت پوزیشن"],
        ["💡 اشتباهات رایج مدیریت پوزیشن"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)