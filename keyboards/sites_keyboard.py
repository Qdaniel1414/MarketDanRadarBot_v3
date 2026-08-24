from telegram import ReplyKeyboardMarkup


sites_keyboard = ReplyKeyboardMarkup(
    [
        [
            "📊 اقتصاد کلان",
            "🥇 طلا و فلزات گرانبها",
        ],
        [
            "💵 دلار و بازار ارز",
            "₿ سایت‌های ارزهای دیجیتال",
        ],
        [
            "🇮🇷 اقتصاد و بازار ایران",
            "📈 بورس و سهام",
        ],
        [
            "🌍 سایت‌های بازارهای جهانی",
            "🛠 ابزارهای مالی",
        ],
        [
            "🏠 خانه",
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="دسته موردنظر را انتخاب کنید...",
)