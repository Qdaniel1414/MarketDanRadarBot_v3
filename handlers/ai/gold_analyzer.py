import json
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes


# ============================================================
# 📁 مسیر فایل قیمت‌ها
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
        print("❌ GOLD ANALYZER PRICE LOAD ERROR:", e)
        return {}


# ============================================================
# 🥇 تحلیل طلا و سکه
# ============================================================

async def gold_market_analysis(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    prices = load_manual_prices()

    gold = prices.get("gold", {})
    coin = prices.get("coin", {})
    currency = prices.get("currency", {})
    global_prices = prices.get("global", {})

    # ========================================================
    # 💵 قیمت دلار
    # ========================================================

    usd = currency.get("usd")

    # ========================================================
    # 🥇 قیمت طلا
    # ========================================================

    gold18 = gold.get("gold18")
    gold24 = gold.get("gold24")
    melted = gold.get("melted")

    # ========================================================
    # 🪙 قیمت سکه‌ها
    # ========================================================

    imami = coin.get("imami")
    bahar = coin.get("bahar")
    nim = coin.get("nim")
    rob = coin.get("rob")
    gerami = coin.get("gerami")

    # ========================================================
    # 🌎 اونس جهانی
    # ========================================================

    ounce = global_prices.get("ounce")

    # ========================================================
    # ❌ بررسی اطلاعات
    # ========================================================

    if gold18 is None and imami is None:
        await update.message.reply_text(
            "❌ اطلاعات قیمت طلا و سکه در سیستم پیدا نشد."
        )
        return

    # ========================================================
    # 📊 محاسبه قیمت نظری تقریبی طلای ۱۸ عیار
    #
    # فرمول:
    # دلار × اونس ÷ 31.103 × 0.75
    # ========================================================

    theoretical_gold18 = None
    gold_bubble_percent = None

    if usd is not None and ounce is not None:
        theoretical_gold18 = (
            usd * ounce / 31.103
        ) * 0.75

        if gold18 is not None and theoretical_gold18 != 0:
            gold_bubble_percent = (
                (gold18 - theoretical_gold18)
                / theoretical_gold18
            ) * 100

    # ========================================================
    # 🧠 تحلیل ساده بازار
    # ========================================================

    if gold_bubble_percent is not None:

        if gold_bubble_percent > 5:
            market_comment = (
                "🔺 قیمت طلای ۱۸ عیار بالاتر از قیمت نظری "
                "محاسبه‌شده قرار دارد."
            )

        elif gold_bubble_percent < -5:
            market_comment = (
                "🔻 قیمت طلای ۱۸ عیار پایین‌تر از قیمت نظری "
                "محاسبه‌شده قرار دارد."
            )

        else:
            market_comment = (
                "⚖️ قیمت طلای ۱۸ عیار به قیمت نظری محاسبه‌شده "
                "نزدیک است."
            )

    else:
        market_comment = (
            "ℹ️ اطلاعات کافی برای محاسبه قیمت نظری طلا وجود ندارد."
        )

    # ========================================================
    # 📋 ساخت گزارش
    # ========================================================

    message = "🥇 تحلیل هوشمند طلا و سکه\n\n"

    if gold18 is not None:
        message += (
            f"🥇 طلای ۱۸ عیار: {gold18:,.0f} تومان\n"
        )

    if gold24 is not None:
        message += (
            f"🥇 طلای ۲۴ عیار: {gold24:,.0f} تومان\n"
        )

    if melted is not None:
        message += (
            f"🔶 طلای آب‌شده: {melted:,.0f} تومان\n"
        )

    message += "\n🪙 قیمت سکه‌ها\n"

    if imami is not None:
        message += (
            f"🪙 سکه امامی: {imami:,.0f} تومان\n"
        )

    if bahar is not None:
        message += (
            f"🪙 بهار آزادی: {bahar:,.0f} تومان\n"
        )

    if nim is not None:
        message += (
            f"🪙 نیم‌سکه: {nim:,.0f} تومان\n"
        )

    if rob is not None:
        message += (
            f"🪙 ربع‌سکه: {rob:,.0f} تومان\n"
        )

    if gerami is not None:
        message += (
            f"🪙 سکه گرمی: {gerami:,.0f} تومان\n"
        )

    if usd is not None or ounce is not None:
        message += "\n🌎 عوامل جهانی\n"

        if usd is not None:
            message += (
                f"💵 دلار: {usd:,.0f} تومان\n"
            )

        if ounce is not None:
            message += (
                f"🌎 اونس جهانی: ${ounce:,.0f}\n"
            )

    if theoretical_gold18 is not None:
        message += (
            "\n📐 قیمت نظری طلای ۱۸ عیار\n"
            f"{theoretical_gold18:,.0f} تومان\n"
        )

    if gold_bubble_percent is not None:
        message += (
            f"📊 اختلاف با قیمت نظری: "
            f"{gold_bubble_percent:+.2f}%\n"
        )

    message += (
        "\n🧠 جمع‌بندی:\n"
        f"{market_comment}\n\n"
        "⚠️ توجه: این تحلیل بر اساس آخرین قیمت‌های "
        "ثبت‌شده در سیستم ربات است و توصیه خرید یا فروش نیست."
    )

    await update.message.reply_text(message)