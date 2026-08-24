import yfinance as yf


symbols = {
    "طلا": "GC=F",
    "نقره": "SI=F",
    "مس": "HG=F",
    "نفت WTI": "CL=F",
    "نفت برنت": "BZ=F",
    "Nasdaq 100": "^NDX",
    "Dow Jones": "^DJI",
    "S&P 500": "^GSPC",
}


for name, symbol in symbols.items():

    try:

        ticker = yf.Ticker(symbol)

        data = ticker.history(
            period="1d"
        )


        if not data.empty:

            price = data["Close"].iloc[-1]

            print(
                name,
                ":",
                round(float(price), 2)
            )

        else:

            print(
                name,
                ": DATA EMPTY"
            )


    except Exception as e:

        print(
            name,
            ": ERROR",
            e
        )