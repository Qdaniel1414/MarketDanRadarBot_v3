from telegram import ReplyKeyboardMarkup

ai_keyboard = ReplyKeyboardMarkup(
    [
        [
            "📊 تحلیلگر هوشمند بازار",
            "📰 تحلیل اخبار اقتصادی",
        ],
        [
            "📉 اسکنر تکنیکال بازار",
            "🧮 محاسبه‌گر هوشمند",
        ],
        [
            "🔬 آزمایشگاه بازار",
            "🧠 تحلیل سناریو",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="دستیار هوشمند را انتخاب کنید...",
)