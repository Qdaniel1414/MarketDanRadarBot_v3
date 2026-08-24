from telegram import KeyboardButton, ReplyKeyboardMarkup


register_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                text="📱 اشتراک‌گذاری شماره موبایل",
                request_contact=True,
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)