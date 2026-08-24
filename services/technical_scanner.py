import yfinance as yf
def get_btc_data():
    """
    دریافت داده‌های Bitcoin از Yahoo Finance
    """
    ticker = yf.Ticker("BTC-USD")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Bitcoin دریافت نشد.")

    return data

def calculate_btc_indicators(data):
    """
    محاسبه اندیکاتورهای پایه تکنیکال Bitcoin
    """

    close = data["Close"]

    # ============================================================
    # EMA
    # ============================================================

    ema20 = close.ewm(span=20, adjust=False).mean()
    ema50 = close.ewm(span=50, adjust=False).mean()

    # ============================================================
    # SMA
    # ============================================================

    sma20 = close.rolling(window=20).mean()
    sma50 = close.rolling(window=50).mean()

    # ============================================================
    # RSI 14
    # ============================================================

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    rsi14 = 100 - (100 / (1 + rs))

    # ============================================================
    # MACD
    # ============================================================

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26

    macd_signal = macd.ewm(
        span=9,
        adjust=False,
    ).mean()

    macd_histogram = macd - macd_signal

    # ============================================================
    # ساخت DataFrame نهایی
    # ============================================================

    result = data.copy()

    result["EMA20"] = ema20
    result["EMA50"] = ema50

    result["SMA20"] = sma20
    result["SMA50"] = sma50

    result["RSI14"] = rsi14

    result["MACD"] = macd
    result["MACD_SIGNAL"] = macd_signal
    result["MACD_HISTOGRAM"] = macd_histogram

    return result



def get_btc_signal(data):
    """
    تولید سیگنال تکنیکال Bitcoin
    """

    last = data.iloc[-1]

    close = float(last["Close"])
    ema20 = float(last["EMA20"])
    ema50 = float(last["EMA50"])
    rsi14 = float(last["RSI14"])

    macd = float(last["MACD"])
    macd_signal = float(last["MACD_SIGNAL"])
    macd_histogram = float(last["MACD_HISTOGRAM"])

    # ============================================================
    # تشخیص روند
    # ============================================================

    if close > ema20 > ema50:
        trend = "🟢 صعودی"

    elif close < ema20 < ema50:
        trend = "🔴 نزولی"

    else:
        trend = "🟡 خنثی"

    # ============================================================
    # وضعیت RSI
    # ============================================================

    if rsi14 >= 70:
        rsi_status = "⚠️ اشباع خرید"

    elif rsi14 <= 30:
        rsi_status = "🟢 اشباع فروش"

    else:
        rsi_status = "🟡 نرمال"

    # ============================================================
    # وضعیت MACD
    # ============================================================

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"

    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"

    else:
        macd_status = "🟡 خنثی"

    # ============================================================
    # جمع‌بندی
    # ============================================================

    bullish_conditions = 0
    bearish_conditions = 0

    # روند
    if trend == "🟢 صعودی":
        bullish_conditions += 1

    elif trend == "🔴 نزولی":
        bearish_conditions += 1

    # MACD
    if macd_status == "🟢 صعودی":
        bullish_conditions += 1

    elif macd_status == "🔴 نزولی":
        bearish_conditions += 1

    # RSI
    if 30 < rsi14 < 70:
        if rsi14 > 50:
            bullish_conditions += 1
        else:
            bearish_conditions += 1

    # ============================================================
    # تعیین سیگنال نهایی
    # ============================================================

    if bullish_conditions >= 2 and rsi14 < 70:
        signal = "🟢 تمایل صعودی"

    elif bearish_conditions >= 2 and rsi14 > 30:
        signal = "🔴 تمایل نزولی"

    elif bullish_conditions >= 2 and rsi14 >= 70:
        signal = "⚠️ صعودی اما در اشباع خرید"

    elif bearish_conditions >= 2 and rsi14 <= 30:
        signal = "⚠️ نزولی اما در اشباع فروش"

    else:
        signal = "🟡 احتیاط / خنثی"

    return {
        "price": close,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "macd_status": macd_status,
        "signal": signal,
    }


def format_btc_report(signal):
    """
    تبدیل نتیجه اسکن Bitcoin به گزارش فارسی
    """

    price = signal["price"]

    ema20 = signal["ema20"]
    ema50 = signal["ema50"]

    rsi14 = signal["rsi14"]

    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]

    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال Bitcoin\n\n"

        f"💰 قیمت فعلی: ${price:,.2f}\n\n"

        "📊 اندیکاتورها:\n"
        f"• EMA20: ${ema20:,.2f}\n"
        f"• EMA50: ${ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.2f}\n"
        f"• MACD Signal: {macd_signal:.2f}\n"
        f"• MACD Histogram: {macd_histogram:.2f}\n\n"

        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"

        f"🎯 جمع‌بندی: {final_signal}\n\n"

        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

# ============================================================
# Ethereum Scanner
# ============================================================

def get_eth_data():
    """
    دریافت داده‌های یک‌ساعته Ethereum از Yahoo Finance
    """

    ticker = yf.Ticker("ETH-USD")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Ethereum دریافت نشد.")

    return data


