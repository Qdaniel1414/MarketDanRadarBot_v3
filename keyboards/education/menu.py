from telegram import ReplyKeyboardMarkup

education_keyboard = ReplyKeyboardMarkup(
    [
        ["💰 مدیریت سرمایه"],
        ["📊 تحلیل تکنیکال"],
        ["₿ آموزش ارزهای دیجیتال"],
        ["🌍 اقتصاد کلان"],
        ["🏦 سواد مالی"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)