from services.provider_currency import get_currency_prices
from services.provider_gold import get_gold_prices
from services.provider_crypto import get_crypto_prices


def get_all_market_prices():

    return {
        "currency": get_currency_prices(),
        "gold": get_gold_prices(),
        "crypto": get_crypto_prices(),
    }