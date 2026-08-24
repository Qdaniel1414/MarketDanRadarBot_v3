import requests


def get_crypto_prices():

    coins = {
        "Bitcoin BTC": "bitcoin",
        "Ethereum ETH": "ethereum",
        "BNB": "binancecoin",
        "Solana SOL": "solana",
        "Zcash ZEC": "zcash",
        "Dogecoin DOGE": "dogecoin",
        "Monero XMR": "monero",
        "Chainlink LINK": "chainlink",
        "Avalanche AVAX": "avalanche-2",
        "NEAR": "near",
        "Tether Gold XAUT": "tether-gold",
        "PAX Gold PAXG": "pax-gold",
        "Bittensor TAO": "bittensor",
        "Aave AAVE": "aave",
        "Render RENDER": "render-token",
        "Compound COMP": "compound-governance-token",
        "Arweave AR": "arweave",
        "Injective INJ": "injective-protocol",
        "MultiversX EGLD": "elrond-erd-2",
    }


    try:

        ids = ",".join(coins.values())


        url = (
            "https://api.coingecko.com/api/v3/simple/price"
            f"?ids={ids}&vs_currencies=usd"
        )


        response = requests.get(
            url,
            timeout=15,
        )


        data = response.json()


        prices = {}


        for name, coin_id in coins.items():

            if coin_id in data:

                prices[name] = data[coin_id]["usd"]


        return prices


    except Exception as e:

        print(
            "Crypto API Error:",
            e,
        )

        return {}