from telegram import ReplyKeyboardMarkup


market_lab_keyboard = ReplyKeyboardMarkup(
    [
        [
            "💵 اثر دلار روی طلا",
            "🥇 اثر اونس روی طلا",
        ],
        [
            "📊 تغییر درصدی قیمت",
            "⚖️ مقایسه دو سناریو",
        ],
        [
            "🔙 بازگشت به دستیار هوشمند",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="آزمایش بازار را انتخاب کنید...",
)