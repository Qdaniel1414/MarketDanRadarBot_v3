from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from keyboards.sites_keyboard import sites_keyboard
from keyboards.macro_sites_keyboard import macro_sites_keyboard


# ============================================================
# 🌐 منوی اصلی سایت‌های کاربردی
# ============================================================

async def sites_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🌐 معرفی سایت‌های کاربردی\n\n"
        "سایت‌های کاربردی حوزه اقتصاد، طلا، دلار، "
        "ارز دیجیتال و بازارهای مالی را انتخاب کنید:",
        reply_markup=sites_keyboard,
    )


# ============================================================
# 📊 اقتصاد کلان
# ============================================================

async def macro_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📊 اقتصاد کلان\n\n"
        "سایت‌های کاربردی برای بررسی داده‌ها و "
        "شاخص‌های اقتصاد کلان:",
        reply_markup=macro_sites_keyboard,
    )


# ============================================================
# 🥇 طلا و فلزات گرانبها
# ============================================================

async def gold_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    gold_sites_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏛 LBMA",
                    url="https://www.lbma.org.uk/",
                ),
                InlineKeyboardButton(
                    "🌐 World Gold Council",
                    url="https://www.gold.org/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📊 Trading Economics",
                    url="https://tradingeconomics.com/commodity/gold",
                ),
                InlineKeyboardButton(
                    "🏦 CME Group",
                    url="https://www.cmegroup.com/markets/metals/precious.html",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "🥇 طلا و فلزات گرانبها\n\n"
        "سایت‌های کاربردی برای بررسی قیمت، "
        "داده‌ها و بازار فلزات گرانبها را انتخاب کنید:",
        reply_markup=gold_sites_keyboard,
    )


# ============================================================
# 💵 دلار و بازار ارز
# ============================================================

async def currency_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    currency_sites_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🇮🇷 TGJU",
                    url="https://www.tgju.org/",
                ),
                InlineKeyboardButton(
                    "🇮🇷 Bonbast",
                    url="https://www.bon-bast.com/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🇺🇸 Federal Reserve",
                    url="https://www.federalreserve.gov/releases/h10/",
                ),
                InlineKeyboardButton(
                    "🌍 Trading Economics",
                    url="https://tradingeconomics.com/currencies",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "💵 دلار و بازار ارز\n\n"
        "سایت‌های کاربردی برای بررسی نرخ ارز، "
        "دلار و بازارهای ارزی را انتخاب کنید:",
        reply_markup=currency_sites_keyboard,
    )


# ============================================================
# ₿ ارزهای دیجیتال
# ============================================================

async def crypto_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    crypto_sites_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📊 CoinMarketCap",
                    url="https://coinmarketcap.com/",
                ),
                InlineKeyboardButton(
                    "🦎 CoinGecko",
                    url="https://www.coingecko.com/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🔵 DeFiLlama",
                    url="https://defillama.com/",
                ),
                InlineKeyboardButton(
                    "👻 Aave",
                    url="https://aave.com/",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "₿ ارزهای دیجیتال\n\n"
        "سایت‌های کاربردی برای بررسی قیمت، "
        "داده‌های بازار و اکوسیستم DeFi را انتخاب کنید:",
        reply_markup=crypto_sites_keyboard,
    )


# ============================================================
# 🇮🇷 اقتصاد و بازار ایران
# ============================================================

async def iran_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    iran_sites_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏦 بانک مرکزی ایران",
                    url="https://www.cbi.ir/",
                ),
                InlineKeyboardButton(
                    "📊 مرکز آمار ایران",
                    url="https://www.amar.org.ir/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📈 TSETMC",
                    url="https://www.tsetmc.com/",
                ),
                InlineKeyboardButton(
                    "📑 کدال",
                    url="https://www.codal.ir/",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "🇮🇷 اقتصاد و بازار ایران\n\n"
        "سایت‌های کاربردی برای بررسی اقتصاد، "
        "بازار سرمایه و اطلاعات مالی ایران را انتخاب کنید:",
        reply_markup=iran_sites_keyboard,
    )


# ============================================================
# 📈 بورس و سهام آمریکا
# ============================================================

async def stock_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    stock_sites_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📊 FINVIZ",
                    url="https://finviz.com/",
                ),
                InlineKeyboardButton(
                    "🌍 Investing.com",
                    url="https://www.investing.com/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📈 StockCharts",
                    url="https://stockcharts.com/",
                ),
                InlineKeyboardButton(
                    "💰 Yahoo Finance",
                    url="https://finance.yahoo.com/",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "🇺🇸 بورس و سهام آمریکا\n\n"
        "سایت‌های کاربردی برای بررسی سهام، "
        "شاخص‌ها، نمودارها و اطلاعات مالی بازار آمریکا را انتخاب کنید:",
        reply_markup=stock_sites_keyboard,
    )


# ============================================================
# 🌍 بازارهای جهانی
# ============================================================

async def global_sites(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    global_sites_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📊 TradingView",
                    url="https://www.tradingview.com/",
                ),
                InlineKeyboardButton(
                    "🌍 Trading Economics",
                    url="https://tradingeconomics.com/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📰 MarketWatch",
                    url="https://www.marketwatch.com/",
                ),
                InlineKeyboardButton(
                    "📰 Reuters Markets",
                    url="https://www.reuters.com/markets/",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "🌍 بازارهای جهانی\n\n"
        "سایت‌های کاربردی برای بررسی بازارهای مالی، "
        "داده‌های اقتصادی، نمودارها و اخبار جهانی را انتخاب کنید:",
        reply_markup=global_sites_keyboard,
    )


# ============================================================
# 🛠 ابزارهای مالی
# ============================================================

async def financial_tools(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    financial_tools_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🧮 ماشین حساب فارکس",
                    url="https://www.myfxbook.com/forex-calculators",
                ),
                InlineKeyboardButton(
                    "₿ ماشین حساب کریپتو",
                    url="https://www.coinbase.com/converter",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🗓 Forex Factory",
                    url="https://www.forexfactory.com/calendar",
                ),
                InlineKeyboardButton(
                    "📅 Investing Calendar",
                    url="https://www.investing.com/economic-calendar/",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📊 Myfxbook Calendar",
                    url="https://www.myfxbook.com/forex-economic-calendar",
                ),
                InlineKeyboardButton(
                    "🌐 FXStreet Calendar",
                    url="https://www.fxstreet.com/economic-calendar",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏠 خانه",
                    callback_data="main_menu",
                ),
            ],
        ]
    )

    await update.message.reply_text(
        "🛠 ابزارهای مالی\n\n"
        "ابزارهای کاربردی برای محاسبات مالی، "
        "تقویم اقتصادی و بررسی رویدادهای مهم بازار را انتخاب کنید:",
        reply_markup=financial_tools_keyboard,
    )