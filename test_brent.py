import requests
import re


url = "https://www.tgju.org"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=15
)


html = r.text


for word in [
    "برنت",
    "brent",
    "Brent",
    "brent_oil"
]:

    print("\n================")
    print("SEARCH:", word)


    result = re.findall(
        r'.{0,100}' + word + r'.{0,150}',
        html,
        re.I
    )


    print(
        result[:3]
    )