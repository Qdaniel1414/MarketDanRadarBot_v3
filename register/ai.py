from telegram.ext import MessageHandler, filters

from handlers.ai.menu import ai_menu
from handlers.ai.market_analyzer import market_analyzer_menu
from handlers.ai.currency_analyzer import currency_market_analysis
from handlers.ai.gold_analyzer import gold_market_analysis
from handlers.ai.crypto_analyzer import crypto_market_analysis
from handlers.ai.global_market_analyzer import global_market_analysis

from handlers.ai.technical_scanner import (
    technical_scanner_menu,
    technical_indices_menu,
    us_stocks_menu,
    bitcoin_scanner,
    ethereum_scanner,
    gold_scanner,
    dxy_scanner,
    sp500_scanner,
    nasdaq_scanner,
    dow_scanner,
    vix_scanner,
        nvda_scanner,
    aapl_scanner,
    msft_scanner,
    googl_scanner,
amzn_scanner,
    tsla_scanner,
)

from handlers.ai.news import (
    news_menu,
    important_economic_news,
    iran_economic_news,
    global_economic_news,
    currency_news,
    gold_coin_news,
    crypto_news,
)

from handlers.ai.smart_calculator_conversation import (
    smart_calculator_conversation,
)

from handlers.ai.scenario import (
    scenario_menu,
    bullish_scenario,
    bearish_scenario,
    neutral_scenario,
    dollar_scenario,
    gold_scenario,
    bitcoin_scenario,
)

from handlers.ai.market_lab import (
    market_lab_menu,
    dollar_gold_test,
    ounce_gold_test,
    price_change_test,
    compare_scenarios_test,
)

from handlers.ai.sites import (
    sites_menu,
    macro_sites,
    gold_sites,
    currency_sites,
    crypto_sites,
    iran_sites,
    stock_sites,
    global_sites,
    financial_tools,
)

