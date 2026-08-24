from telegram import Update
from telegram.ext import ContextTypes

import json
from pathlib import Path


ADMIN_ID = 8920456282

PRICE_FILE = Path("data/manual_prices.json")

user_states = {}


SET_COMMANDS = {
    # =====================================
    # ارز
    # =====================================

    "SET_USD": ("currency", "usd", "💵 قیمت دلار"),
    "SET_USDT": ("currency", "usdt", "💲 قیمت تتر"),
    "SET_AED": ("currency", "aed", "🇦🇪 قیمت درهم"),
    "SET_EUR": ("currency", "eur", "🇪🇺 قیمت یورو"),
    "SET_GBP": ("currency", "gbp", "🇬🇧 قیمت پوند"),
    "SET_TRY": ("currency", "try", "🇹🇷 قیمت لیر"),

    # =====================================
    # طلا و سکه
    # =====================================

    "SET_GOLD18": ("gold", "gold18", "🥇 طلای ۱۸ عیار"),
    "SET_GOLD24": ("gold", "gold24", "🥇 طلای ۲۴ عیار"),
    "SET_MELTED": ("gold", "melted", "🔥 طلای آبشده"),

    "SET_IMAMI": ("gold", "imami", "🪙 سکه امامی"),
    "SET_BAHAR": ("gold", "bahar", "🥈 سکه بهار آزادی"),
    "SET_NIM": ("gold", "nim", "🥉 نیم سکه"),
    "SET_ROB": ("gold", "rob", "🔹 ربع سکه"),
    "SET_GERAMI": ("gold", "gerami", "⚪ سکه گرمی"),

    # =====================================
    # قیمت‌های جهانی قبلی
    # =====================================

    "SET_OUNCE": ("global", "ounce", "🌍 اونس جهانی"),
    "SET_BTC": ("global", "bitcoin", "₿ بیت کوین"),
    "SET_ETH": ("global", "ethereum", "Ξ اتریوم"),

    # =====================================
    # کامودیتی‌ها
    # =====================================

    "SET_WTI": (
        "global_markets",
        "commodities.wti",
        "🛢️ نفت WTI",
    ),

    "SET_BRENT": (
        "global_markets",
        "commodities.brent",
        "🛢️ نفت Brent",
    ),

    "SET_GAS": (
        "global_markets",
        "commodities.natural_gas",
        "🔥 گاز طبیعی",
    ),

    "SET_SILVER": (
        "global_markets",
        "commodities.silver",
        "🥈 نقره",
    ),

    "SET_COPPER": (
        "global_markets",
        "commodities.copper",
        "🔩 مس",
    ),

    # =====================================
    # شاخص‌های اصلی
    # =====================================

    "SET_SP500": (
        "global_markets",
        "indices.sp500",
        "📊 S&P 500",
    ),

    "SET_NASDAQ": (
        "global_markets",
        "indices.nasdaq",
        "💻 Nasdaq",
    ),

    "SET_DOW": (
        "global_markets",
        "indices.dow_jones",
        "🏦 Dow Jones",
    ),

    "SET_VIX": (
        "global_markets",
        "indices.vix",
        "📉 VIX",
    ),

    # =====================================
    # سهام آمریکا
    # =====================================

    "SET_NVDA": (
        "global_markets",
        "stocks.nvda",
        "🟢 Nvidia",
    ),

    "SET_AAPL": (
        "global_markets",
        "stocks.aapl",
        "🍎 Apple",
    ),

    "SET_MSFT": (
        "global_markets",
        "stocks.msft",
        "🪟 Microsoft",
    ),

    "SET_GOOGL": (
        "global_markets",
        "stocks.googl",
        "🔎 Google",
    ),

    "SET_AMZN": (
        "global_markets",
        "stocks.amzn",
        "📦 Amazon",
    ),

    "SET_META": (
        "global_markets",
        "stocks.meta",
        "Ⓜ️ Meta",
    ),

    "SET_JPM": (
        "global_markets",
        "stocks.jpm",
        "🏦 JPMorgan",
    ),
}


# =====================================
# خواندن قیمت‌ها
# =====================================

def load_prices():
    with open(
        PRICE_FILE,
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)


# =====================================
# ذخیره قیمت‌ها
# =====================================

def save_prices(data):
    with open(
        PRICE_FILE,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4,
        )


# =====================================
# قرار دادن مقدار داخل مسیر تو در تو
# مثال:
# commodities.wti
# stocks.nvda
# =====================================

def set_nested_value(data, path, value):
    keys = path.split(".")

    current = data

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}

        current = current[key]

    current[keys[-1]] = value


# =====================================
# شروع بروزرسانی قیمت
# =====================================

async def start_set(
    update,
    context,
    state,
):

    if update.effective_user is None:
        return

    if update.message is None:
        return

    if update.effective_user.id != ADMIN_ID:
        return

    user_states[
        update.effective_user.id
    ] = state

    _, _, title = SET_COMMANDS[state]

    await update.message.reply_text(
        f"{title} جدید را وارد کن:"
    )