def calculate_eth_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Ethereum
    """

    close = data["Close"]

    # ============================================================
    # EMA
    # ============================================================

    ema20 = close.ewm(span=20, adjust=False).mean()
    ema50 = close.ewm(span=50, adjust=False).mean()

    # ============================================================
    # SMA
    # ============================================================

    sma20 = close.rolling(window=20).mean()
    sma50 = close.rolling(window=50).mean()

    # ============================================================
    # RSI 14
    # ============================================================

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    rsi14 = 100 - (100 / (1 + rs))

    # ============================================================
    # MACD
    # ============================================================

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26

    macd_signal = macd.ewm(
        span=9,
        adjust=False,
    ).mean()

    macd_histogram = macd - macd_signal

    # ============================================================
    # ساخت DataFrame نهایی
    # ============================================================

    result = data.copy()

    result["EMA20"] = ema20
    result["EMA50"] = ema50

    result["SMA20"] = sma20
    result["SMA50"] = sma50

    result["RSI14"] = rsi14

    result["MACD"] = macd
    result["MACD_SIGNAL"] = macd_signal
    result["MACD_HISTOGRAM"] = macd_histogram

    return result

def get_eth_signal(data):
    """
    تولید سیگنال تکنیکال Ethereum
    """

    last = data.iloc[-1]

    close = float(last["Close"])
    ema20 = float(last["EMA20"])
    ema50 = float(last["EMA50"])
    rsi14 = float(last["RSI14"])

    macd = float(last["MACD"])
    macd_signal = float(last["MACD_SIGNAL"])
    macd_histogram = float(last["MACD_HISTOGRAM"])

    # ============================================================
    # تشخیص روند
    # ============================================================

    if close > ema20 > ema50:
        trend = "🟢 صعودی"

    elif close < ema20 < ema50:
        trend = "🔴 نزولی"

    else:
        trend = "🟡 خنثی"

    # ============================================================
    # وضعیت RSI
    # ============================================================

    if rsi14 >= 70:
        rsi_status = "⚠️ اشباع خرید"

    elif rsi14 <= 30:
        rsi_status = "🟢 اشباع فروش"

    else:
        rsi_status = "🟡 نرمال"

    # ============================================================
    # وضعیت MACD
    # ============================================================

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"

    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"

    else:
        macd_status = "🟡 خنثی"

    # ============================================================
    # شمارش شرایط صعودی و نزولی
    # ============================================================

    bullish_conditions = 0
    bearish_conditions = 0

    # روند
    if trend == "🟢 صعودی":
        bullish_conditions += 1

    elif trend == "🔴 نزولی":
        bearish_conditions += 1

    # MACD
    if macd_status == "🟢 صعودی":
        bullish_conditions += 1

    elif macd_status == "🔴 نزولی":
        bearish_conditions += 1

    # RSI
    if 30 < rsi14 < 70:

        if rsi14 > 50:
            bullish_conditions += 1

        else:
            bearish_conditions += 1

    # ============================================================
    # سیگنال نهایی
    # ============================================================

    if bullish_conditions >= 2 and rsi14 < 70:
        signal = "🟢 تمایل صعودی"

    elif bearish_conditions >= 2 and rsi14 > 30:
        signal = "🔴 تمایل نزولی"

    elif bullish_conditions >= 2 and rsi14 >= 70:
        signal = "⚠️ صعودی اما در اشباع خرید"

    elif bearish_conditions >= 2 and rsi14 <= 30:
        signal = "⚠️ نزولی اما در اشباع فروش"

    else:
        signal = "🟡 احتیاط / خنثی"

    return {
        "price": close,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "rsi_status": rsi_status,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "macd_status": macd_status,
        "trend": trend,
        "signal": signal,
    }

def format_eth_report(signal):
    """
    تبدیل نتیجه اسکن Ethereum به گزارش فارسی
    """

    price = signal["price"]

    ema20 = signal["ema20"]
    ema50 = signal["ema50"]

    rsi14 = signal["rsi14"]

    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]

    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال Ethereum\n\n"

        f"💰 قیمت فعلی: ${price:,.2f}\n\n"

        "📊 اندیکاتورها:\n"
        f"• EMA20: ${ema20:,.2f}\n"
        f"• EMA50: ${ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.2f}\n"
        f"• MACD Signal: {macd_signal:.2f}\n"
        f"• MACD Histogram: {macd_histogram:.2f}\n\n"

        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"

        f"🎯 جمع‌بندی: {final_signal}\n\n"

        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

# ============================================================
# Gold Scanner
# ============================================================

def get_gold_data():
    """
    دریافت داده‌های یک‌ساعته Gold از Yahoo Finance
    نماد GC=F مربوط به قرارداد آتی طلا است.
    """

    ticker = yf.Ticker("GC=F")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Gold دریافت نشد.")

    return data


def calculate_gold_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Gold
    """

    close = data["Close"]

    # ============================================================
    # EMA
    # ============================================================

    ema20 = close.ewm(span=20, adjust=False).mean()
    ema50 = close.ewm(span=50, adjust=False).mean()

    # ============================================================
    # SMA
    # ============================================================

    sma20 = close.rolling(window=20).mean()
    sma50 = close.rolling(window=50).mean()

    # ============================================================
    # RSI 14
    # ============================================================

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    rsi14 = 100 - (100 / (1 + rs))

    # ============================================================
    # MACD
    # ============================================================

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26

    macd_signal = macd.ewm(
        span=9,
        adjust=False,
    ).mean()

    macd_histogram = macd - macd_signal

    # ============================================================
    # ساخت DataFrame نهایی
    # ============================================================

    result = data.copy()

    result["EMA20"] = ema20
    result["EMA50"] = ema50

    result["SMA20"] = sma20
    result["SMA50"] = sma50

    result["RSI14"] = rsi14

    result["MACD"] = macd
    result["MACD_SIGNAL"] = macd_signal
    result["MACD_HISTOGRAM"] = macd_histogram

    return result

