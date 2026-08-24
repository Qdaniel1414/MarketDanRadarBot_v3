from telegram import ReplyKeyboardMarkup

financial_literacy_keyboard = ReplyKeyboardMarkup(
    [
        ["🧮 بهره مرکب"],
        ["⏳ ارزش زمانی پول"],
        ["💵 قدرت خرید"],
        ["🎯 پس‌انداز هدف"],
        ["📈 ROI"],
        ["📊 بازده واقعی"],
        ["📋 بودجه 50/30/20"],
        ["🧺 تنوع‌بخشی سرمایه"],
        ["💼 درآمد فعال و غیرفعال"],
        ["⬅️ بازگشت", "🏠 خانه"],
    ],
    resize_keyboard=True,
)