# =====================================
# دستورات ارز
# =====================================

async def set_usd(update, context):
    await start_set(update, context, "SET_USD")


async def set_usdt(update, context):
    await start_set(update, context, "SET_USDT")


async def set_aed(update, context):
    await start_set(update, context, "SET_AED")


async def set_eur(update, context):
    await start_set(update, context, "SET_EUR")


async def set_gbp(update, context):
    await start_set(update, context, "SET_GBP")


async def set_try(update, context):
    await start_set(update, context, "SET_TRY")


# =====================================
# دستورات طلا
# =====================================

async def set_gold18(update, context):
    await start_set(update, context, "SET_GOLD18")


async def set_gold24(update, context):
    await start_set(update, context, "SET_GOLD24")


async def set_melted(update, context):
    await start_set(update, context, "SET_MELTED")


async def set_imami(update, context):
    await start_set(update, context, "SET_IMAMI")


async def set_bahar(update, context):
    await start_set(update, context, "SET_BAHAR")


async def set_nim(update, context):
    await start_set(update, context, "SET_NIM")


async def set_rob(update, context):
    await start_set(update, context, "SET_ROB")


async def set_gerami(update, context):
    await start_set(update, context, "SET_GERAMI")


# =====================================
# دستورات قیمت جهانی
# =====================================

async def set_ounce(update, context):
    await start_set(update, context, "SET_OUNCE")


async def set_btc(update, context):
    await start_set(update, context, "SET_BTC")


async def set_eth(update, context):
    await start_set(update, context, "SET_ETH")


# =====================================
# دستورات کامودیتی‌ها
# =====================================

async def set_wti(update, context):
    await start_set(update, context, "SET_WTI")


async def set_brent(update, context):
    await start_set(update, context, "SET_BRENT")


async def set_gas(update, context):
    await start_set(update, context, "SET_GAS")


async def set_silver(update, context):
    await start_set(update, context, "SET_SILVER")


async def set_copper(update, context):
    await start_set(update, context, "SET_COPPER")


# =====================================
# دستورات شاخص‌ها
# =====================================

async def set_sp500(update, context):
    await start_set(update, context, "SET_SP500")


async def set_nasdaq(update, context):
    await start_set(update, context, "SET_NASDAQ")


async def set_dow(update, context):
    await start_set(update, context, "SET_DOW")


async def set_vix(update, context):
    await start_set(update, context, "SET_VIX")


# =====================================
# دستورات سهام آمریکا
# =====================================

async def set_nvda(update, context):
    await start_set(update, context, "SET_NVDA")


async def set_aapl(update, context):
    await start_set(update, context, "SET_AAPL")


async def set_msft(update, context):
    await start_set(update, context, "SET_MSFT")


async def set_googl(update, context):
    await start_set(update, context, "SET_GOOGL")


async def set_amzn(update, context):
    await start_set(update, context, "SET_AMZN")


async def set_meta(update, context):
    await start_set(update, context, "SET_META")


async def set_jpm(update, context):
    await start_set(update, context, "SET_JPM")


# =====================================
# دریافت و ذخیره قیمت
# =====================================

async def admin_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update is None:
        return

    if update.effective_user is None:
        return

    if update.message is None:
        return

    if update.message.text is None:
        return

    # فقط ادمین
    if update.effective_user.id != ADMIN_ID:
        return

    state = user_states.get(
        update.effective_user.id
    )

    if state not in SET_COMMANDS:
        return

    try:

        raw_price = (
            update.message.text
            .replace(",", "")
            .replace("،", ".")
        )

        price = float(raw_price)

        section, key, title = SET_COMMANDS[state]

        data = load_prices()

        # -------------------------------------
        # قیمت‌های قدیمی که مسیر ساده دارند
        # -------------------------------------

        if "." not in key:
            data[section][key] = price

        # -------------------------------------
        # قیمت‌های جدید با مسیر تو در تو
        # -------------------------------------

        else:
            set_nested_value(
                data[section],
                key,
                price,
            )

        save_prices(data)

        user_states.pop(
            update.effective_user.id,
            None,
        )

        # -------------------------------------
        # واحد قیمت
        # -------------------------------------

        if section == "currency":
            unit = "تومان"

        elif section == "gold":
            unit = "تومان"

        elif section == "global":
            unit = "دلار"

        else:
            unit = "دلار"

        # -------------------------------------
        # نمایش عدد بدون اعشار اضافی
        # -------------------------------------

        if price.is_integer():
            display_price = f"{int(price):,}"
        else:
            display_price = f"{price:,.2f}"

        await update.message.reply_text(
            f"✅ {title} بروزرسانی شد.\n\n"
            f"{display_price} {unit}"
        )

    except ValueError:

        await update.message.reply_text(
            "❌ فقط عدد وارد کن.\n\n"
            "مثال:\n"
            "90.25"
        )