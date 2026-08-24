from telegram import ReplyKeyboardMarkup


dollar_calculator_keyboard = ReplyKeyboardMarkup(
    [
        [
            "🇦🇪 درهم امارات",
            "💰 دلار بر اساس طلا",
        ],
        [
            "🇮🇷🇺🇸 دلار بر اساس تورم",
            "📈 دلار بر اساس نقدینگی",
        ],
        [
            "📊 مقایسه همه روش‌ها",
        ],
        [
            "⬅️ بازگشت",
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)