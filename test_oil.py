import requests
import re


url = "https://www.tgju.org/profile/oil"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=15
)


html = r.text


patterns = [

    r'chartData(.*?)\]',
    r'series(.*?)\]',
    r'\[.*?\]',
    r'107500',
    r'chart',
    r'api',

]


for p in patterns:

    print("\n================")
    print("PATTERN:", p)


    result = re.findall(
        p,
        html,
        re.S
    )


    if result:

        print(
            result[:2]
        )

    else:

        print("NOT FOUND")