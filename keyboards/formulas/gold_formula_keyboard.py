from telegram import ReplyKeyboardMarkup


gold_formula_keyboard = ReplyKeyboardMarkup(

    [

        [

            "🥇 طلای ۱۸ عیار",
            "🥈 طلای ۲۴ عیار",

        ],

        [

            "🌙 طلای آب‌شده",

        ],

        [

            "🏠 خانه",

        ],

    ],

    resize_keyboard=True,

    input_field_placeholder="نوع محاسبه طلا را انتخاب کنید...",

)