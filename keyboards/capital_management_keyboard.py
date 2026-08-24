from telegram import ReplyKeyboardMarkup

capital_management_keyboard = ReplyKeyboardMarkup(
    [
        ["💰 مدیریت سرمایه چیست؟"],
        ["📏 قانون ۱٪"],
        ["🧮 محاسبه اندازه پوزیشن"],
        ["⚖️ ریسک به ریوارد"],
        ["❌ اشتباهات رایج معامله‌گران"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)