from telegram import ReplyKeyboardMarkup

technical_analysis_keyboard = ReplyKeyboardMarkup(
    [
        ["📊 روند", "🧱 حمایت و مقاومت"],
        ["📦 حجم معاملات", "⚖️ مدیریت پوزیشن"],
        ["🧠 روانشناسی معامله"],
        ["📚 اصطلاحات تحلیل تکنیکال"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)