from services.nosan_api import (
    get_ounce_usd,
    get_dollar_price,
    get_imami_price,
    get_nim_price,
    get_rob_price,
    get_gerami_price,
)

COIN_WEIGHTS = {
    "imami": 8.133,
    "nim": 4.0665,
    "rob": 2.03325,
    "gerami": 1.01,
}

PURITY = 0.900
OUNCE_TO_GRAM = 31.1035


def calculate_coin_intrinsic(weight: float):

    ounce_usd = get_ounce_usd()
    dollar = get_dollar_price()

    intrinsic = (
        (ounce_usd / OUNCE_TO_GRAM)
        * dollar
        * PURITY
        * weight
    )

    return round(intrinsic)


def calc_bubble(market, intrinsic):

    bubble = market - intrinsic

    if market == 0:
        bubble_percent = 0
    else:
        bubble_percent = (bubble / market) * 100

    return bubble, round(bubble_percent, 2)


def get_imami_intrinsic():

    intrinsic = calculate_coin_intrinsic(
        COIN_WEIGHTS["imami"]
    )

    market = get_imami_price()

    bubble, bubble_percent = calc_bubble(
        market,
        intrinsic,
    )

    return {
        "weight": COIN_WEIGHTS["imami"],
        "ounce": get_ounce_usd(),
        "dollar": get_dollar_price(),
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "bubble_percent": bubble_percent,
    }

def get_nim_intrinsic():

    intrinsic = calculate_coin_intrinsic(
        COIN_WEIGHTS["nim"]
    )

    market = get_nim_price()

    bubble = market - intrinsic

    bubble_percent = (
        bubble / market * 100
    )

    return {
        "weight": COIN_WEIGHTS["nim"],
        "ounce": get_ounce_usd(),
        "dollar": get_dollar_price(),
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "bubble_percent": round(
            bubble_percent,
            2,
        ),
    }

def get_nim_intrinsic():

    intrinsic = calculate_coin_intrinsic(
        COIN_WEIGHTS["nim"]
    )

    market = get_nim_price()

    bubble = market - intrinsic

    bubble_percent = (
        bubble / market * 100
    )

    return {

        "weight": COIN_WEIGHTS["nim"],

        "ounce": get_ounce_usd(),

        "dollar": get_dollar_price(),

        "intrinsic": intrinsic,

        "market": market,

        "bubble": bubble,

        "bubble_percent": round(
            bubble_percent,
            2,
        ),
    }


def get_rob_intrinsic():

    intrinsic = calculate_coin_intrinsic(
        COIN_WEIGHTS["rob"]
    )

    market = get_rob_price()

    bubble = market - intrinsic

    bubble_percent = (
        bubble / market * 100
    )

    return {

        "weight": COIN_WEIGHTS["rob"],

        "ounce": get_ounce_usd(),

        "dollar": get_dollar_price(),

        "intrinsic": intrinsic,

        "market": market,

        "bubble": bubble,

        "bubble_percent": round(
            bubble_percent,
            2,
        ),
    }


def get_gerami_intrinsic():

    intrinsic = calculate_coin_intrinsic(
        COIN_WEIGHTS["gerami"]
    )

    market = get_gerami_price()

    bubble = market - intrinsic

    bubble_percent = (
        bubble / market * 100
    )

    return {

        "weight": COIN_WEIGHTS["gerami"],

        "ounce": get_ounce_usd(),

        "dollar": get_dollar_price(),

        "intrinsic": intrinsic,

        "market": market,

        "bubble": bubble,

        "bubble_percent": round(
            bubble_percent,
            2,
        ),
    }