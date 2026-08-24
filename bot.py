print("🔥 BOT.PY IS RUNNING")
print("🔥 BOT FILE:", __file__)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN

from handlers.start import start
from handlers.contact import contact_handler
from handlers.profile import profile_handler

from handlers.market import market_menu
from handlers.market_back import market_back_handler
from handlers.back import back_handler

from handlers.currency import currency_prices
from handlers.gold import gold_prices
from handlers.global_prices import global_prices

from handlers.crypto import crypto_prices

from handlers.crypto_pages import (
    crypto_page_1,
    crypto_page_2,
)

from handlers.crypto_search import (
    crypto_search_start,
    crypto_search_result,
)

from handlers.calculator import calculator_menu


from handlers.iran_market.menu import (
    iran_market_menu,
)

from handlers.iran_market.funds.investment_funds import (
    investment_funds,
)


from handlers.iran_market.funds.leveraged_funds import (
    leveraged_funds,
)

from handlers.iran_market.funds.mixed_funds import (
    mixed_funds,
)

from handlers.iran_market.funds.gold_funds import (
    gold_funds,
)

from handlers.iran_market.funds.fixed_income_funds import (
    fixed_income_funds,
)

from handlers.iran_market.funds.stock_funds import (
    stock_funds,
)

from handlers.iran_market.funds.mixed_funds import (
    mixed_funds,
)

from handlers.iran_market.funds.index_funds import (
    index_funds,
)

from handlers.iran_market.funds.real_estate_funds import (
    real_estate_funds,
)


from handlers.iran_market.gold_funds.menu import (
    gold_funds_menu,
)

from handlers.iran_market.gold_funds.fund_detail import (
    gold_fund_detail,
)

from handlers.iran_market.formulas.gold_formula import (
    gold_formula,
)

from handlers.iran_market.formulas.dollar_formula import (
    dollar_formula,
)

from handlers.iran_market.formulas.coin_formula import (
    coin_formula,
)

from handlers.iran_market.gold_calculator.menu import (
    gold_calculator_menu,
)

from handlers.iran_market.dollar_calculator.menu import (
    dollar_calculator_menu,
)

from handlers.iran_market.coin_calculator.menu import (
    coin_calculator_menu,
)

# موتور جدید ماشین حساب
from handlers.calculator_conversation import (
    calculator_conversation,
)

from handlers.iran_market.formulas.gold18_conversation import (
    gold18_conversation,
)

from handlers.iran_market.formulas.gold24_conversation import (
    gold24_conversation,
)

from handlers.iran_market.formulas.mesghal_conversation import (
    mesghal_conversation,
)

from handlers.iran_market.formulas.gold_melted_conversation import (
    gold_melted_conversation,
)

from handlers.iran_market.formulas.ons_conversation import (
    ons_conversation,
)

from handlers.iran_market.formulas.dollar_conversation import (
    dollar_conversation,
)

from handlers.iran_market.formulas.dollar_by_aed import (
    dollar_by_aed,
)

from handlers.iran_market.formulas.dollar_by_gold import (
    dollar_by_gold,
)

from handlers.iran_market.formulas.dollar_by_inflation import (
    dollar_by_inflation,
)

from handlers.iran_market.formulas.dollar_by_liquidity import (
    dollar_by_liquidity,
)

from services.inflation_service import *
from handlers.iran_market.formulas.dollar_by_inflation import *

from handlers.iran_market.formulas.dollar_compare import (
    dollar_compare,
)

from handlers.iran_market.formulas.intrinsic_imami import (
    intrinsic_imami,
)

from handlers.iran_market.formulas.intrinsic_nim import (
    intrinsic_nim,
)

from handlers.iran_market.formulas.intrinsic_rob import intrinsic_rob

from handlers.iran_market.formulas.intrinsic_gerami import (
    intrinsic_gerami,
)

from handlers.iran_market.funds.fund_detail import (
    fund_detail,
)

from handlers.iran_market.funds.fixed_income_detail import (
    fixed_income_detail,
)

from handlers.home import home

from handlers.education.capital_management.intro import capital_intro

from handlers.education.menu import (
    education_menu,
    education_router,
)

from handlers.education.capital_management.menu import capital_management_menu

