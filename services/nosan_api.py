import json
from pathlib import Path

from data.manual_prices import (
    CURRENCY_PRICES,
    GOLD_PRICES,
    GLOBAL_PRICES,
)


# =========================================================
# مسیر قیمت‌های دستی
# =========================================================

PRICE_FILE = Path("data/manual_prices.json")


# =========================================================
# خواندن قیمت‌های دستی از JSON
# =========================================================

def load_manual_prices():
    try:
        with open(
            PRICE_FILE,
            "r",
            encoding="utf-8",
        ) as f:
            return json.load(f)

    except Exception as e:
        print(
            f"❌ ERROR LOADING MANUAL PRICES: {e}"
        )

        return {}


# =========================
# ارز
# =========================

def get_dollar_price():
    return CURRENCY_PRICES["دلار آمریکا"]


def get_tether_price():
    return CURRENCY_PRICES["تتر"]


def get_aed_price():
    return CURRENCY_PRICES["درهم امارات"]


# =========================
# طلا
# =========================

def get_gold18_price():
    data = load_manual_prices()

    return int(
        data["gold"]["gold18"]
    )


def get_gold24_price():
    data = load_manual_prices()

    return int(
        data["gold"]["gold24"]
    )


def get_mesghal_price():
    data = load_manual_prices()

    return int(
        data["gold"]["melted"]
    )


def get_abshode_price():
    data = load_manual_prices()

    return int(
        data["gold"]["melted"]
    )


# =========================
# سکه
# =========================

def get_imami_price():
    return GOLD_PRICES["سکه امامی"]


def get_bahar_price():
    return GOLD_PRICES["سکه بهار آزادی"]


def get_nim_price():
    return GOLD_PRICES["نیم سکه"]


def get_rob_price():
    return GOLD_PRICES["ربع سکه"]


def get_gerami_price():
    return GOLD_PRICES["سکه گرمی"]


# =========================
# بازار جهانی
# =========================

def get_ounce_price():
    return GLOBAL_PRICES["اونس"]


def get_ounce_usd():
    return GLOBAL_PRICES["اونس"]


def get_ounce_toman():
    return GLOBAL_PRICES["اونس"]


def get_bitcoin_price():
    return GLOBAL_PRICES["بیت کوین"]


def get_ethereum_price():
    return GLOBAL_PRICES["اتریوم"]


# =========================

def get_all_prices():
    return {
        "currency": CURRENCY_PRICES,
        "gold": GOLD_PRICES,
        "global": GLOBAL_PRICES,
    }


def debug_navasan():
    print("✅ Manual Price Mode Enabled")