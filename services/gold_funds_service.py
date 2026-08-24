import json
from pathlib import Path


DATA_FILE = Path("data/funds/gold_funds.json")


def load_gold_funds():

    with open(
        DATA_FILE,
        encoding="utf-8",
    ) as f:

        return json.load(f)


def get_gold_fund(symbol: str):

    funds = load_gold_funds()
    print("SYMBOL:", symbol)
    print("FUNDS:", funds)
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

                "daily": float(
                    fund["daily"]
                ),

                "weekly": float(
                    fund["weekly"]
                ),

                "monthly": float(
                    fund["monthly"]
                ),

                "value": int(
                    fund["value"]
                ),

            }

    return None


def get_tala():

    return get_gold_fund("TALA")


def get_ayar():

    return get_gold_fund("AYAR")


def get_gohar():

    return get_gold_fund("GOHAR")


def get_zar():

    return get_gold_fund("ZAR")


def get_kahraba():

    return get_gold_fund("KAHRABA")


def get_nafis():

    return get_gold_fund("NAFIS")


def get_javaher():

    return get_gold_fund("JAVAHER")

if __name__ == "__main__":
    print(load_gold_funds())