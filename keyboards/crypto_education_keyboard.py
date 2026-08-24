from telegram import ReplyKeyboardMarkup

crypto_education_keyboard = ReplyKeyboardMarkup(
    [
        ["₿ بیت کوین چیست؟"],
        ["⛓ بلاکچین چیست؟"],
        ["🪙 آلت کوین چیست؟"],
        ["🏦 استیبل کوین چیست؟"],
        ["💵 تتر USDT"],
        ["🧠 اسمارت کانترکت"],
        ["💳 دیفای DeFi"],
        ["🎨 NFT"],
        ["⚡ ماینینگ"],
        ["🧾 واژه نامه کریپتو"],

        # 👇 این خط را تغییر بده
        ["🪙 ماشین حساب کریپتو"],

        [ "🏠 خانه"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)