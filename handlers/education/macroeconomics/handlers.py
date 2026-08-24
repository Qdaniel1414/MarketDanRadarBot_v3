from telegram import Update
from telegram.ext import ContextTypes

from handlers.home import home

# ======================================
# Topics
# ======================================

from handlers.education.macroeconomics.topics.inflation import inflation
from handlers.education.macroeconomics.topics.cpi import cpi
from handlers.education.macroeconomics.topics.core_cpi import core_cpi
from handlers.education.macroeconomics.topics.ppi import ppi
from handlers.education.macroeconomics.topics.gdp import gdp
from handlers.education.macroeconomics.topics.interest_rate import interest_rate
from handlers.education.macroeconomics.topics.fomc import fomc
from handlers.education.macroeconomics.topics.dot_plot import dot_plot

from handlers.education.macroeconomics.topics.nfp import nfp
from handlers.education.macroeconomics.topics.pmi import pmi
from handlers.education.macroeconomics.topics.pce import pce
from handlers.education.macroeconomics.topics.qe import qe
from handlers.education.macroeconomics.topics.qt import qt
from handlers.education.macroeconomics.topics.tapering import tapering
from handlers.education.macroeconomics.topics.dxy import dxy
from handlers.education.macroeconomics.topics.unemployment import unemployment
from handlers.education.macroeconomics.topics.liquidity import liquidity
from handlers.education.macroeconomics.topics.monetary_base import monetary_base
from handlers.education.macroeconomics.topics.money_supply import money_supply
from handlers.education.macroeconomics.topics.recession import recession
from handlers.education.macroeconomics.topics.economic_cycle import economic_cycle
from handlers.education.macroeconomics.topics.yield_curve import yield_curve
from handlers.education.macroeconomics.topics.federal_reserve import federal_reserve
from handlers.education.macroeconomics.topics.ecb import ecb
from handlers.education.macroeconomics.topics.boj import boj
from handlers.education.macroeconomics.topics.inflation_expectation import inflation_expectation
from handlers.education.macroeconomics.topics.retail_sales import retail_sales
from handlers.education.macroeconomics.topics.consumer_confidence import consumer_confidence
from handlers.education.macroeconomics.topics.producer_confidence import producer_confidence
from handlers.education.macroeconomics.topics.trade_balance import trade_balance
from handlers.education.macroeconomics.topics.current_account import current_account
from handlers.education.macroeconomics.topics.budget_deficit import budget_deficit
from handlers.education.macroeconomics.topics.government_debt import government_debt
from handlers.education.macroeconomics.topics.exchange_rate import exchange_rate
from handlers.education.macroeconomics.topics.purchasing_power import purchasing_power


# ======================================
# Dictionary
# ======================================

TOPICS = {

    "📈 تورم": inflation,
    "📊 CPI": cpi,
    "📉 Core CPI": core_cpi,
    "🏭 PPI": ppi,
    "🌍 GDP": gdp,
    "💰 نرخ بهره": interest_rate,
    "🏦 FOMC": fomc,
    "🎯 Dot Plot": dot_plot,

    "💼 NFP": nfp,
    "🏢 PMI": pmi,
    "💳 PCE": pce,
    "💵 QE": qe,
    "📉 QT": qt,
    "✂️ Tapering": tapering,
    "💲 شاخص DXY": dxy,
    "👥 نرخ بیکاری": unemployment,
    "💸 نقدینگی": liquidity,
    "🏛 پایه پولی": monetary_base,
    "💵 عرضه پول": money_supply,
    "📉 رکود": recession,
    "🔄 چرخه اقتصادی": economic_cycle,
    "📈 منحنی بازده": yield_curve,
    "🏦 فدرال رزرو": federal_reserve,
    "🏦 ECB": ecb,
    "🏦 BOJ": boj,
    "💬 انتظارات تورمی": inflation_expectation,
    "🛒 خرده فروشی": retail_sales,
    "👥 اعتماد مصرف‌کننده": consumer_confidence,
    "🏭 اعتماد تولیدکننده": producer_confidence,
    "⚖️ تراز تجاری": trade_balance,
    "🌐 حساب جاری": current_account,
    "📉 کسری بودجه": budget_deficit,
    "🏛 بدهی دولت": government_debt,
    "💱 نرخ ارز": exchange_rate,
    "💰 قدرت خرید": purchasing_power,

}


# ======================================
# Main Handler
# ======================================

async def macroeconomics_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    

    # آموزش‌ها
    handler = TOPICS.get(text)

    if handler:
        return await handler(update, context)

    # اگر آموزش ثبت نشده بود
    await update.message.reply_text(
        "🚧 این آموزش هنوز اضافه نشده است."
    )