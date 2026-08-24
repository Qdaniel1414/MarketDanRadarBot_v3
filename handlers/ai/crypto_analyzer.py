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
        print("❌ CRYPTO ANALYZER PRICE LOAD ERROR:", e)
        return {}


# ============================================================
# ₿ تحلیل بازار کریپتو
# ============================================================

async def crypto_market_analysis(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    prices = load_manual_prices()

    crypto = prices.get("crypto", {})
    global_prices = prices.get("global", {})

    # ========================================================
    # ₿ دریافت قیمت‌ها
    # ========================================================

    bitcoin = crypto.get(
        "bitcoin",
        global_prices.get("bitcoin"),
    )

    ethereum = crypto.get(
        "ethereum",
        global_prices.get("ethereum"),
    )

    bnb = crypto.get(
        "bnb",
        global_prices.get("bnb"),
    )

    solana = crypto.get(
        "solana",
        global_prices.get("solana"),
    )

    tether = crypto.get("tether")
    usdc = crypto.get("usdc")

    # ========================================================
    # ❌ بررسی اطلاعات
    # ========================================================

    if bitcoin is None and ethereum is None:
        await update.message.reply_text(
            "❌ اطلاعات قیمت کریپتو در سیستم پیدا نشد."
        )
        return

    # ========================================================
    # 📊 مقایسه BTC و ETH
    # ========================================================

    btc_eth_ratio = None

    if (
        bitcoin is not None
        and ethereum is not None
        and ethereum != 0
    ):
        btc_eth_ratio = bitcoin / ethereum

    # ========================================================
    # 🧠 تحلیل ساده
    # ========================================================

    if bitcoin is not None and ethereum is not None:

        if bitcoin > ethereum:
            market_comment = (
                "₿ بیت‌کوین در مقایسه با اتریوم ارزش دلاری "
                "بالاتری دارد و همچنان دارایی اصلی بازار کریپتو است."
            )
        else:
            market_comment = (
                "Ξ اتریوم در مقایسه با بیت‌کوین قیمت دلاری پایین‌تری "
                "دارد و برای مقایسه باید ارزش بازار و تعداد واحدها "
                "نیز در نظر گرفته شود."
            )

    else:
        market_comment = (
            "ℹ️ اطلاعات کافی برای مقایسه بیت‌کوین و اتریوم وجود ندارد."
        )

    # ========================================================
    # 📋 ساخت گزارش
    # ========================================================

    message = "₿ تحلیل هوشمند بازار کریپتو\n\n"

    if bitcoin is not None:
        message += (
            f"₿ Bitcoin: ${bitcoin:,.2f}\n"
        )

    if ethereum is not None:
        message += (
            f"Ξ Ethereum: ${ethereum:,.2f}\n"
        )

    if bnb is not None:
        message += (
            f"🟡 BNB: ${bnb:,.2f}\n"
        )

    if solana is not None:
        message += (
            f"◎ Solana: ${solana:,.2f}\n"
        )

    if tether is not None:
        message += (
            f"🪙 USDT: ${tether:,.2f}\n"
        )

    if usdc is not None:
        message += (
            f"💵 USDC: ${usdc:,.2f}\n"
        )

    if btc_eth_ratio is not None:
        message += (
            "\n📊 مقایسه Bitcoin و Ethereum\n"
            f"نسبت BTC/ETH: {btc_eth_ratio:,.2f}\n"
        )

    message += (
        "\n🧠 جمع‌بندی:\n"
        f"{market_comment}\n\n"
        "⚠️ توجه: این تحلیل بر اساس آخرین قیمت‌های "
        "ثبت‌شده در سیستم ربات است و توصیه خرید یا فروش نیست."
    )

    await update.message.reply_text(message)