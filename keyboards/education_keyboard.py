from telegram import ReplyKeyboardMarkup

education_keyboard = ReplyKeyboardMarkup(
    [
        ["💰 آموزش سواد مالی"],
        ["📈 آموزش تحلیل تکنیکال"],
        ["🪙 آموزش ارزهای دیجیتال"],
        ["🌍 آموزش اقتصاد کلان"],
        ["💼 آموزش مدیریت سرمایه"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)