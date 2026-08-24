from data.manual_prices import MANUAL_PRICES


def get_currency_prices():
    data = MANUAL_PRICES

    return {
        "دلار آمریکا": data["currency"]["usd"],
        "تتر": data["currency"]["usdt"],
        "درهم امارات": data["currency"]["aed"],
        "یورو": data["currency"]["eur"],
        "پوند انگلیس": data["currency"]["gbp"],
        "لیر ترکیه": data["currency"]["try"],
    }