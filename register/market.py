from telegram.ext import MessageHandler, filters

from handlers.market import market_menu

from handlers.global_market.menu import (
    global_market_menu,
)

from handlers.iran_market.menu import (
    iran_market_menu,
)

from handlers.iran_market.formulas.gold_formula import (
    gold_formula,
)

from handlers.iran_market.formulas.dollar_formula import (
    dollar_formula,
)

from handlers.iran_market.funds.investment_funds import (
    investment_funds,
)

# ==========================================
# Conversation محاسبه سکه
# ==========================================

from handlers.iran_market.coin_calculator.coin_conversation import (
    coin_conversation,
)

# ==========================================
# Conversation محاسبه ارزش‌گذاری دلار
# ==========================================

from handlers.iran_market.dollar_calculator.dollar_conversation import (
    dollar_conversation,
)

# ==========================================
# Conversation محاسبه طلای ۱۸ عیار
# ==========================================

from handlers.iran_market.formulas.gold18_conversation import (
    gold18_conversation,
)

# ==========================================
# Conversation محاسبه طلای ۲۴ عیار
# ==========================================

from handlers.iran_market.formulas.gold24_conversation import (
    gold24_conversation,
)

# ==========================================
# Conversation محاسبه طلای آب‌شده
# ==========================================

from handlers.iran_market.formulas.gold_melted_conversation import (
    gold_melted_conversation,
)


def register_market_handlers(app):

    print("🔥 REGISTER MARKET")

    # ==========================================
    # محاسبه سکه
    # ==========================================

    print("🔥 REGISTER COIN CONVERSATION")

    app.add_handler(
        coin_conversation
    )

    print("✅ COIN CONVERSATION REGISTERED")

    # ==========================================
    # محاسبه ارزش‌گذاری دلار
    # ==========================================

    print("🔥 REGISTER DOLLAR CONVERSATION")

    app.add_handler(
        dollar_conversation
    )

    print("✅ DOLLAR CONVERSATION REGISTERED")

    # ==========================================
    # محاسبه طلای ۱۸ عیار
    # ==========================================

    print("🔥 REGISTER GOLD 18 CONVERSATION")

    app.add_handler(
        gold18_conversation
    )

    print("✅ GOLD 18 CONVERSATION REGISTERED")

    # ==========================================
    # محاسبه طلای ۲۴ عیار
    # ==========================================

    print("🔥 REGISTER GOLD 24 CONVERSATION")

    app.add_handler(
        gold24_conversation
    )

    print("✅ GOLD 24 CONVERSATION REGISTERED")

    # ==========================================
    # محاسبه طلای آب‌شده
    # ==========================================

    print("🔥 REGISTER GOLD MELTED CONVERSATION")

    app.add_handler(
        gold_melted_conversation
    )

    print("✅ GOLD MELTED CONVERSATION REGISTERED")

    # ==========================================
    # قیمت‌های لحظه‌ای بازار
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^📊 قیمت‌های لحظه‌ای بازار$"
            ),
            market_menu,
        )
    )

    # ==========================================
    # بازارهای بین‌المللی
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^🌍 بازارهای بین‌المللی$"
            ),
            global_market_menu,
        )
    )

    # ==========================================
    # بازار ایران
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^🇮🇷 بازار ایران$"
            ),
            iran_market_menu,
        )
    )

    # ==========================================
    # صندوق‌های سرمایه‌گذاری
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^🏦 صندوق‌های سرمایه‌گذاری$"
            ),
            investment_funds,
        )
    )

    # ==========================================
    # فرمول محاسبه طلا
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^🪙 فرمول محاسبه طلا$"
            ),
            gold_formula,
        )
    )

    # ==========================================
    # فرمول محاسبه دلار
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^💵 فرمول محاسبه دلار$"
            ),
            dollar_formula,
        )
    )

    print(
        "✅ MARKET HANDLERS REGISTERED SUCCESSFULLY"
    )