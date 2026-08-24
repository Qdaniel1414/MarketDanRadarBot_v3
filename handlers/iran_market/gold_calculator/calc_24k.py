from services.nosan_api import get_gold24_price

from handlers.iran_market.formulas.gold_formula_engine import (
    calculate_gold18,
)


def calculate_gold24(

    weight: float,

    ojrat_percent: float,

    profit_percent: float,

    tax_percent: float,

):

    price_per_gram = get_gold24_price()

    return calculate_gold18(

        weight=weight,

        price_per_gram=price_per_gram,

        ojrat_percent=ojrat_percent,

        profit_percent=profit_percent,

        tax_percent=tax_percent,

    )