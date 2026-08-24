from telegram import Update
from telegram.ext import ContextTypes

from keyboards.financial_literacy_keyboard import financial_literacy_keyboard


# =========================
# بهره مرکب
# =========================

from handlers.education.financial_literacy.compound_interest import (
    compound_interest,
)


# =========================
# ارزش زمانی پول
# =========================

from handlers.education.financial_literacy.time_value import (
    time_value_menu,
)


# =========================
# قدرت خرید
# =========================

from handlers.education.financial_literacy.purchasing_power import (
    purchasing_power_menu,
)


# =========================
# پس‌انداز هدف
# =========================

from handlers.education.financial_literacy.goal_saving import (
    goal_saving_menu,
)


# =========================
# ROI
# =========================

from handlers.education.financial_literacy.roi import (
    roi_menu,
)


# =========================
# بازده واقعی
# =========================

from handlers.education.financial_literacy.real_return import (
    real_return_menu,
)


# =========================
# تنوع‌بخشی سرمایه
# =========================

from handlers.education.financial_literacy.diversification import (
    diversification_menu,
)


# =========================
# درآمد فعال و غیرفعال
# =========================

from handlers.education.financial_literacy.active_passive_income import (
    active_passive_income_menu,
)


# =========================
# بودجه 50/30/20
# =========================

# بودجه 50/30/20
from handlers.education.financial_literacy.budget_50_30_20.menu import (
    budget_50_30_20_menu,
)


# =========================
# منوی اصلی سواد مالی
# =========================

async def financial_literacy_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "💰 آموزش سواد مالی\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=financial_literacy_keyboard,
    )


# =========================
# Router سواد مالی
# =========================

async def financial_literacy_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    # =========================
    # بهره مرکب
    # =========================

    if text == "🧮 بهره مرکب":
        return await compound_interest(update, context)


    # =========================
    # ارزش زمانی پول
    # =========================

    elif text == "⏳ ارزش زمانی پول":
        return await time_value_menu(update, context)


    # =========================
    # قدرت خرید
    # =========================

    elif text == "💵 قدرت خرید":
        return await purchasing_power_menu(update, context)


    # =========================
    # پس‌انداز هدف
    # =========================

    elif text == "🎯 پس‌انداز هدف":
        return await goal_saving_menu(update, context)


    # =========================
    # ROI
    # =========================

    elif text == "📈 ROI":
        return await roi_menu(update, context)


    # =========================
    # بازده واقعی
    # =========================

    elif text == "📊 بازده واقعی":
        return await real_return_menu(update, context)


    # =========================
    # تنوع‌بخشی سرمایه
    # =========================

    elif text == "🧺 تنوع‌بخشی سرمایه":
        return await diversification_menu(update, context)


    # =========================
    # درآمد فعال و غیرفعال
    # =========================

    elif text == "💼 درآمد فعال و غیرفعال":
        return await active_passive_income_menu(update, context)


    # =========================
    # بودجه 50/30/20
    # =========================

    elif text == "📋 بودجه 50/30/20":
        return await budget_50_30_20_menu(update, context)