from telegram import InlineKeyboardButton, InlineKeyboardMarkup


macro_sites_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🌐 FRED",
                url="https://fred.stlouisfed.org/"
            ),
            InlineKeyboardButton(
                "🌍 IMF",
                url="https://www.imf.org/en/Data"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 World Bank",
                url="https://data.worldbank.org/"
            ),
            InlineKeyboardButton(
                "📊 Trading Economics",
                url="https://tradingeconomics.com/"
            ),
        ],
    ]
)