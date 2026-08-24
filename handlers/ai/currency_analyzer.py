import json
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes


# ============================================================
# 📁 مسیر فایل قیمت‌های دستی
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]
MANUAL_PRICES_FILE = BASE_DIR / "data" / "manual_prices.json"


# ============================================================
# 📥 دریافت قیمت‌ها
# ============================================================

def load_manual_prices():
    try:
        with open(
            MANUAL_PRICES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except Exception as e:
        print("❌ MANUAL PRICES LOAD ERROR:", e)
        return {}


# ============================================================
# 💵 تحلیل دلار و ارز
# ============================================================

async def currency_market_analysis(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    prices = load_manual_prices()

    currency = prices.get("currency", {})

    usd = currency.get("usd")
    usdt = currency.get("usdt")
    eur = currency.get("eur")
    gbp = currency.get("gbp")
    aed = currency.get("aed")
    try_price = currency.get("try")

    if usd is None:
        await update.message.reply_text(
            "❌ قیمت دلار در فایل قیمت‌ها پیدا نشد."
        )
        return

    # ========================================================
    # 📊 محاسبه اختلاف دلار و تتر
    # ========================================================

    usdt_difference = None
    usdt_percent = None

    if usdt is not None and usd != 0:
        usdt_difference = usdt - usd
        usdt_percent = (usdt_difference / usd) * 100

    # ========================================================
    # 🧠 تحلیل ساده
    # ========================================================

    if usdt_difference is not None:

        if usdt_difference > 0:
            market_comment = (
                "🔺 تتر بالاتر از دلار معامله می‌شود؛ "
                "این اختلاف می‌تواند نشان‌دهنده فشار تقاضا "
                "در بازار ارز باشد."
            )

        elif usdt_difference < 0:
            market_comment = (
                "🔻 تتر پایین‌تر از دلار قرار دارد؛ "
                "در این لحظه تتر نسبت به دلار اختلاف منفی دارد."
            )

        else:
            market_comment = (
                "⚖️ قیمت تتر و دلار تقریباً برابر است."
            )

    else:
        market_comment = (
            "ℹ️ اطلاعات کافی برای مقایسه دلار و تتر وجود ندارد."
        )

    # ========================================================
    # 📋 ساخت گزارش
    # ========================================================

    message = "📊 تحلیل هوشمند دلار و ارز\n\n"

    message += (
        f"💵 دلار: {usd:,.0f} تومان\n"
    )

    if usdt is not None:
        message += (
            f"🪙 تتر: {usdt:,.0f} تومان\n"
        )

    if eur is not None:
        message += (
            f"💶 یورو: {eur:,.0f} تومان\n"
        )

    if gbp is not None:
        message += (
            f"🇬🇧 پوند: {gbp:,.0f} تومان\n"
        )

    if aed is not None:
        message += (
            f"🇦🇪 درهم: {aed:,.0f} تومان\n"
        )

    if try_price is not None:
        message += (
            f"🇹🇷 لیر: {try_price:,.0f} تومان\n"
        )

    message += "\n"

    if usdt_difference is not None:
        sign = "+" if usdt_difference > 0 else ""

        message += (
            "📈 مقایسه دلار و تتر\n"
            f"اختلاف: {sign}{usdt_difference:,.0f} تومان\n"
            f"درصد اختلاف: {usdt_percent:+.2f}%\n\n"
        )

    message += (
        "🧠 جمع‌بندی:\n"
        f"{market_comment}\n\n"
        "⚠️ توجه: این تحلیل بر اساس آخرین قیمت‌های "
        "ثبت‌شده در سیستم ربات است و توصیه خرید یا فروش نیست."
    )

    await update.message.reply_text(message)