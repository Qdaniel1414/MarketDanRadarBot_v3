import requests
import re


url = "https://www.tgju.org/"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    }
)


text = r.text.lower()


keywords = [
    "s&p",
    "500",
    "داوجونز",
    "dow",
    "dxy",
    "شاخص دلار",
]


for k in keywords:

    print("\n================")
    print("SEARCH:", k)


    index = text.find(
        k.lower()
    )


    if index != -1:

        print(
            r.text[index-200:index+300]
        )

    else:

        print(
            "NOT FOUND"
        )