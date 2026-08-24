from telegram import ReplyKeyboardMarkup


gold_calculator_keyboard = ReplyKeyboardMarkup(
    [
        [
            "🥇 طلای ۱۸ عیار",
            "🥇 طلای ۲۴ عیار",
        ],
        [
            "🏅 مثقال طلا",
            "🪙 طلای آب‌شده",
        ],
        [
            "🌍 انس جهانی",
        ],
        [
            "⬅️ بازگشت",
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
)