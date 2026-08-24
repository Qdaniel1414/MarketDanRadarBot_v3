import json

PRICE_FILE = "data/manual_prices.json"


def load_prices():
    with open(PRICE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_price(key):
    prices = load_prices()
    return prices.get(key)