def get_gold_signal(data):
    """
    تولید سیگنال تکنیکال Gold
    """

    last = data.iloc[-1]

    close = float(last["Close"])
    ema20 = float(last["EMA20"])
    ema50 = float(last["EMA50"])
    rsi14 = float(last["RSI14"])

    macd = float(last["MACD"])
    macd_signal = float(last["MACD_SIGNAL"])
    macd_histogram = float(last["MACD_HISTOGRAM"])

    # ============================================================
    # تشخیص روند
    # ============================================================

    if close > ema20 > ema50:
        trend = "🟢 صعودی"

    elif close < ema20 < ema50:
        trend = "🔴 نزولی"

    else:
        trend = "🟡 خنثی"

    # ============================================================
    # وضعیت RSI
    # ============================================================

    if rsi14 >= 70:
        rsi_status = "⚠️ اشباع خرید"

    elif rsi14 <= 30:
        rsi_status = "🟢 اشباع فروش"

    else:
        rsi_status = "🟡 نرمال"

    # ============================================================
    # وضعیت MACD
    # ============================================================

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"

    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"

    else:
        macd_status = "🟡 خنثی"

    # ============================================================
    # شمارش شرایط صعودی و نزولی
    # ============================================================

    bullish_conditions = 0
    bearish_conditions = 0

    # روند
    if trend == "🟢 صعودی":
        bullish_conditions += 1

    elif trend == "🔴 نزولی":
        bearish_conditions += 1

    # MACD
    if macd_status == "🟢 صعودی":
        bullish_conditions += 1

    elif macd_status == "🔴 نزولی":
        bearish_conditions += 1

    # RSI
    if 30 < rsi14 < 70:

        if rsi14 > 50:
            bullish_conditions += 1

        else:
            bearish_conditions += 1

    # ============================================================
    # سیگنال نهایی
    # ============================================================

    if bullish_conditions >= 2 and rsi14 < 70:
        signal = "🟢 تمایل صعودی"

    elif bearish_conditions >= 2 and rsi14 > 30:
        signal = "🔴 تمایل نزولی"

    elif bullish_conditions >= 2 and rsi14 >= 70:
        signal = "⚠️ صعودی اما در اشباع خرید"

    elif bearish_conditions >= 2 and rsi14 <= 30:
        signal = "⚠️ نزولی اما در اشباع فروش"

    else:
        signal = "🟡 احتیاط / خنثی"

    return {
        "price": close,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "rsi_status": rsi_status,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "macd_status": macd_status,
        "trend": trend,
        "signal": signal,
    }

def format_gold_report(signal):
    """
    تبدیل نتیجه اسکن Gold به گزارش فارسی
    """

    price = signal["price"]

    ema20 = signal["ema20"]
    ema50 = signal["ema50"]

    rsi14 = signal["rsi14"]

    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]

    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال Gold\n\n"

        f"💰 قیمت فعلی: ${price:,.2f}\n\n"

        "📊 اندیکاتورها:\n"
        f"• EMA20: ${ema20:,.2f}\n"
        f"• EMA50: ${ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.2f}\n"
        f"• MACD Signal: {macd_signal:.2f}\n"
        f"• MACD Histogram: {macd_histogram:.2f}\n\n"

        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"

        f"🎯 جمع‌بندی: {final_signal}\n\n"

        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

def get_dxy_data():
    """
    دریافت داده‌های شاخص دلار آمریکا (DXY)
    """

    ticker = yf.Ticker("DX-Y.NYB")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای DXY دریافت نشد.")

    return data

