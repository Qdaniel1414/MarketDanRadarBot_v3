from telegram import ReplyKeyboardMarkup

bitcoin_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 بیت کوین چیست؟"],
        ["📈 مثال واقعی"],
        ["🧮 ماشین حساب بیت کوین"],
        ["🔙 آموزش ارزهای دیجیتال", "🏠 خانه"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)