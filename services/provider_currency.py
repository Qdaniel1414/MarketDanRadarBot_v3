import json
from pathlib import Path


PRICE_FILE = Path("data/manual_prices.json")


def load_prices():

    with open(
        PRICE_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def get_currency_prices():

    prices = load_prices()

    currency = prices.get(
        "currency",
        {}
    )

    return {
        "دلار آمریکا": currency.get("usd", 0),
        "تتر": currency.get("usdt", 0),
        "درهم": currency.get("aed", 0),
        "یورو": currency.get("eur", 0),
        "پوند": currency.get("gbp", 0),
        "لیر": currency.get("try", 0),
    }