def calculate_dxy_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال DXY
    """

    data = data.copy()

    data["EMA20"] = data["Close"].ewm(span=20, adjust=False).mean()
    data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()

    data["SMA20"] = data["Close"].rolling(window=20).mean()
    data["SMA50"] = data["Close"].rolling(window=50).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()

    data["MACD"] = ema12 - ema26
    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False,
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_dxy_signal(data):
    """
    تحلیل تکنیکال DXY و تولید سیگنال نهایی
    """

    last = data.iloc[-1]

    price = last["Close"]
    ema20 = last["EMA20"]
    ema50 = last["EMA50"]
    rsi14 = last["RSI14"]

    macd = last["MACD"]
    macd_signal = last["MACD_Signal"]
    macd_histogram = last["MACD_Histogram"]

    # تشخیص روند
    if price > ema20 and ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 and ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # وضعیت RSI
    if rsi14 >= 70:
        rsi_status = "⚠️ اشباع خرید"
    elif rsi14 <= 30:
        rsi_status = "⚠️ اشباع فروش"
    else:
        rsi_status = "🟡 نرمال"

    # وضعیت MACD
    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"
    else:
        macd_status = "🟡 خنثی"

    # امتیازدهی
    bullish_conditions = 0
    bearish_conditions = 0

    if price > ema20:
        bullish_conditions += 1
    elif price < ema20:
        bearish_conditions += 1

    if ema20 > ema50:
        bullish_conditions += 1
    elif ema20 < ema50:
        bearish_conditions += 1

    if macd > macd_signal:
        bullish_conditions += 1
    elif macd < macd_signal:
        bearish_conditions += 1

    # سیگنال نهایی
    if bullish_conditions >= 2 and rsi14 < 70:
        final_signal = "🟢 صعودی"
    elif bearish_conditions >= 2 and rsi14 > 30:
        final_signal = "🔴 نزولی"
    elif bullish_conditions >= 2 and rsi14 >= 70:
        final_signal = "⚠️ صعودی اما در اشباع خرید"
    elif bearish_conditions >= 2 and rsi14 <= 30:
        final_signal = "⚠️ نزولی اما در اشباع فروش"
    else:
        final_signal = "🟡 خنثی"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "signal": final_signal,
    }
def format_dxy_report(signal):
    """
    تبدیل نتیجه اسکن DXY به گزارش فارسی
    """

    price = signal["price"]

    ema20 = signal["ema20"]
    ema50 = signal["ema50"]

    rsi14 = signal["rsi14"]

    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]

    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال DXY\n\n"

        f"💵 شاخص دلار آمریکا: {price:,.3f}\n\n"

        "📊 اندیکاتورها:\n"
        f"• EMA20: {ema20:,.3f}\n"
        f"• EMA50: {ema50:,.3f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.4f}\n"
        f"• MACD Signal: {macd_signal:.4f}\n"
        f"• MACD Histogram: {macd_histogram:.4f}\n\n"

        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"

        f"🎯 جمع‌بندی: {final_signal}\n\n"

        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

def get_sp500_data():
    """
    دریافت داده‌های شاخص S&P 500
    """

    ticker = yf.Ticker("^GSPC")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای S&P 500 دریافت نشد.")

    return data

def calculate_sp500_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال S&P 500
    """

    data = data.copy()

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False,
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False,
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False,
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False,
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False,
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_sp500_signal(data):
    """
    تحلیل تکنیکال S&P 500 و تولید سیگنال نهایی
    """

    last = data.iloc[-1]

    price = last["Close"]
    ema20 = last["EMA20"]
    ema50 = last["EMA50"]
    rsi14 = last["RSI14"]

    macd = last["MACD"]
    macd_signal = last["MACD_Signal"]
    macd_histogram = last["MACD_Histogram"]

    # تشخیص روند
    if price > ema20 and ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 and ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # وضعیت RSI
    if rsi14 >= 70:
        rsi_status = "⚠️ اشباع خرید"
    elif rsi14 <= 30:
        rsi_status = "⚠️ اشباع فروش"
    else:
        rsi_status = "🟡 نرمال"

    # وضعیت MACD
    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"
    else:
        macd_status = "🟡 خنثی"

    # امتیازدهی
    bullish_conditions = 0
    bearish_conditions = 0

    if price > ema20:
        bullish_conditions += 1
    elif price < ema20:
        bearish_conditions += 1

    if ema20 > ema50:
        bullish_conditions += 1
    elif ema20 < ema50:
        bearish_conditions += 1

    if macd > macd_signal:
        bullish_conditions += 1
    elif macd < macd_signal:
        bearish_conditions += 1

    # سیگنال نهایی
    if bullish_conditions >= 2 and rsi14 < 70:
        final_signal = "🟢 صعودی"
    elif bearish_conditions >= 2 and rsi14 > 30:
        final_signal = "🔴 نزولی"
    elif bullish_conditions >= 2 and rsi14 >= 70:
        final_signal = "⚠️ صعودی اما در اشباع خرید"
    elif bearish_conditions >= 2 and rsi14 <= 30:
        final_signal = "⚠️ نزولی اما در اشباع فروش"
    else:
        final_signal = "🟡 خنثی"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "signal": final_signal,
    }

def format_sp500_report(signal):
    """
    تبدیل نتیجه اسکن S&P 500 به گزارش فارسی
    """

    price = signal["price"]
    ema20 = signal["ema20"]
    ema50 = signal["ema50"]
    rsi14 = signal["rsi14"]
    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]
    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال S&P 500\n\n"
        f"📊 قیمت فعلی: {price:,.2f}\n\n"
        "📊 اندیکاتورها:\n"
        f"• EMA20: {ema20:,.2f}\n"
        f"• EMA50: {ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.2f}\n"
        f"• MACD Signal: {macd_signal:.2f}\n"
        f"• MACD Histogram: {macd_histogram:.2f}\n\n"
        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"
        f"🎯 جمع‌بندی: {final_signal}\n\n"
        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

def get_nasdaq_data():
    """
    دریافت داده‌های شاخص Nasdaq
    """

    ticker = yf.Ticker("^IXIC")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Nasdaq دریافت نشد.")

    return data