from handlers.education.capital_management.menu import (
    one_percent_router,
)
from handlers.education.capital_management.position_size import (
    position_size_handler,
)

from handlers.education.capital_management.risk_reward import (
    risk_reward_handler,
)

from handlers.education.capital_management.mistakes import mistakes_handler

from handlers.education.financial_literacy.menu import (
    financial_literacy_menu,
    financial_literacy_router,
)

from handlers.education.financial_literacy.compound_interest.calculator import (
    compound_interest_handler,
)

from handlers.education.financial_literacy.compound_interest import (
    compound_interest,
    compound_interest_intro,
    compound_interest_example,
)

from handlers.education.financial_literacy.time_value import (
    time_value_menu,
    time_value_intro,
    time_value_example,
    time_value_calculator,
    time_value_input,
)

from handlers.education.financial_literacy.purchasing_power import (
    purchasing_power_menu,
    purchasing_power_intro,
    purchasing_power_example,
    purchasing_power_calculator,
    purchasing_power_input,
)

from handlers.education.financial_literacy.goal_saving.menu import (
    goal_saving_menu,
    goal_saving_router,
)

from handlers.education.financial_literacy.goal_saving.intro import (
    goal_saving_intro,
)

from handlers.education.financial_literacy.goal_saving.example import (
    goal_saving_example,
)

from handlers.education.financial_literacy.goal_saving.calculator import (
    goal_saving_calculator,
    goal_saving_input,
)

from handlers.education.financial_literacy.roi import (
    roi_menu,
    roi_intro,
    roi_example,
    roi_calculator,
    roi_input,
)

from handlers.education.financial_literacy.real_return import (
    real_return_menu,
    real_return_intro,
    real_return_example,
    real_return_calculator,
    real_return_input,
)

from handlers.education.financial_literacy.diversification import (
    diversification_menu,
    diversification_intro,
    diversification_example,
    diversification_calculator,
)

from handlers.education.financial_literacy.active_passive_income import (
    active_passive_income_menu,
    active_passive_income_intro,
    active_passive_income_example,
    active_passive_income_calculator,
    active_passive_income_input,
)

from handlers.education.financial_literacy.budget_50_30_20 import (
    budget_50_30_20_menu,
    budget_50_30_20_intro,
    budget_50_30_20_example,
    budget_50_30_20_calculator,
    budget_50_30_20_input,
)

from handlers.education.technical_analysis import (
    technical_analysis_menu,
    technical_analysis_router,
)

from handlers.education.technical_analysis.trend import (
    trend_menu,
    trend_router,
    trend_intro,
    trend_example,
    trend_calculator,
    trend_input,
)

from handlers.education.technical_analysis.support_resistance import (
    support_resistance_menu,
    support_resistance_router,
    support_resistance_intro,
    support_resistance_example,
    support_resistance_calculator,
    support_resistance_input,
)

from handlers.education.technical_analysis.volume import (
    volume_menu,
    volume_router,
    volume_intro,
    volume_example,
    volume_calculator,
    volume_input,
)

from handlers.education.technical_analysis.position_management import (
    position_management_menu,
    position_management_router,
    position_management_intro,
    position_management_calculator,
    position_management_example,
    position_management_input,
    position_management_mistakes,
)

from handlers.education.technical_analysis.trading_psychology import (
    trading_psychology_menu,
    trading_psychology_router,
    trading_psychology_intro,
    trading_psychology_example,
    trading_psychology_mistakes,
    trading_personality_test,
    trading_personality_input,
)

from handlers.education.technical_analysis.glossary import (
    glossary_menu,
    glossary_router,
    candlestick_intro,
    timeframe_intro,
    glossary_trend_intro,
    volatility_intro,
    liquidity_intro,
    pullback_intro,
    breakout_intro,
    fake_breakout_intro,
    momentum_intro,
    risk_reward_intro,
    liquidity_grab_intro,
    glossary_dictionary,
)

from handlers.education.crypto_education import (
    crypto_education_menu,
    crypto_education_router,
)

from handlers.education.crypto_education.bitcoin import (
    bitcoin_menu,
    bitcoin_intro,
    bitcoin_example,
    bitcoin_calculator,
    bitcoin_input,
)

from loaders.register_education import register_education

