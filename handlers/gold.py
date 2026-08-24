from datetime import datetime
import json
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes

from keyboards.market_keyboard import market_keyboard


# =========================================================
# مسیر فایل قیمت‌های دستی
# =========================================================

PRICE_FILE = Path("data/manual_prices.json")


# =========================================================
# قیمت‌های پیش‌فرض
#
# فقط در صورتی استفاده می‌شوند که کلید مربوطه
# داخل فایل manual_prices.json وجود نداشته باشد.
# =========================================================

DEFAULT_GOLD_PRICES = {
    "طلای 18 عیار": 16333400,
    "طلای 24 عیار": 21778000,
    "طلای آبشده": 70780000,

    "سکه امامی": 166005000,
    "سکه بهار آزادی": 152000000,
    "نیم سکه": 93000000,
    "ربع سکه": 53000000,
    "سکه گرمی": 30000000,
}


# =========================================================
# خواندن قیمت‌های دستی از JSON
# =========================================================

def load_manual_gold_prices():
    """
    قیمت طلا و سکه را مستقیماً از
    data/manual_prices.json می‌خواند.

    این همان فایلی است که دستورات ادمین
    مثل /setimami داخل آن قیمت را ذخیره می‌کنند.
    """

    prices = DEFAULT_GOLD_PRICES.copy()

    try:

        if not PRICE_FILE.exists():
            print(
                f"⚠️ PRICE FILE NOT FOUND: {PRICE_FILE}"
            )

            return prices

        with open(
            PRICE_FILE,
            "r",
            encoding="utf-8",
        ) as f:

            data = json.load(f)

        # -------------------------------------------------
        # بخش gold
        # -------------------------------------------------

        gold_data = data.get("gold", {})

        # طلای 18 عیار
        if "gold18" in gold_data:

            prices["طلای 18 عیار"] = int(
                gold_data["gold18"]
            )

        # طلای 24 عیار
        if "gold24" in gold_data:

            prices["طلای 24 عیار"] = int(
                gold_data["gold24"]
            )

        # طلای آبشده
        if "melted" in gold_data:

            prices["طلای آبشده"] = int(
                gold_data["melted"]
            )

        # -------------------------------------------------
        # سکه‌ها
        # -------------------------------------------------

        # سکه امامی
        if "imami" in gold_data:

            prices["سکه امامی"] = int(
                gold_data["imami"]
            )

        # سکه بهار آزادی
        if "bahar" in gold_data:

            prices["سکه بهار آزادی"] = int(
                gold_data["bahar"]
            )

        # نیم سکه
        if "nim" in gold_data:

            prices["نیم سکه"] = int(
                gold_data["nim"]
            )

        # ربع سکه
        if "rob" in gold_data:

            prices["ربع سکه"] = int(
                gold_data["rob"]
            )

        # سکه گرمی
        if "gerami" in gold_data:

            prices["سکه گرمی"] = int(
                gold_data["gerami"]
            )

        print(
            "✅ MANUAL GOLD PRICES LOADED FROM JSON"
        )

        print(
            f"🥇 Gold18: {prices['طلای 18 عیار']:,}"
        )

        print(
            f"🥇 Gold24: {prices['طلای 24 عیار']:,}"
        )

        print(
            f"🔥 Melted: {prices['طلای آبشده']:,}"
        )

        print(
            f"🪙 Imami: {prices['سکه امامی']:,}"
        )

        print(
            f"🥈 Bahar: {prices['سکه بهار آزادی']:,}"
        )

        print(
            f"🥉 Nim: {prices['نیم سکه']:,}"
        )

        print(
            f"🔹 Rob: {prices['ربع سکه']:,}"
        )

        print(
            f"⚪ Gerami: {prices['سکه گرمی']:,}"
        )

    except Exception as e:

        print(
            f"❌ ERROR LOADING MANUAL GOLD PRICES: {e}"
        )

        print(
            "⚠️ USING DEFAULT GOLD PRICES"
        )

    return prices


# =========================================================
# فرمت قیمت
# =========================================================

def format_price(price):

    try:

        return f"{int(price):,} تومان"

    except (ValueError, TypeError):

        return "نامشخص"


# =========================================================
# نمایش قیمت طلا و سکه
# =========================================================

async def gold_prices(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    # =====================================================
    # بسیار مهم:
    # هر بار که کاربر صفحه طلا و سکه را باز می‌کند،
    # JSON دوباره خوانده می‌شود.
    #
    # بنابراین قیمت جدید بدون Restart قابل مشاهده است.
    # =====================================================

    prices = load_manual_gold_prices()

    # =====================================================
    # متن قیمت‌ها
    # =====================================================

    text = (
        "🥇 قیمت لحظه‌ای طلا و سکه 🇮🇷\n"
        "━━━━━━━━━━━━━━\n\n"

        "🟡 طلا\n\n"

        "🔸 طلای 18 عیار:\n"
        f"{format_price(prices['طلای 18 عیار'])}\n\n"

        "🔸 طلای 24 عیار:\n"
        f"{format_price(prices['طلای 24 عیار'])}\n\n"

        "🔸 طلای آبشده:\n"
        f"{format_price(prices['طلای آبشده'])}\n\n"

        "━━━━━━━━━━━━━━\n\n"

        "🪙 سکه‌ها\n\n"

        "🥇 سکه امامی:\n"
        f"{format_price(prices['سکه امامی'])}\n\n"

        "🥈 سکه بهار آزادی:\n"
        f"{format_price(prices['سکه بهار آزادی'])}\n\n"

        "🥉 نیم سکه:\n"
        f"{format_price(prices['نیم سکه'])}\n\n"

        "🔹 ربع سکه:\n"
        f"{format_price(prices['ربع سکه'])}\n\n"

        "⚪ سکه گرمی:\n"
        f"{format_price(prices['سکه گرمی'])}\n\n"

        "━━━━━━━━━━━━━━\n\n"
    )

    # =====================================================
    # زمان نمایش
    # =====================================================

    now = datetime.now().strftime("%H:%M:%S")

    text += (
        "🕒 آخرین بروزرسانی:\n"
        f"{now}\n\n"

        "📌 قیمت طلا و سکه به صورت دستی "
        "توسط مدیریت بروزرسانی می‌شود."
    )

    # =====================================================
    # ارسال
    # =====================================================

    await update.message.reply_text(
        text,
        reply_markup=market_keyboard,
    )