def calculate_nasdaq_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Nasdaq
    """

    data = data.copy()

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False,
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False,
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False,
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False,
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False,
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_nasdaq_signal(data):
    """
    تحلیل تکنیکال Nasdaq و تولید سیگنال نهایی
    """

    last = data.iloc[-1]

    price = last["Close"]
    ema20 = last["EMA20"]
    ema50 = last["EMA50"]
    rsi14 = last["RSI14"]

    macd = last["MACD"]
    macd_signal = last["MACD_Signal"]
    macd_histogram = last["MACD_Histogram"]

    # تشخیص روند
    if price > ema20 and ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 and ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # وضعیت RSI
    if rsi14 >= 70:
        rsi_status = "⚠️ اشباع خرید"
    elif rsi14 <= 30:
        rsi_status = "⚠️ اشباع فروش"
    else:
        rsi_status = "🟡 نرمال"

    # وضعیت MACD
    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"
    else:
        macd_status = "🟡 خنثی"

    # امتیازدهی
    bullish_conditions = 0
    bearish_conditions = 0

    if price > ema20:
        bullish_conditions += 1
    elif price < ema20:
        bearish_conditions += 1

    if ema20 > ema50:
        bullish_conditions += 1
    elif ema20 < ema50:
        bearish_conditions += 1

    if macd > macd_signal:
        bullish_conditions += 1
    elif macd < macd_signal:
        bearish_conditions += 1

    # سیگنال نهایی
    if bullish_conditions >= 2 and rsi14 < 70:
        final_signal = "🟢 صعودی"
    elif bearish_conditions >= 2 and rsi14 > 30:
        final_signal = "🔴 نزولی"
    elif bullish_conditions >= 2 and rsi14 >= 70:
        final_signal = "⚠️ صعودی اما در اشباع خرید"
    elif bearish_conditions >= 2 and rsi14 <= 30:
        final_signal = "⚠️ نزولی اما در اشباع فروش"
    else:
        final_signal = "🟡 خنثی"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "signal": final_signal,
    }

def format_nasdaq_report(signal):
    """
    تبدیل نتیجه اسکن Nasdaq به گزارش فارسی
    """

    price = signal["price"]
    ema20 = signal["ema20"]
    ema50 = signal["ema50"]
    rsi14 = signal["rsi14"]
    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]
    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال Nasdaq\n\n"
        f"💻 قیمت فعلی: {price:,.2f}\n\n"
        "📊 اندیکاتورها:\n"
        f"• EMA20: {ema20:,.2f}\n"
        f"• EMA50: {ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.2f}\n"
        f"• MACD Signal: {macd_signal:.2f}\n"
        f"• MACD Histogram: {macd_histogram:.2f}\n\n"
        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"
        f"🎯 جمع‌بندی: {final_signal}\n\n"
        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

def get_dow_data():
    """
    دریافت داده‌های شاخص Dow Jones
    """

    ticker = yf.Ticker("^DJI")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Dow Jones دریافت نشد.")

    return data

def calculate_dow_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Dow Jones
    """

    data = data.copy()

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False,
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False,
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False,
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False,
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False,
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_dow_signal(data):
    """
    تحلیل سیگنال تکنیکال Dow Jones
    """

    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]
    rsi14 = latest["RSI14"]
    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    # روند
    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # وضعیت RSI
    if rsi14 >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi14 <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 نرمال"

    # وضعیت MACD
    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 نزولی"
    else:
        macd_status = "🟡 خنثی"

    # امتیازدهی
    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    # سیگنال نهایی
    if score >= 2 and rsi14 < 70:
        signal = "🟢 صعودی"
    elif score >= 2 and rsi14 > 30:
        signal = "🔴 نزولی"
    elif score >= 2 and rsi14 >= 70:
        signal = "🟢 صعودی — اشباع خرید"
    elif score >= 2 and rsi14 <= 30:
        signal = "🔴 نزولی — اشباع فروش"
    else:
        signal = "🟡 خنثی"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "signal": signal,
    }

def format_dow_report(signal):
    """
    تبدیل نتیجه اسکن Dow Jones به گزارش فارسی
    """

    price = signal["price"]
    ema20 = signal["ema20"]
    ema50 = signal["ema50"]
    rsi14 = signal["rsi14"]
    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]
    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال Dow Jones\n\n"
        f"🏦 قیمت فعلی: {price:,.2f}\n\n"
        "📊 اندیکاتورها:\n"
        f"• EMA20: {ema20:,.2f}\n"
        f"• EMA50: {ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.2f}\n"
        f"• MACD Signal: {macd_signal:.2f}\n"
        f"• MACD Histogram: {macd_histogram:.2f}\n\n"
        f"📈 روند: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"
        f"🎯 جمع‌بندی: {final_signal}\n\n"
        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

def get_vix_data():
    """
    دریافت داده‌های شاخص VIX
    """

    ticker = yf.Ticker("^VIX")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای VIX دریافت نشد.")

    return data

