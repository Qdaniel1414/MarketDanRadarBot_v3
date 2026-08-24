from telegram import ReplyKeyboardMarkup


technical_scanner_keyboard = ReplyKeyboardMarkup(
    [
        ["₿ Bitcoin", "Ξ Ethereum"],
        ["🥇 طلا", "💵 دلار"],
        ["📊 شاخص‌ها", "🏢 سهام آمریکا"],
        ["🏠 خانه"],
    ],
    resize_keyboard=True,
    input_field_placeholder="بازار موردنظر برای اسکن تکنیکال را انتخاب کنید...",
)