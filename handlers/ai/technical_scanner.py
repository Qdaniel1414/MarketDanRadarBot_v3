from telegram import Update
from telegram.ext import ContextTypes

from keyboards.technical_scanner_keyboard import technical_scanner_keyboard
from keyboards.technical_indices_keyboard import technical_indices_keyboard
from keyboards.us_stocks_keyboard import us_stocks_keyboard

from services.technical_scanner import (
    get_btc_data,
    calculate_btc_indicators,
    get_btc_signal,
    format_btc_report,

    get_eth_data,
    calculate_eth_indicators,
    get_eth_signal,
    format_eth_report,

    get_gold_data,
    calculate_gold_indicators,
    get_gold_signal,
    format_gold_report,

    get_dxy_data,
    calculate_dxy_indicators,
    get_dxy_signal,
    format_dxy_report,

    get_sp500_data,
    calculate_sp500_indicators,
    get_sp500_signal,
    format_sp500_report,

    get_nasdaq_data,
    calculate_nasdaq_indicators,
    get_nasdaq_signal,
    format_nasdaq_report,

    get_dow_data,
    calculate_dow_indicators,
    get_dow_signal,
    format_dow_report,

    get_vix_data,
    calculate_vix_indicators,
    get_vix_signal,
    format_vix_report,

    get_nvda_data,
    calculate_nvda_indicators,
    get_nvda_signal,
    format_nvda_report,

    get_aapl_data,
    calculate_aapl_indicators,
    get_aapl_signal,
    format_aapl_report,

    get_msft_data,
    calculate_msft_indicators,
    get_msft_signal,
    format_msft_report,

    get_googl_data,
    calculate_googl_indicators,
    get_googl_signal,
    format_googl_report,

    get_amzn_data,
    calculate_amzn_indicators,
    get_amzn_signal,
    format_amzn_report,

    get_tsla_data,
    calculate_tsla_indicators,
    get_tsla_signal,
    format_tsla_report,
)


# ============================================================
# 📉 منوی اصلی اسکنر تکنیکال
# ============================================================

async def technical_scanner_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📉 اسکنر تکنیکال بازار\n\n"
        "بازاری را که می‌خواهید اسکن تکنیکال شود انتخاب کنید:",
        reply_markup=technical_scanner_keyboard,
    )


# ============================================================
# 📊 منوی شاخص‌ها
# ============================================================

async def technical_indices_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📊 شاخص‌های بازار\n\n"
        "لطفاً شاخص موردنظر را انتخاب کنید:",
        reply_markup=technical_indices_keyboard,
    )


# ============================================================
# 🏢 منوی سهام آمریکا
# ============================================================

async def us_stocks_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🏢 سهام آمریکا\n\n"
        "لطفاً سهم موردنظر برای اسکن تکنیکال را انتخاب کنید:",
        reply_markup=us_stocks_keyboard,
    )


# ============================================================
# ₿ Bitcoin
# ============================================================

async def bitcoin_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Bitcoin..."
    )

    try:
        data = get_btc_data()
        data = calculate_btc_indicators(data)
        signal = get_btc_signal(data)
        report = format_btc_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ BITCOIN SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Bitcoin مشکلی رخ داد."
        )


# ============================================================
# Ξ Ethereum
# ============================================================

async def ethereum_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Ethereum..."
    )

    try:
        data = get_eth_data()
        data = calculate_eth_indicators(data)
        signal = get_eth_signal(data)
        report = format_eth_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ ETHEREUM SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Ethereum مشکلی رخ داد."
        )


# ============================================================
# 🥇 Gold
# ============================================================

async def gold_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های طلا..."
    )

    try:
        data = get_gold_data()
        data = calculate_gold_indicators(data)
        signal = get_gold_signal(data)
        report = format_gold_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ GOLD SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات طلا مشکلی رخ داد."
        )


# ============================================================
# 💵 DXY
# ============================================================

async def dxy_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های DXY..."
    )

    try:
        data = get_dxy_data()
        data = calculate_dxy_indicators(data)
        signal = get_dxy_signal(data)
        report = format_dxy_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ DXY SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات DXY مشکلی رخ داد."
        )


# ============================================================
# 📈 S&P 500
# ============================================================

async def sp500_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های S&P 500..."
    )

    try:
        data = get_sp500_data()
        data = calculate_sp500_indicators(data)
        signal = get_sp500_signal(data)
        report = format_sp500_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ S&P 500 SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات S&P 500 مشکلی رخ داد."
        )


# ============================================================
# 💻 Nasdaq
# ============================================================

async def nasdaq_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Nasdaq..."
    )

    try:
        data = get_nasdaq_data()
        data = calculate_nasdaq_indicators(data)
        signal = get_nasdaq_signal(data)
        report = format_nasdaq_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ NASDAQ SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Nasdaq مشکلی رخ داد."
        )


# ============================================================
# 🏦 Dow Jones
# ============================================================

async def dow_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Dow Jones..."
    )

    try:
        data = get_dow_data()
        data = calculate_dow_indicators(data)
        signal = get_dow_signal(data)
        report = format_dow_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ DOW JONES SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Dow Jones مشکلی رخ داد."
        )


# ============================================================
# 📉 VIX
# ============================================================

async def vix_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های VIX..."
    )

    try:
        data = get_vix_data()
        data = calculate_vix_indicators(data)
        signal = get_vix_signal(data)
        report = format_vix_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ VIX SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات VIX مشکلی رخ داد."
        )


# ============================================================
# 🟢 Nvidia
# ============================================================

async def nvda_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Nvidia..."
    )

    try:
        data = get_nvda_data()
        data = calculate_nvda_indicators(data)
        signal = get_nvda_signal(data)
        report = format_nvda_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ NVIDIA SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Nvidia مشکلی رخ داد."
        )


# ============================================================
# 🍎 Apple
# ============================================================

async def aapl_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Apple..."
    )

    try:
        data = get_aapl_data()
        data = calculate_aapl_indicators(data)
        signal = get_aapl_signal(data)
        report = format_aapl_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ APPLE SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Apple مشکلی رخ داد."
        )


# ============================================================
# 🪟 Microsoft
# ============================================================

async def msft_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Microsoft..."
    )

    try:
        data = get_msft_data()
        data = calculate_msft_indicators(data)
        signal = get_msft_signal(data)
        report = format_msft_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ MICROSOFT SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Microsoft مشکلی رخ داد."
        )


# ============================================================
# 🔎 Google
# ============================================================

async def googl_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Google..."
    )

    try:
        data = get_googl_data()
        data = calculate_googl_indicators(data)
        signal = get_googl_signal(data)
        report = format_googl_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ GOOGLE SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Google مشکلی رخ داد."
        )


# ============================================================
# 📦 Amazon
# ============================================================

async def amzn_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Amazon..."
    )

    try:
        data = get_amzn_data()
        data = calculate_amzn_indicators(data)
        signal = get_amzn_signal(data)
        report = format_amzn_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ AMAZON SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ در دریافت یا تحلیل اطلاعات Amazon مشکلی رخ داد."
        )


# ============================================================
# 🚗 Tesla
# ============================================================

async def tsla_scanner(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⏳ در حال دریافت و تحلیل داده‌های Tesla..."
    )

    try:
        data = get_tsla_data()
        data = calculate_tsla_indicators(data)
        signal = get_tsla_signal(data)
        report = format_tsla_report(signal)

        await update.message.reply_text(report)

    except Exception as e:
        print("❌ TESLA SCANNER ERROR:", e)

        await update.message.reply_text(
            "❌ متأسفانه در دریافت یا تحلیل داده‌های Tesla مشکلی پیش آمد."
        )