from handlers.education.crypto_education.blockchain.intro import blockchain_intro

from handlers.education.crypto_education.altcoin import altcoin_intro

from handlers.education.crypto_education.stablecoin import stablecoin_intro

from handlers.education.crypto_education.usdt import usdt_intro

from handlers.education.crypto_education.usdt import (
    usdt_intro,
)
from handlers.education.crypto_education.smart_contract import (
    smart_contract_intro,
)

from handlers.education.crypto_education.defi import (
    defi_intro,
)

from handlers.education.crypto_education.nft import (
    nft_intro,
)

from handlers.education.crypto_education.mining import (
    mining_intro,
)

from handlers.education.crypto_education.glossary import glossary_intro
from handlers.education.crypto_education.calculators.dca import (
    dca_start,
    dca_capital,
    dca_count,
    dca_interval,
)

from handlers.admin import (
    admin_input,
    set_usd,
    set_usdt,
    set_aed,
    set_eur,
    set_gbp,
    set_try,
    set_gold18,
    set_gold24,
    set_melted,
    set_imami,
    set_bahar,
    set_nim,
    set_rob,
    set_gerami,
    set_ounce,
    set_btc,
    set_eth,
)
from core.handlers import register_handlers

from core.handlers import register_handlers
from register.crypto import register_crypto
from register.education import register_education_handlers
from register.market import register_market_handlers
from register.prices import register_price_handlers
from register.profile import register_profile_handlers
from register.contact import register_contact_handlers
from register.admin import register_admin_handlers
from register.finance_education import register_finance_education
from register.financial_literacy import register_financial_literacy

from register.technical_analysis import register_technical_analysis
from register.crypto_education import register_crypto_education
from handlers.education.macroeconomics.menu import macroeconomics_menu
from register.international_market import register_international_market
from handlers.home_handler import home_handler
from handlers.app_info import app_info_handler
from telegram.ext import CallbackQueryHandler

from handlers.membership_callback import membership_callback
from telegram.ext import CommandHandler
from register.calculators import register_calculator_handlers
from register.ai import register_ai_handlers
# ============================================================
# ADMIN INPUT
# ============================================================

# این Handler را داخل main ثبت می‌کنیم.
# اینجا فقط تابع‌های مربوط به تست را تعریف می‌کنیم.


# ============================================================
# ADMIN / TEST COMMAND
# ============================================================

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        from services.admin_notify import notify_admin

        await notify_admin(
            context,
            "✅ تست ارسال پیام به ادمین"
        )

        if update.message:

            await update.message.reply_text(
                f"""
Chat ID:
{update.effective_chat.id}

User ID:
{update.effective_user.id}
"""
            )

    except Exception as e:

        print("MYID ERROR:", repr(e))

        if update.message:

            await update.message.reply_text(
                "❌ خطا در اجرای دستور /myid"
            )


# ============================================================
# DEBUG HANDLER
# ============================================================