def calculate_vix_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال VIX
    """

    data["EMA20"] = data["Close"].ewm(span=20, adjust=False).mean()
    data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()

    data["SMA20"] = data["Close"].rolling(window=20).mean()
    data["SMA50"] = data["Close"].rolling(window=50).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()

    data["MACD"] = ema12 - ema26
    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_vix_signal(data):
    """
    تحلیل تکنیکال شاخص VIX
    """

    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]
    rsi14 = latest["RSI14"]
    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    # روند VIX
    if price > ema20 > ema50:
        trend = "🔴 صعودی / افزایش ترس بازار"

    elif price < ema20 < ema50:
        trend = "🟢 نزولی / کاهش ترس بازار"

    else:
        trend = "🟡 خنثی"

    # وضعیت RSI
    if rsi14 >= 70:
        rsi_status = "🔴 اشباع خرید / ترس بالا"

    elif rsi14 <= 30:
        rsi_status = "🟢 اشباع فروش / آرامش بیشتر"

    else:
        rsi_status = "🟡 نرمال"

    # وضعیت MACD
    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🔴 مومنتوم صعودی VIX"

    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🟢 مومنتوم نزولی VIX"

    else:
        macd_status = "🟡 خنثی"

    # امتیاز کلی
    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        signal = "🔴 افزایش ریسک و ترس بازار"

    elif score == 0:
        signal = "🟢 کاهش ریسک و آرامش بازار"

    else:
        signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "signal": signal,
    }

def format_vix_report(signal):
    """
    تبدیل نتیجه اسکن VIX به گزارش فارسی
    """

    price = signal["price"]
    ema20 = signal["ema20"]
    ema50 = signal["ema50"]
    rsi14 = signal["rsi14"]
    macd = signal["macd"]
    macd_signal = signal["macd_signal"]
    macd_histogram = signal["macd_histogram"]

    trend = signal["trend"]
    rsi_status = signal["rsi_status"]
    macd_status = signal["macd_status"]
    final_signal = signal["signal"]

    report = (
        "📉 اسکن تکنیکال VIX\n\n"
        f"📊 مقدار فعلی VIX: {price:,.2f}\n\n"

        "📈 اندیکاتورها:\n"
        f"• EMA20: {ema20:,.2f}\n"
        f"• EMA50: {ema50:,.2f}\n"
        f"• RSI14: {rsi14:.2f}\n"
        f"• MACD: {macd:.4f}\n"
        f"• MACD Signal: {macd_signal:.4f}\n"
        f"• MACD Histogram: {macd_histogram:.4f}\n\n"

        f"📈 روند VIX: {trend}\n"
        f"📊 وضعیت RSI: {rsi_status}\n"
        f"📉 وضعیت MACD: {macd_status}\n\n"

        f"🎯 جمع‌بندی: {final_signal}\n\n"

        "💡 VIX یکی از مهم‌ترین شاخص‌های سنجش ترس و نوسان "
        "انتظاری بازار سهام آمریکاست.\n\n"

        "⚠️ این گزارش صرفاً تحلیل تکنیکال است و توصیه خرید یا فروش نیست."
    )

    return report

def get_nvda_data():
    """
    دریافت داده‌های Nvidia از Yahoo Finance
    """

    ticker = yf.Ticker("NVDA")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Nvidia دریافت نشد.")

    return data

def calculate_nvda_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Nvidia
    """

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_nvda_signal(data):
    """
    تولید سیگنال تکنیکال Nvidia
    """

    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]

    rsi = latest["RSI14"]

    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    # -------------------------
    # روند
    # -------------------------

    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # -------------------------
    # RSI
    # -------------------------

    if rsi >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 ناحیه نرمال"

    # -------------------------
    # MACD
    # -------------------------

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 مومنتوم صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 مومنتوم نزولی"
    else:
        macd_status = "🟡 مومنتوم خنثی"

    # -------------------------
    # امتیاز نهایی
    # -------------------------

    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        final_signal = "🟢 تمایل صعودی"
    elif score == 0:
        final_signal = "🔴 تمایل نزولی"
    else:
        final_signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "final_signal": final_signal,
    }

def format_nvda_report(signal):
    """
    ساخت گزارش فارسی تحلیل تکنیکال Nvidia
    """

    return (
        "🟢 تحلیل تکنیکال Nvidia (NVDA)\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💰 قیمت فعلی: {signal['price']:.2f} دلار\n\n"

        "📊 میانگین‌های متحرک\n"
        f"EMA20: {signal['ema20']:.2f}\n"
        f"EMA50: {signal['ema50']:.2f}\n"
        f"روند: {signal['trend']}\n\n"

        "📈 RSI14\n"
        f"RSI: {signal['rsi']:.2f}\n"
        f"وضعیت: {signal['rsi_status']}\n\n"

        "📉 MACD\n"
        f"MACD: {signal['macd']:.2f}\n"
        f"Signal: {signal['macd_signal']:.2f}\n"
        f"Histogram: {signal['macd_histogram']:.2f}\n"
        f"وضعیت: {signal['macd_status']}\n\n"

        "🎯 سیگنال نهایی\n"
        f"{signal['final_signal']}\n\n"

        "⚠️ توجه:\n"
        "این تحلیل صرفاً بر اساس داده‌های تکنیکال و برای اهداف آموزشی "
        "ارائه شده و به‌تنهایی توصیه خرید یا فروش نیست."
    )

def get_aapl_data():
    """
    دریافت داده‌های Apple از Yahoo Finance
    """

    ticker = yf.Ticker("AAPL")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Apple دریافت نشد.")

    return data

def calculate_aapl_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Apple
    """

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_aapl_signal(data):
    """
    تولید سیگنال تکنیکال Apple
    """

    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]

    rsi = latest["RSI14"]

    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    # -------------------------
    # روند
    # -------------------------

    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # -------------------------
    # RSI
    # -------------------------

    if rsi >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 ناحیه نرمال"

    # -------------------------
    # MACD
    # -------------------------

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 مومنتوم صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 مومنتوم نزولی"
    else:
        macd_status = "🟡 مومنتوم خنثی"

    # -------------------------
    # امتیاز نهایی
    # -------------------------

    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        final_signal = "🟢 تمایل صعودی"
    elif score == 0:
        final_signal = "🔴 تمایل نزولی"
    else:
        final_signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "final_signal": final_signal,
    }

def format_aapl_report(signal):
    """
    ساخت گزارش فارسی تحلیل تکنیکال Apple
    """

    return (
        "🍎 تحلیل تکنیکال Apple (AAPL)\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💰 قیمت فعلی: {signal['price']:.2f} دلار\n\n"

        "📊 میانگین‌های متحرک\n"
        f"EMA20: {signal['ema20']:.2f}\n"
        f"EMA50: {signal['ema50']:.2f}\n"
        f"روند: {signal['trend']}\n\n"

        "📈 RSI14\n"
        f"RSI: {signal['rsi']:.2f}\n"
        f"وضعیت: {signal['rsi_status']}\n\n"

        "📉 MACD\n"
        f"MACD: {signal['macd']:.2f}\n"
        f"Signal: {signal['macd_signal']:.2f}\n"
        f"Histogram: {signal['macd_histogram']:.2f}\n"
        f"وضعیت: {signal['macd_status']}\n\n"

        "🎯 سیگنال نهایی\n"
        f"{signal['final_signal']}\n\n"

        "⚠️ توجه:\n"
        "این تحلیل صرفاً بر اساس داده‌های تکنیکال و برای اهداف آموزشی "
        "ارائه شده و به‌تنهایی توصیه خرید یا فروش نیست."
    )

def get_msft_data():
    """
    دریافت داده‌های Microsoft از Yahoo Finance
    """

    ticker = yf.Ticker("MSFT")

    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Microsoft دریافت نشد.")

    return data

def calculate_msft_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Microsoft
    """

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_msft_signal(data):
    """
    تولید سیگنال تکنیکال Microsoft
    """

    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]

    rsi = latest["RSI14"]

    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    if rsi >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 ناحیه نرمال"

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 مومنتوم صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 مومنتوم نزولی"
    else:
        macd_status = "🟡 مومنتوم خنثی"

    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        final_signal = "🟢 تمایل صعودی"
    elif score == 0:
        final_signal = "🔴 تمایل نزولی"
    else:
        final_signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "final_signal": final_signal,
    }

