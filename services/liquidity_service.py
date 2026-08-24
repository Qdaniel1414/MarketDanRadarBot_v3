import json
from pathlib import Path


DATA_FILE = Path("data/economy/liquidity.json")


def load_liquidity():

    with open(DATA_FILE, encoding="utf-8") as file:

        return json.load(file)


def intrinsic_dollar():

    data = load_liquidity()

    base_usd = float(data["base_usd"])

    base_liquidity = float(data["base_liquidity"])

    current_liquidity = float(data["current_liquidity"])

    alpha = float(data["alpha"])

    usd = base_usd * (

        current_liquidity / base_liquidity

    ) ** alpha

    return {

        "base_year": data["base_year"],

        "base_usd": base_usd,

        "base_liquidity": base_liquidity,

        "current_liquidity": current_liquidity,

        "alpha": alpha,

        "intrinsic_usd": round(usd),

    }