import json
import re
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


# ============================================================
# STATES
# ============================================================

SMART_CALCULATOR_INPUT = 1


# ============================================================
# LOAD MANUAL PRICES
# ============================================================

def load_manual_prices():
    """
    خواندن قیمت‌ها از data/manual_prices.json
    """

    base_dir = Path(__file__).resolve().parents[2]
    prices_file = base_dir / "data" / "manual_prices.json"

    try:
        with open(
            prices_file,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except Exception as error:
        print(
            "❌ ERROR LOADING MANUAL PRICES:",
            error,
        )
        return {}


# ============================================================
# NORMALIZE NUMBERS
# ============================================================

def normalize_text(text: str) -> str:
    """
    تبدیل اعداد فارسی و عربی به انگلیسی
    """

    translation_table = str.maketrans(
        "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",
        "01234567890123456789",
    )

    text = text.translate(translation_table)

    # تبدیل جداکننده‌های رایج
    text = text.replace("٬", ",")
    text = text.replace("،", ",")

    return text


# ============================================================
# EXTRACT NUMBER
# ============================================================

def extract_number(text: str):
    """
    اولین عدد موجود در متن را پیدا می‌کند.
    """

    match = re.search(
        r"(?<!\d)(\d+(?:[.,]\d+)?)(?!\d)",
        text,
    )

    if not match:
        return None

    value = match.group(1).replace(",", "")

    # اگر عدد به صورت 0,5 یا 0.5 نوشته شده باشد
    value = value.replace(",", ".")

    try:
        return float(value)
    except ValueError:
        return None


# ============================================================
# FIND QUANTITY BEFORE ASSET
# ============================================================

def extract_quantity(text: str, asset_pattern: str):
    """
    مقدار دارایی را قبل از نام دارایی پیدا می‌کند.

    مثال:
    0.5 بیت کوین
    2 اتریوم
    10 BNB
    """

    pattern = (
        r"(\d+(?:[.,]\d+)?)"
        r"\s*"
        r""
        + asset_pattern
    )

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE,
    )

    if not match:
        return None

    value = match.group(1).replace(",", ".")

    try:
        return float(value)
    except ValueError:
        return None


# ============================================================
# FORMAT NUMBER
# ============================================================

def format_number(value: float):
    """
    نمایش عدد به شکل خوانا
    """

    if value == int(value):
        return f"{int(value):,}"

    return f"{value:,.8f}".rstrip("0").rstrip(".")


# ============================================================
# START SMART CALCULATOR
# ============================================================

async def smart_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return ConversationHandler.END

    await update.message.reply_text(
        "🧮 محاسبه‌گر هوشمند\n\n"
        "محاسبه‌ای که می‌خواهید انجام شود را به زبان ساده بنویسید.\n\n"
        "مثلاً:\n"
        "🔹 ارزش ۰.۵ بیت‌کوین چقدر می‌شود؟\n"
        "🔹 ارزش ۲ اتریوم چقدر می‌شود؟\n"
        "🔹 ارزش ۱۰ BNB چقدر می‌شود؟\n"
        "🔹 ارزش ۵۰ تتر چقدر می‌شود؟\n"
        "🔹 ارزش ۱۰۰۰ دلار چقدر می‌شود؟\n"
        "🔹 ارزش ۱۰ گرم طلای ۱۸ عیار چقدر می‌شود؟\n"
        "🔹 قیمت ۲ اونس طلا چقدر است؟\n"
        "🔹 ارزش ۲ سکه امامی چقدر می‌شود؟"
    )

    return SMART_CALCULATOR_INPUT


# ============================================================
# SMART CALCULATOR INPUT
# ============================================================

