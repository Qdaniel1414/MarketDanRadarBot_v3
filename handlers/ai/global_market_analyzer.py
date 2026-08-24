import json
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes


BASE_DIR = Path(__file__).resolve().parents[2]
MANUAL_PRICES_FILE = BASE_DIR / "data" / "manual_prices.json"


def load_manual_prices():
    try:
        with open(
            MANUAL_PRICES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except Exception as e:
        print("❌ GLOBAL MARKET ANALYZER PRICE LOAD ERROR:", e)
        return {}


def format_price(value):
    if value is None:
        return "-"

    if isinstance(value, float) and value.is_integer():
        return f"{int(value):,}"

    return f"{value:,.2f}"


async def global_market_analysis(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    prices = load_manual_prices()

    # =========================
    # GLOBAL
    # =========================

    global_prices = prices.get("global", {})

    ounce = global_prices.get("ounce")
    bitcoin = global_prices.get("bitcoin")
    ethereum = global_prices.get("ethereum")
    bnb = global_prices.get("bnb")
    solana = global_prices.get("solana")

    # =========================
    # GLOBAL MARKETS
    # =========================

    global_markets = prices.get("global_markets", {})

    commodities = global_markets.get("commodities", {})
    indices = global_markets.get("indices", {})
    stocks = global_markets.get("stocks", {})

    # Commodities
    wti = commodities.get("wti")
    brent = commodities.get("brent")
    natural_gas = commodities.get("natural_gas")
    silver = commodities.get("silver")
    copper = commodities.get("copper")

    # Indices
    sp500 = indices.get("sp500")
    nasdaq = indices.get("nasdaq")
    dow_jones = indices.get("dow_jones")
    vix = indices.get("vix")

    # Stocks
    nvda = stocks.get("nvda")
    aapl = stocks.get("aapl")
    msft = stocks.get("msft")
    googl = stocks.get("googl")
    amzn = stocks.get("amzn")
    meta = stocks.get("meta")
    jpm = stocks.get("jpm")

    # =========================
    # CHECK DATA
    # =========================

    all_data = [
        ounce,
        bitcoin,
        ethereum,
        bnb,
        solana,
        wti,
        brent,
        natural_gas,
        silver,
        copper,
        sp500,
        nasdaq,
        dow_jones,
        vix,
        nvda,
        aapl,
        msft,
        googl,
        amzn,
        meta,
        jpm,
    ]

    if all(value is None for value in all_data):
        await update.message.reply_text(
            "❌ اطلاعات بازارهای جهانی در سیستم پیدا نشد."
        )
        return

    # =========================
    # MESSAGE
    # =========================

    message = "📈 تحلیل هوشمند بازارهای جهانی\n\n"

    # =========================
    # GOLD & CRYPTO
    # =========================

    message += "🥇 طلا و رمزارزها\n"
    message += "━━━━━━━━━━━━━━\n"

    if ounce is not None:
        message += f"🥇 اونس جهانی طلا: ${format_price(ounce)}\n"

    if bitcoin is not None:
        message += f"₿ Bitcoin: ${format_price(bitcoin)}\n"

    if ethereum is not None:
        message += f"Ξ Ethereum: ${format_price(ethereum)}\n"

    if bnb is not None:
        message += f"🟡 BNB: ${format_price(bnb)}\n"

    if solana is not None:
        message += f"◎ Solana: ${format_price(solana)}\n"

    # =========================
    # COMMODITIES
    # =========================

    message += "\n🛢️ کالاهای جهانی\n"
    message += "━━━━━━━━━━━━━━\n"

    if wti is not None:
        message += f"🛢️ نفت WTI: ${format_price(wti)}\n"

    if brent is not None:
        message += f"🛢️ نفت Brent: ${format_price(brent)}\n"

    if natural_gas is not None:
        message += f"🔥 گاز طبیعی: ${format_price(natural_gas)}\n"

    if silver is not None:
        message += f"🥈 نقره: ${format_price(silver)}\n"

    if copper is not None:
        message += f"🔩 مس: ${format_price(copper)}\n"

    # =========================
    # INDICES
    # =========================

    message += "\n📊 شاخص‌های مهم\n"
    message += "━━━━━━━━━━━━━━\n"

    if sp500 is not None:
        message += f"📊 S&P 500: {format_price(sp500)}\n"

    if nasdaq is not None:
        message += f"💻 Nasdaq: {format_price(nasdaq)}\n"

    if dow_jones is not None:
        message += f"🏦 Dow Jones: {format_price(dow_jones)}\n"

    if vix is not None:
        message += f"📉 VIX: {format_price(vix)}\n"

    # =========================
    # STOCKS
    # =========================

    message += "\n🏢 سهام منتخب آمریکا\n"
    message += "━━━━━━━━━━━━━━\n"

    if nvda is not None:
        message += f"🟢 Nvidia: ${format_price(nvda)}\n"

    if aapl is not None:
        message += f"🍎 Apple: ${format_price(aapl)}\n"

    if msft is not None:
        message += f"🪟 Microsoft: ${format_price(msft)}\n"

    if googl is not None:
        message += f"🔎 Google: ${format_price(googl)}\n"

    if amzn is not None:
        message += f"📦 Amazon: ${format_price(amzn)}\n"

    if meta is not None:
        message += f"Ⓜ️ Meta: ${format_price(meta)}\n"

    if jpm is not None:
        message += f"🏦 JPMorgan: ${format_price(jpm)}\n"

    # =========================
    # SUMMARY
    # =========================

    message += (
        "\n🧠 جمع‌بندی:\n"
        "این بخش نمایی از وضعیت فعلی بازارهای جهانی را "
        "بر اساس قیمت‌های ثبت‌شده در سیستم ربات نمایش می‌دهد.\n\n"
        "برای تحلیل حرفه‌ای‌تر روند بازار، باید علاوه بر "
        "قیمت فعلی، تغییرات قیمت، روند تاریخی، حجم معاملات، "
        "بازدهی و شرایط اقتصادی نیز بررسی شود.\n\n"
        "⚠️ توجه: اطلاعات این گزارش بر اساس آخرین قیمت‌های "
        "ثبت‌شده در سیستم ربات است و توصیه خرید یا فروش نیست."
    )

    await update.message.reply_text(message)