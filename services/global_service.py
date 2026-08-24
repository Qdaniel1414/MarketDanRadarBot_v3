import yfinance as yf



def get_yahoo_price(symbol):

    try:

        ticker = yf.Ticker(symbol)

        data = ticker.history(
            period="1d"
        )


        if data.empty:

            return 0


        price = data["Close"].iloc[-1]


        return round(
            float(price),
            2
        )


    except Exception as e:

        print(
            "YAHOO ERROR:",
            symbol,
            e
        )

        return 0




def get_global_prices():


    prices = {


        "انس جهانی طلا":

            get_yahoo_price(
                "GC=F"
            ),


        "انس نقره":

            get_yahoo_price(
                "SI=F"
            ),


        "مس جهانی":

            get_yahoo_price(
                "HG=F"
            ),


        "نفت WTI":

            get_yahoo_price(
                "CL=F"
            ),


        "نفت برنت":

            get_yahoo_price(
                "BZ=F"
            ),


        "Nasdaq 100":

            get_yahoo_price(
                "^NDX"
            ),


        "Dow Jones":

            get_yahoo_price(
                "^DJI"
            ),


        "S&P 500":

            get_yahoo_price(
                "^GSPC"
            ),


    }



    print(
        "GLOBAL RESULT:",
        prices
    )


    return prices