def format_msft_report(signal):
    """
    ساخت گزارش فارسی تحلیل تکنیکال Microsoft
    """

    return (
        "🪟 تحلیل تکنیکال Microsoft (MSFT)\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💰 قیمت فعلی: {signal['price']:.2f} دلار\n\n"

        "📊 میانگین‌های متحرک\n"
        f"EMA20: {signal['ema20']:.2f}\n"
        f"EMA50: {signal['ema50']:.2f}\n"
        f"روند: {signal['trend']}\n\n"

        "📈 RSI14\n"
        f"RSI: {signal['rsi']:.2f}\n"
        f"وضعیت: {signal['rsi_status']}\n\n"

        "📉 MACD\n"
        f"MACD: {signal['macd']:.2f}\n"
        f"Signal: {signal['macd_signal']:.2f}\n"
        f"Histogram: {signal['macd_histogram']:.2f}\n"
        f"وضعیت: {signal['macd_status']}\n\n"

        "🎯 سیگنال نهایی\n"
        f"{signal['final_signal']}\n\n"

        "⚠️ توجه:\n"
        "این تحلیل صرفاً بر اساس داده‌های تکنیکال و برای اهداف آموزشی "
        "ارائه شده و به‌تنهایی توصیه خرید یا فروش نیست."
    )

def get_googl_data():
    """
    دریافت داده‌های Google از Yahoo Finance
    """
    ticker = yf.Ticker("GOOGL")
    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Google دریافت نشد.")

    return data

def calculate_googl_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Google
    """

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    data["SMA20"] = data["Close"].rolling(
        window=20
    ).mean()

    data["SMA50"] = data["Close"].rolling(
        window=50
    ).mean()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(
        window=14
    ).mean()

    avg_loss = loss.rolling(
        window=14
    ).mean()

    rs = avg_gain / avg_loss

    data["RSI14"] = 100 - (
        100 / (1 + rs)
    )

    ema12 = data["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = data["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    data["MACD"] = ema12 - ema26

    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_googl_signal(data):
    """
    تولید سیگنال تکنیکال Google
    """

    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]
    rsi = latest["RSI14"]
    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    if rsi >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 ناحیه نرمال"

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 مومنتوم صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 مومنتوم نزولی"
    else:
        macd_status = "🟡 مومنتوم خنثی"

    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        final_signal = "🟢 تمایل صعودی"
    elif score == 0:
        final_signal = "🔴 تمایل نزولی"
    else:
        final_signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "final_signal": final_signal,
    }

def format_googl_report(signal):
    """
    ساخت گزارش فارسی تحلیل تکنیکال Google
    """

    return (
        "🔎 تحلیل تکنیکال Google (GOOGL)\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 قیمت فعلی: {signal['price']:.2f} دلار\n\n"

        "📊 میانگین‌های متحرک\n"
        f"EMA20: {signal['ema20']:.2f}\n"
        f"EMA50: {signal['ema50']:.2f}\n"
        f"روند: {signal['trend']}\n\n"

        "📈 RSI14\n"
        f"RSI: {signal['rsi']:.2f}\n"
        f"وضعیت: {signal['rsi_status']}\n\n"

        "📉 MACD\n"
        f"MACD: {signal['macd']:.2f}\n"
        f"Signal: {signal['macd_signal']:.2f}\n"
        f"Histogram: {signal['macd_histogram']:.2f}\n"
        f"وضعیت: {signal['macd_status']}\n\n"

        "🎯 سیگنال نهایی\n"
        f"{signal['final_signal']}\n\n"

        "⚠️ توجه:\n"
        "این تحلیل صرفاً بر اساس داده‌های تکنیکال و برای اهداف آموزشی "
        "ارائه شده و به‌تنهایی توصیه خرید یا فروش نیست."
    )

def get_amzn_data():
    """
    دریافت داده‌های Amazon از Yahoo Finance
    """
    ticker = yf.Ticker("AMZN")
    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Amazon دریافت نشد.")

    return data

def calculate_amzn_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Amazon
    """
    data["EMA20"] = data["Close"].ewm(span=20, adjust=False).mean()
    data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()
    data["SMA20"] = data["Close"].rolling(window=20).mean()
    data["SMA50"] = data["Close"].rolling(window=50).mean()

    delta = data["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    data["RSI14"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()

    data["MACD"] = ema12 - ema26
    data["MACD_Signal"] = data["MACD"].ewm(span=9, adjust=False).mean()
    data["MACD_Histogram"] = data["MACD"] - data["MACD_Signal"]

    return data

def get_amzn_signal(data):
    """
    تولید سیگنال تکنیکال Amazon
    """
    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]
    rsi = latest["RSI14"]
    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    if rsi >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 ناحیه نرمال"

    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 مومنتوم صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 مومنتوم نزولی"
    else:
        macd_status = "🟡 مومنتوم خنثی"

    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        final_signal = "🟢 تمایل صعودی"
    elif score == 0:
        final_signal = "🔴 تمایل نزولی"
    else:
        final_signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "final_signal": final_signal,
    }