async def debug_all_messages(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    print("🔥🔥 UPDATE RECEIVED 🔥🔥")

    if update.message:
        print(
            "TEXT:",
            repr(update.message.text)
        )

    if update.effective_user:
        print(
            "USER:",
            update.effective_user.id
        )


# ============================================================
# MAIN
# ============================================================

def main():
    print("🔥 BOT.PY IS RUNNING")
    print("🔥 BOT FILE:", __file__)

    # --------------------------------------------------------
    # CREATE APPLICATION
    # --------------------------------------------------------

    app = Application.builder().token(BOT_TOKEN).build()

    print("🔥 APPLICATION CREATED")

    # --------------------------------------------------------
    # START
    # --------------------------------------------------------

    print("🔥 REGISTERING START HANDLER")

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    print("🔥 START HANDLER REGISTERED")

    # --------------------------------------------------------
    # MAIN HANDLERS
    # --------------------------------------------------------

    print("🔥 REGISTERING MAIN HANDLERS")
    register_handlers(app)

    # --------------------------------------------------------
    # HOME
    # --------------------------------------------------------

    print("🔥 REGISTER HOME HANDLER")

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🏠 خانه$"),
            home_handler
        )
    )

    # --------------------------------------------------------
    # APP INFO
    # --------------------------------------------------------

    print("🔥 REGISTER APP INFO HANDLER")

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^ℹ️ اطلاعات برنامه$"),
            app_info_handler
        )
    )

    print("🔥 APP INFO HANDLER REGISTERED")
    
    print("🔥 HOME HANDLER REGISTERED")

    # --------------------------------------------------------
    # CALCULATORS
    # --------------------------------------------------------

    print("🔥 REGISTER CALCULATOR HANDLERS")

    register_calculator_handlers(app)

    print("🔥 CALCULATOR HANDLERS REGISTERED")


    print("🔥 REGISTER AI")
    register_ai_handlers(app)
    print("🔥 AI HANDLERS REGISTERED")


    # --------------------------------------------------------
    # CRYPTO
    # --------------------------------------------------------

    print("🔥 REGISTER CRYPTO")
    register_crypto(app)

    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    print("🔥 REGISTER EDUCATION")
    register_education_handlers(app)

    # --------------------------------------------------------
    # MARKET
    # --------------------------------------------------------

    print("🔥 REGISTER MARKET")
    register_market_handlers(app)

    print("🔥 MARKET HANDLERS REGISTERED SUCCESSFULLY")

    # --------------------------------------------------------
    # PRICES
    # --------------------------------------------------------

    print("🔥 REGISTER PRICES")
    register_price_handlers(app)

    print("🔥 PRICE HANDLERS REGISTERED SUCCESSFULLY")

    # --------------------------------------------------------
    # PROFILE
    # --------------------------------------------------------

    print("🔥 REGISTER PROFILE")
    register_profile_handlers(app)

    # --------------------------------------------------------
    # CONTACT
    # --------------------------------------------------------

    print("🔥 REGISTER CONTACT")
    register_contact_handlers(app)

    # --------------------------------------------------------
    # ADMIN
    # --------------------------------------------------------

    print("🔥 REGISTER ADMIN")
    register_admin_handlers(app)

    # --------------------------------------------------------
    # FINANCE EDUCATION
    # --------------------------------------------------------

    print("🔥 REGISTER FINANCE EDUCATION")
    register_finance_education(app)

    # --------------------------------------------------------
    # FINANCIAL LITERACY
    # --------------------------------------------------------

    print("🔥 REGISTER FINANCIAL LITERACY")
    register_financial_literacy(app)

    # --------------------------------------------------------
    # TECHNICAL ANALYSIS
    # --------------------------------------------------------

    print("🔥 REGISTER TECHNICAL ANALYSIS")
    register_technical_analysis(app)

    # --------------------------------------------------------
    # CRYPTO EDUCATION
    # --------------------------------------------------------

    print("🔥 REGISTER CRYPTO EDUCATION")
    register_crypto_education(app)

    # --------------------------------------------------------
    # INTERNATIONAL MARKET
    # --------------------------------------------------------

    print("🔥 REGISTER INTERNATIONAL MARKET")
    register_international_market(app)

    # --------------------------------------------------------
    # MEMBERSHIP CALLBACK
    # --------------------------------------------------------

    print("🔥 REGISTER MEMBERSHIP CALLBACK")

    app.add_handler(
        CallbackQueryHandler(
            membership_callback,
            pattern=r"^check_membership$"
        )
    )

    # --------------------------------------------------------
    # ADMIN INPUT
    # --------------------------------------------------------

    print("🔥 REGISTER ADMIN INPUT")

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            admin_input
        ),
        group=100
    )

    # --------------------------------------------------------
    # DEBUG
    # --------------------------------------------------------

    print("🔥 REGISTER DEBUG HANDLER")

    app.add_handler(
        MessageHandler(
            filters.ALL,
            debug_all_messages
        ),
        group=-1000
    )

    # --------------------------------------------------------
    # ALL HANDLERS REGISTERED
    # --------------------------------------------------------

    print("🔥🔥🔥 ALL HANDLERS REGISTERED 🔥🔥🔥")

    # --------------------------------------------------------
    # RUN POLLING
    # --------------------------------------------------------

    print("🔥 BEFORE RUN_POLLING")

    app.run_polling()

    print("🔥 AFTER RUN_POLLING")


# ============================================================
# START BOT
# ============================================================

if __name__ == "__main__":
    main()