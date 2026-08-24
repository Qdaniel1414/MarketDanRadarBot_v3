from services.liquidity_service import intrinsic_dollar
from services.inflation_service import get_theoretical_dollar

from services.nosan_api import (
    get_gold18_price,
    get_ounce_usd,
)

# وزن هر مدل
WEIGHT_LIQUIDITY = 0.40
WEIGHT_GOLD = 0.35
WEIGHT_INFLATION = 0.25


def gold_theoretical_dollar():
    """
    ارزش ذاتی دلار بر اساس طلای ۱۸ عیار
    """

    gold18 = get_gold18_price()

    ounce_usd = get_ounce_usd()

    # تبدیل قیمت طلای ۱۸ عیار به طلای خالص
    pure_gold_price = gold18 / 0.75

    # قیمت هر گرم طلای خالص جهانی
    world_gold_per_gram = ounce_usd / 31.1035

    return pure_gold_price / world_gold_per_gram


def get_final_dollar_valuation():
    """
    ارزش ذاتی نهایی دلار
    """

    liquidity_value = intrinsic_dollar()["intrinsic_usd"]

    inflation_value = get_theoretical_dollar()

    gold_value = gold_theoretical_dollar()

    final_value = (
        liquidity_value * WEIGHT_LIQUIDITY
        + gold_value * WEIGHT_GOLD
        + inflation_value * WEIGHT_INFLATION
    )

    return {
        "gold": round(gold_value),
        "liquidity": round(liquidity_value),
        "inflation": round(inflation_value),
        "final": round(final_value),
    }