async def smart_calculator_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return ConversationHandler.END

    text = update.message.text.strip()

    print(
        "🤖 SMART CALCULATOR INPUT:",
        text,
    )

    normalized_text = normalize_text(text)

    prices = load_manual_prices()

    if not prices:
        await update.message.reply_text(
            "❌ اطلاعات قیمت‌ها از فایل قیمت ربات خوانده نشد."
        )

        return SMART_CALCULATOR_INPUT

    # ========================================================
    # CRYPTO PRICES
    # ========================================================

    crypto_prices = prices.get(
        "crypto",
        {},
    )

    # --------------------------------------------------------
    # BITCOIN
    # --------------------------------------------------------

    if (
        "بیت کوین" in normalized_text
        or "بیت‌کوین" in normalized_text
        or re.search(
            r"\bBTC\b",
            normalized_text,
            flags=re.IGNORECASE,
        )
    ):

        btc_amount = extract_quantity(
            normalized_text,
            r"(?:بیت[\s‌-]*کوین|BTC)",
        )

        if btc_amount is None:
            btc_amount = extract_number(normalized_text)

        if btc_amount is None:
            await update.message.reply_text(
                "❌ مقدار بیت‌کوین مشخص نیست.\n\n"
                "مثلاً بنویسید:\n"
                "ارزش 0.5 بیت کوین چقدر میشه؟"
            )

            return SMART_CALCULATOR_INPUT

        btc_price = float(
            crypto_prices.get(
                "bitcoin",
                prices.get("global", {}).get(
                    "bitcoin",
                    0,
                ),
            )
        )

        if btc_price <= 0:
            await update.message.reply_text(
                "❌ قیمت بیت‌کوین در دیتای ربات ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total_value = btc_amount * btc_price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 مقدار بیت‌کوین: "
            f"{format_number(btc_amount)} BTC\n"
            f"💵 قیمت هر بیت‌کوین: "
            f"{format_number(btc_price)} دلار\n"
            "📌 منبع قیمت: قیمت فعلی ثبت‌شده در ربات\n\n"
            f"💰 ارزش کل: "
            f"{format_number(total_value)} دلار"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # ETHEREUM
    # --------------------------------------------------------

    if (
        "اتریوم" in normalized_text
        or re.search(
            r"\bETH\b",
            normalized_text,
            flags=re.IGNORECASE,
        )
    ):

        eth_amount = extract_quantity(
            normalized_text,
            r"(?:اتریوم|ETH)",
        )

        if eth_amount is None:
            eth_amount = extract_number(normalized_text)

        if eth_amount is None:
            await update.message.reply_text(
                "❌ مقدار اتریوم مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        eth_price = float(
            crypto_prices.get(
                "ethereum",
                prices.get("global", {}).get(
                    "ethereum",
                    0,
                ),
            )
        )

        if eth_price <= 0:
            await update.message.reply_text(
                "❌ قیمت اتریوم در دیتای ربات ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total_value = eth_amount * eth_price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"♦️ مقدار اتریوم: "
            f"{format_number(eth_amount)} ETH\n"
            f"💵 قیمت هر اتریوم: "
            f"{format_number(eth_price)} دلار\n"
            "📌 منبع قیمت: قیمت فعلی ثبت‌شده در ربات\n\n"
            f"💰 ارزش کل: "
            f"{format_number(total_value)} دلار"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # TETHER
    # --------------------------------------------------------

    if (
        "تتر" in normalized_text
        or re.search(
            r"\bUSDT\b",
            normalized_text,
            flags=re.IGNORECASE,
        )
    ):

        usdt_amount = extract_quantity(
            normalized_text,
            r"(?:تتر|USDT)",
        )

        if usdt_amount is None:
            usdt_amount = extract_number(normalized_text)

        if usdt_amount is None:
            await update.message.reply_text(
                "❌ مقدار تتر مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        usdt_price_usd = float(
            crypto_prices.get(
                "tether",
                1,
            )
        )

        usdt_price_toman = float(
            prices.get(
                "currency",
                {},
            ).get(
                "usdt",
                0,
            )
        )

        total_usd = (
            usdt_amount * usdt_price_usd
        )

        total_toman = (
            usdt_amount * usdt_price_toman
        )

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"💵 مقدار تتر: "
            f"{format_number(usdt_amount)} USDT\n"
            f"💲 ارزش دلاری: "
            f"{format_number(total_usd)} دلار\n"
            f"🇮🇷 قیمت هر تتر: "
            f"{format_number(usdt_price_toman)} تومان\n\n"
            f"💰 ارزش تقریبی: "
            f"{format_number(total_toman)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # BNB
    # --------------------------------------------------------

    if (
        "bnb" in normalized_text.lower()
        or "بایننس" in normalized_text
    ):

        amount = extract_quantity(
            normalized_text,
            r"(?:BNB|bnb|بایننس)",
        )

        if amount is None:
            amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار BNB مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            crypto_prices.get(
                "bnb",
                prices.get("global", {}).get(
                    "bnb",
                    0,
                ),
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت BNB در دیتای ربات ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 مقدار BNB: "
            f"{format_number(amount)} BNB\n"
            f"💵 قیمت هر BNB: "
            f"{format_number(price)} دلار\n\n"
            f"💰 ارزش کل: "
            f"{format_number(total)} دلار"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # USDC
    # --------------------------------------------------------

    if (
        "usdc" in normalized_text.lower()
        or "یو اس دی سی" in normalized_text.lower()
    ):

        amount = extract_quantity(
            normalized_text,
            r"(?:USDC|usdc|یو\s*اس\s*دی\s*سی)",
        )

        if amount is None:
            amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار USDC مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            crypto_prices.get(
                "usdc",
                1,
            )
        )

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"💵 مقدار USDC: "
            f"{format_number(amount)} USDC\n"
            f"💲 ارزش تقریبی: "
            f"{format_number(total)} دلار"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # SOLANA
    # --------------------------------------------------------

    if (
        "سولانا" in normalized_text
        or re.search(
            r"\bSOL\b",
            normalized_text,
            flags=re.IGNORECASE,
        )
    ):

        amount = extract_quantity(
            normalized_text,
            r"(?:سولانا|SOL)",
        )

        if amount is None:
            amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار سولانا مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            crypto_prices.get(
                "solana",
                prices.get("global", {}).get(
                    "solana",
                    0,
                ),
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت سولانا در دیتای ربات ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 مقدار سولانا: "
            f"{format_number(amount)} SOL\n"
            f"💵 قیمت هر سولانا: "
            f"{format_number(price)} دلار\n\n"
            f"💰 ارزش کل: "
            f"{format_number(total)} دلار"
        )

        return SMART_CALCULATOR_INPUT

    # ========================================================
    # GOLD
    # ========================================================

    gold_prices = prices.get(
        "gold",
        {},
    )

    # --------------------------------------------------------
    # GOLD 18
    # --------------------------------------------------------

    if (
        "طلای 18" in normalized_text
        or "طلای ۱۸" in text
        or "عیار 18" in normalized_text
        or "عیار ۱۸" in text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار گرم طلا مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            gold_prices.get(
                "gold18",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت طلای ۱۸ عیار ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🥇 مقدار طلا: "
            f"{format_number(amount)} گرم\n"
            f"💰 قیمت هر گرم طلای ۱۸ عیار: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # GOLD 24
    # --------------------------------------------------------

    if (
        "طلای 24" in normalized_text
        or "طلای ۲۴" in text
        or "عیار 24" in normalized_text
        or "عیار ۲۴" in text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار گرم طلا مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            gold_prices.get(
                "gold24",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت طلای ۲۴ عیار ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🥇 مقدار طلا: "
            f"{format_number(amount)} گرم\n"
            f"💰 قیمت هر گرم طلای ۲۴ عیار: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # MELTED GOLD
    # --------------------------------------------------------

    if (
        "آبشده" in normalized_text
        or "آب شده" in normalized_text
        or "مذاب" in normalized_text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار گرم طلای آب‌شده مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            gold_prices.get(
                "melted",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت طلای آب‌شده ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🥇 مقدار طلای آب‌شده: "
            f"{format_number(amount)} گرم\n"
            f"💰 قیمت هر گرم آب‌شده: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # GOLD GRAM
    # --------------------------------------------------------

    if (
        "گرم طلا" in normalized_text
        or "gram" in normalized_text.lower()
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار گرم طلا مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        price = float(
            gold_prices.get(
                "gram",
                gold_prices.get(
                    "gold18",
                    0,
                ),
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت گرم طلا ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🥇 مقدار طلا: "
            f"{format_number(amount)} گرم\n"
            f"💰 قیمت هر گرم: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # GOLD OUNCE
    # --------------------------------------------------------

    if (
        "اونس" in normalized_text
        or "انس" in normalized_text
        or "ounce" in normalized_text.lower()
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            amount = 1

        price = float(
            gold_prices.get(
                "ounce",
                prices.get("global", {}).get(
                    "ounce",
                    0,
                ),
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت اونس جهانی در دیتای ربات ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🌎 مقدار اونس: "
            f"{format_number(amount)} اونس\n"
            f"🥇 قیمت هر اونس: "
            f"{format_number(price)} دلار\n\n"
            f"💰 ارزش کل: "
            f"{format_number(total)} دلار"
        )

        return SMART_CALCULATOR_INPUT

    # ========================================================
    # COINS
    # ========================================================

    coin_prices = prices.get(
        "coin",
        {},
    )

    # --------------------------------------------------------
    # EMAMI
    # --------------------------------------------------------

    if (
        "سکه امامی" in normalized_text
        or "امامی" in normalized_text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            amount = 1

        price = float(
            coin_prices.get(
                "imami",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت سکه امامی ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 تعداد سکه امامی: "
            f"{format_number(amount)}\n"
            f"💰 قیمت هر سکه: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # BAHAR AZADI
    # --------------------------------------------------------

    if (
        "بهار آزادی" in normalized_text
        or "بهارآزادی" in normalized_text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            amount = 1

        price = float(
            coin_prices.get(
                "bahar",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت سکه بهار آزادی ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 تعداد سکه بهار آزادی: "
            f"{format_number(amount)}\n"
            f"💰 قیمت هر سکه: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # HALF COIN
    # --------------------------------------------------------

    if (
        "نیم سکه" in normalized_text
        or "نیم‌سکه" in text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            amount = 1

        price = float(
            coin_prices.get(
                "nim",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت نیم‌سکه ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 تعداد نیم‌سکه: "
            f"{format_number(amount)}\n"
            f"💰 قیمت هر نیم‌سکه: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # QUARTER COIN
    # --------------------------------------------------------

    if (
        "ربع سکه" in normalized_text
        or "ربع‌سکه" in text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            amount = 1

        price = float(
            coin_prices.get(
                "rob",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت ربع‌سکه ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 تعداد ربع‌سکه: "
            f"{format_number(amount)}\n"
            f"💰 قیمت هر ربع‌سکه: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # --------------------------------------------------------
    # GERAMI COIN
    # --------------------------------------------------------

    if (
        "سکه گرمی" in normalized_text
        or "سکه‌گرمی" in text
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            amount = 1

        price = float(
            coin_prices.get(
                "gerami",
                0,
            )
        )

        if price <= 0:
            await update.message.reply_text(
                "❌ قیمت سکه گرمی ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"🪙 تعداد سکه گرمی: "
            f"{format_number(amount)}\n"
            f"💰 قیمت هر سکه گرمی: "
            f"{format_number(price)} تومان\n\n"
            f"💵 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # ========================================================
    # USD
    # ========================================================

    if (
        "دلار" in normalized_text
        or "usd" in normalized_text.lower()
    ):

        amount = extract_number(normalized_text)

        if amount is None:
            await update.message.reply_text(
                "❌ مقدار دلار مشخص نیست."
            )

            return SMART_CALCULATOR_INPUT

        usd_price = float(
            prices.get(
                "currency",
                {},
            ).get(
                "usd",
                0,
            )
        )

        if usd_price <= 0:
            await update.message.reply_text(
                "❌ قیمت دلار در دیتای ربات ثبت نشده است."
            )

            return SMART_CALCULATOR_INPUT

        total = amount * usd_price

        await update.message.reply_text(
            "🧮 نتیجه محاسبه\n\n"
            f"💵 مقدار دلار: "
            f"{format_number(amount)} USD\n"
            f"🇮🇷 قیمت هر دلار: "
            f"{format_number(usd_price)} تومان\n\n"
            f"💰 ارزش کل: "
            f"{format_number(total)} تومان"
        )

        return SMART_CALCULATOR_INPUT

    # ========================================================
    # UNKNOWN REQUEST
    # ========================================================

    await update.message.reply_text(
        "⚠️ فعلاً این نوع محاسبه برای محاسبه‌گر هوشمند فعال نشده است.\n\n"
        "دارایی‌های فعلی:\n"
        "🪙 BTC\n"
        "♦️ ETH\n"
        "💵 USDT\n"
        "🟡 BNB\n"
        "💲 USDC\n"
        "🟣 SOL\n"
        "🥇 طلا\n"
        "🪙 سکه\n"
        "💵 دلار"
    )

    return SMART_CALCULATOR_INPUT