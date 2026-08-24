from data.manual_prices import MANUAL_PRICES


def get_gold_prices():

    data = MANUAL_PRICES["gold"]

    return {
        "طلای 18 عیار": data["gold18"],
        "طلای 24 عیار": data["gold24"],
        "طلای آبشده": data["melted"],
        "سکه امامی": data["imami"],
        "سکه بهار آزادی": data["bahar"],
        "نیم سکه": data["nim"],
        "ربع سکه": data["rob"],
        "سکه گرمی": data["gerami"],
    }