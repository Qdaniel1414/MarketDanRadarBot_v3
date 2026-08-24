import json
from pathlib import Path

DATA_FILE = Path("data/funds/fixed_income_funds.json")


def load_fixed_income_funds():

    with open(
        DATA_FILE,
        encoding="utf-8",
    ) as f:

        return json.load(f)


def get_fixed_income_fund(symbol: str):

    funds = load_fixed_income_funds()

    for fund in funds:

        if fund["symbol"] == symbol:

            market = int(fund["market"])

            nav = int(fund["nav"])

            bubble = market - nav

            if nav > 0:
                bubble_percent = (
                    bubble / nav
                ) * 100
            else:
                bubble_percent = 0

            return {

                "symbol": fund["symbol"],

                "name": fund["name"],

                "market": market,

                "nav": nav,

                "bubble": bubble,

                "bubble_percent": round(
                    bubble_percent,
                    2,
                ),

                "daily": float(fund["daily"]),

                "weekly": float(fund["weekly"]),

                "monthly": float(fund["monthly"]),

                "value": int(fund["value"]),

            }

    return None


def get_yak():
    return get_fixed_income_fund("YAK")


def get_kar():
    return get_fixed_income_fund("KAR")


def get_aman():
    return get_fixed_income_fund("AMAN")