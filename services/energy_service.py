import requests
import re



def extract_oil_price(url, target):

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )


        html = response.text



        numbers = re.findall(
            r'\b\d+\.\d+\b',
            html
        )


        candidates = []


        for number in numbers:

            try:

                value = float(number)


                if 40 <= value <= 120:

                    candidates.append(value)


            except:

                pass



        print(
            "OIL FILTERED:",
            candidates[:30]
        )



        if candidates:

            return round(
                min(
                    candidates,
                    key=lambda x: abs(x - target)
                ),
                2
            )



    except Exception as e:

        print(
            "OIL ERROR:",
            e
        )


    return 0





def get_energy_prices():


    prices = {


        "نفت WTI":

        extract_oil_price(
            "https://www.tgju.org/profile/oil",
            70
        ),



        "نفت برنت":

        extract_oil_price(
            "https://www.tgju.org/profile/energy-brent-oil",
            85
        ),


    }



    print(
        "ENERGY RESULT:",
        prices
    )


    return prices