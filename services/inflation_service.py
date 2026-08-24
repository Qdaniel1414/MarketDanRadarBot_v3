import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "economy" / "inflation.json"


def load_inflation_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_base_year():
    return load_inflation_data()["base_year"]


def get_base_usd():
    return load_inflation_data()["base_usd"]


def get_iran_cumulative():
    return load_inflation_data()["iran_cumulative"]


def get_usa_cumulative():
    return load_inflation_data()["usa_cumulative"]


def get_inflation_difference():
    return get_iran_cumulative() - get_usa_cumulative()


def get_theoretical_dollar():
    """
    ارزش نظری دلار بر اساس اختلاف تورم تجمعی
    """

    base = get_base_usd()

    iran = get_iran_cumulative()

    usa = get_usa_cumulative()

    return int(base * ((100 + iran) / (100 + usa)))