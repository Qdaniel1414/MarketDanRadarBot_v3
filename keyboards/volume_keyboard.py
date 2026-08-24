from telegram import ReplyKeyboardMarkup

volume_keyboard = ReplyKeyboardMarkup(
    [
        ["📘 حجم معاملات چیست؟"],
        ["🧮 ماشین حساب حجم معاملات"],
        ["📈 مثال واقعی حجم معاملات"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)