def register_ai_handlers(app):
    print("🔥 REGISTER AI")

    # ============================================================
    # 🤖 منوی اصلی دستیار هوشمند
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🤖 دستیار هوشمند$"),
            ai_menu,
        )
    )

    # ============================================================
    # 📊 تحلیلگر هوشمند بازار
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📊 تحلیلگر هوشمند بازار$"),
            market_analyzer_menu,
        )
    )

    # ============================================================
    # 📉 اسکنر تکنیکال بازار
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📉 اسکنر تکنیکال بازار$"),
            technical_scanner_menu,
        )
    )

    # ============================================================
    # 📊 منوی شاخص‌های بازار
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📊 شاخص‌ها$"),
            technical_indices_menu,
        )
    )

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🏢 سهام آمریکا$"),
        us_stocks_menu,
    )
)
    # ============================================================
    # 📈 S&P 500
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📈 S&P 500$"),
            sp500_scanner,
        )
    )


    app.add_handler(
    MessageHandler(
        filters.Regex(r"^💻 Nasdaq$"),
        nasdaq_scanner,
    )
)

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🏦 Dow Jones$"),
        dow_scanner,
    )
)
    app.add_handler(
    MessageHandler(
        filters.Regex(r"^📉 VIX$"),
        vix_scanner,
    )
)

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🟢 Nvidia$"),
        nvda_scanner,
    )
)

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🍎 Apple$"),
        aapl_scanner,
    )
)

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🪟 Microsoft$"),
        msft_scanner,
    )
)

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🔎 Google$"),
            googl_scanner,
        )
    )

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^📦 Amazon$"),
        amzn_scanner,
    )
)

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🚗 Tesla$"),
        tsla_scanner,
    )
)
    # ============================================================
    # ₿ Bitcoin
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^₿ Bitcoin$"),
            bitcoin_scanner,
        )
    )

    # ============================================================
    # Ξ Ethereum
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^Ξ Ethereum$"),
            ethereum_scanner,
        )
    )

    # ============================================================
    # 🥇 Gold
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 طلا$"),
            gold_scanner,
        )
    )

    # ============================================================
    # 💵 DXY
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 دلار$"),
            dxy_scanner,
        )
    )

    # ============================================================
    # 💵 تحلیل دلار و ارز
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 تحلیل دلار و ارز$"),
            currency_market_analysis,
        )
    )

    # ============================================================
    # 🥇 تحلیل طلا و سکه
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 تحلیل طلا و سکه$"),
            gold_market_analysis,
        )
    )

    # ============================================================
    # ₿ تحلیل کریپتو
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^₿ تحلیل کریپتو$"),
            crypto_market_analysis,
        )
    )

    # ============================================================
    # 📈 تحلیل بازارهای جهانی
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📈 تحلیل بازارهای جهانی$"),
            global_market_analysis,
        )
    )

    # ============================================================
    # 🧮 محاسبه‌گر هوشمند
    # ============================================================

    app.add_handler(
        smart_calculator_conversation
    )

    # ============================================================
    # 📰 تحلیل اخبار اقتصادی
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📰 تحلیل اخبار اقتصادی$"),
            news_menu,
        )
    )

    # ============================================================
    # 🧠 تحلیل سناریو
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🧠 تحلیل سناریو$"),
            scenario_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📈 سناریوی صعودی$"),
            bullish_scenario,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📉 سناریوی نزولی$"),
            bearish_scenario,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^⚖️ سناریوی خنثی$"),
            neutral_scenario,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 سناریوی دلار$"),
            dollar_scenario,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 سناریوی طلا$"),
            gold_scenario,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^₿ سناریوی بیت‌کوین$"),
            bitcoin_scenario,
        )
    )

        # ============================================================
    # 🔙 بازگشت به دستیار هوشمند
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🔙 بازگشت به دستیار هوشمند$"),
            ai_menu,
        )
    )


    # ============================================================
    # 🔬 آزمایشگاه بازار
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🔬 آزمایشگاه بازار$"),
            market_lab_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 اثر دلار روی طلا$"),
            dollar_gold_test,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 اثر اونس روی طلا$"),
            ounce_gold_test,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📊 تغییر درصدی قیمت$"),
            price_change_test,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^⚖️ مقایسه دو سناریو$"),
            compare_scenarios_test,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🔙 بازگشت به دستیار هوشمند$"),
            ai_menu,
        )
    )


    # ============================================================
    # 🌐 معرفی سایت‌های کاربردی
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🌐 معرفی سایت‌های کاربردی$"),
            sites_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📊 اقتصاد کلان$"),
            macro_sites,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 طلا و فلزات گرانبها$"),
            gold_sites,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 دلار و بازار ارز$"),
            currency_sites,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^\u20bf سایت‌های ارزهای دیجیتال$"),
            crypto_sites,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🌍 سایت‌های بازارهای جهانی$"),
            global_sites,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🇮🇷 اقتصاد و بازار ایران$"),
            iran_sites,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📈 بورس و سهام$"),
            stock_sites,
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🛠 ابزارهای مالی$"),
            financial_tools,
        )
    )
    
    # ============================================================
    # 📰 اخبار مهم اقتصادی
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📰 اخبار مهم اقتصادی$"),
            important_economic_news,
        )
    )

    # ============================================================
    # 🇮🇷 اخبار اقتصاد ایران
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🇮🇷 اخبار اقتصاد ایران$"),
            iran_economic_news,
        )
    )

    # ============================================================
    # 🌍 اخبار اقتصاد جهان
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🌍 اخبار اقتصاد جهان$"),
            global_economic_news,
        )
    )

    # ============================================================
    # 💵 اخبار دلار و ارز
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 اخبار دلار و ارز$"),
            currency_news,
        )
    )

    # ============================================================
    # 🥇 اخبار طلا و سکه
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🥇 اخبار طلا و سکه$"),
            gold_coin_news,
        )
    )

    # ============================================================
    # ₿ اخبار کریپتو
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^₿ اخبار کریپتو$"),
            crypto_news,
        )
    )

    print("✅ AI HANDLERS REGISTERED")