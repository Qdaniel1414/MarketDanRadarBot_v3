from telegram import ReplyKeyboardMarkup


glossary_keyboard = ReplyKeyboardMarkup(
    [
        ["🕯 کندل (Candlestick)"],
        ["⏰ تایم فریم"],
        ["📈 روند"],
        ["📊 نوسان"],
        ["💧 نقدشوندگی"],
        ["↩ پولبک"],
        ["🚀 بریک اوت"],
        ["❌ فیک بریک اوت"],
        ["⚡ مومنتوم"],
        ["💰 لیکوییدیتی گراب"],
        ["📖 واژه‌نامه کامل"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)