from telegram import ReplyKeyboardMarkup


crypto_calculator_keyboard = ReplyKeyboardMarkup(
    [
        ["🪙 میانگین خرید DCA"],
        ["⚡ سود استیکینگ"],
        ["📈 سود و زیان کریپتو"],
        ["📉 محاسبه افت سرمایه Drawdown"],
        ["₿ ساتوشی ↔ بیت کوین"],
        ["💵 تبدیل BTC ↔ دلار / تومان"],
        ["💎 تبدیل ETH ↔ دلار / تومان"],
        ["🏠 خانه"],
    ],
    resize_keyboard=True
)