def format_amzn_report(signal):
    """
    ساخت گزارش فارسی تحلیل تکنیکال Amazon
    """
    return (
        "📦 تحلیل تکنیکال Amazon (AMZN)\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💰 قیمت فعلی: {signal['price']:.2f} دلار\n\n"

        "📊 میانگین‌های متحرک\n"
        f"EMA20: {signal['ema20']:.2f}\n"
        f"EMA50: {signal['ema50']:.2f}\n"
        f"روند: {signal['trend']}\n\n"

        "📈 RSI14\n"
        f"RSI: {signal['rsi']:.2f}\n"
        f"وضعیت: {signal['rsi_status']}\n\n"

        "📉 MACD\n"
        f"MACD: {signal['macd']:.2f}\n"
        f"Signal: {signal['macd_signal']:.2f}\n"
        f"Histogram: {signal['macd_histogram']:.2f}\n"
        f"وضعیت: {signal['macd_status']}\n\n"

        "🎯 سیگنال نهایی\n"
        f"{signal['final_signal']}\n\n"

        "⚠️ توجه:\n"
        "این تحلیل صرفاً بر اساس داده‌های تکنیکال و برای اهداف آموزشی "
        "ارائه شده و به‌تنهایی توصیه خرید یا فروش نیست."
    )

def get_tsla_data():
    """
    دریافت داده‌های Tesla از Yahoo Finance
    """
    ticker = yf.Ticker("TSLA")
    data = ticker.history(
        period="5d",
        interval="1h",
        auto_adjust=False,
    )

    if data.empty:
        raise ValueError("داده‌ای برای Tesla دریافت نشد.")

    return data

def calculate_tsla_indicators(data):
    """
    محاسبه اندیکاتورهای تکنیکال Tesla
    """
    data["EMA20"] = data["Close"].ewm(span=20, adjust=False).mean()
    data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()

    data["SMA20"] = data["Close"].rolling(window=20).mean()
    data["SMA50"] = data["Close"].rolling(window=50).mean()

    # RSI14
    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    data["RSI14"] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()

    data["MACD"] = ema12 - ema26
    data["MACD_Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    return data

def get_tsla_signal(data):
    """
    تولید سیگنال تکنیکال Tesla
    """
    latest = data.iloc[-1]

    price = latest["Close"]
    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]

    rsi = latest["RSI14"]

    macd = latest["MACD"]
    macd_signal = latest["MACD_Signal"]
    macd_histogram = latest["MACD_Histogram"]

    # Trend
    if price > ema20 > ema50:
        trend = "🟢 صعودی"
    elif price < ema20 < ema50:
        trend = "🔴 نزولی"
    else:
        trend = "🟡 خنثی"

    # RSI
    if rsi >= 70:
        rsi_status = "🔴 اشباع خرید"
    elif rsi <= 30:
        rsi_status = "🟢 اشباع فروش"
    else:
        rsi_status = "🟡 ناحیه نرمال"

    # MACD
    if macd > macd_signal and macd_histogram > 0:
        macd_status = "🟢 مومنتوم صعودی"
    elif macd < macd_signal and macd_histogram < 0:
        macd_status = "🔴 مومنتوم نزولی"
    else:
        macd_status = "🟡 مومنتوم خنثی"

    # Final score
    score = 0

    if price > ema20:
        score += 1

    if ema20 > ema50:
        score += 1

    if macd > macd_signal:
        score += 1

    if score >= 2:
        final_signal = "🟢 تمایل صعودی"
    elif score == 0:
        final_signal = "🔴 تمایل نزولی"
    else:
        final_signal = "🟡 وضعیت متعادل"

    return {
        "price": price,
        "ema20": ema20,
        "ema50": ema50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_histogram,
        "trend": trend,
        "rsi_status": rsi_status,
        "macd_status": macd_status,
        "final_signal": final_signal,
    }

def format_tsla_report(signal):
    """
    ساخت گزارش فارسی تحلیل تکنیکال Tesla
    """
    return (
        "🚗 تحلیل تکنیکال Tesla (TSLA)\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💰 قیمت فعلی: {signal['price']:.2f} دلار\n\n"

        "📊 میانگین‌های متحرک\n"
        f"EMA20: {signal['ema20']:.2f}\n"
        f"EMA50: {signal['ema50']:.2f}\n"
        f"روند: {signal['trend']}\n\n"

        "📈 RSI14\n"
        f"RSI: {signal['rsi']:.2f}\n"
        f"وضعیت: {signal['rsi_status']}\n\n"

        "📉 MACD\n"
        f"MACD: {signal['macd']:.2f}\n"
        f"Signal: {signal['macd_signal']:.2f}\n"
        f"Histogram: {signal['macd_histogram']:.2f}\n"
        f"وضعیت: {signal['macd_status']}\n\n"

        "🎯 سیگنال نهایی\n"
        f"{signal['final_signal']}\n\n"

        "⚠️ توجه:\n"
        "این تحلیل صرفاً بر اساس داده‌های تکنیکال و برای اهداف آموزشی "
        "ارائه شده و به‌تنهایی توصیه خرید یا فروش نیست."
    )
