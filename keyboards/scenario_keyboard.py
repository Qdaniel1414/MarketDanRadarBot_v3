from telegram import ReplyKeyboardMarkup


scenario_keyboard = ReplyKeyboardMarkup(
    [
        [
            "📈 سناریوی صعودی",
            "📉 سناریوی نزولی",
        ],
        [
            "⚖️ سناریوی خنثی",
            "💵 سناریوی دلار",
        ],
        [
            "🥇 سناریوی طلا",
            "₿ سناریوی بیت‌کوین",
        ],
        [
            "🔙 بازگشت به دستیار هوشمند",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="سناریو را انتخاب کنید...",
)