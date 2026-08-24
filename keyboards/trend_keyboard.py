from telegram import ReplyKeyboardMarkup

trend_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 روند چیست؟"],
        ["🧮 ابزار تشخیص روند"],
        ["📈 مثال واقعی روند"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)