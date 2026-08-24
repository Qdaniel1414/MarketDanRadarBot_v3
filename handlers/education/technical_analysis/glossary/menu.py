from telegram import Update
from telegram.ext import ContextTypes

from keyboards.glossary_keyboard import glossary_keyboard

from .candlestick import candlestick_intro
from .timeframe import timeframe_intro
from .trend import glossary_trend_intro
from .volatility import volatility_intro
from .liquidity import liquidity_intro
from .pullback import pullback_intro
from .breakout import breakout_intro
from .fake_breakout import fake_breakout_intro
from .momentum import momentum_intro
from .liquidity_grab import liquidity_grab_intro



# =========================================================
# منوی اصطلاحات تحلیل تکنیکال
# =========================================================

async def glossary_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📚 اصطلاحات تحلیل تکنیکال\n\n"
        "یکی از اصطلاحات زیر را انتخاب کنید:",
        reply_markup=glossary_keyboard,
    )


# =========================================================
# Router اصطلاحات تحلیل تکنیکال
# =========================================================

async def glossary_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    # لاگ برای بررسی اینکه Router اجرا شده یا نه
    print(
        "🔥 GLOSSARY ROUTER CALLED:",
        repr(text),
    )

    # -----------------------------------------------------
    # کندل
    # -----------------------------------------------------

    if text == "🕯 کندل (Candlestick)":
        return await candlestick_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # تایم فریم
    # -----------------------------------------------------

    elif text == "⏰ تایم فریم":
        return await timeframe_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # روند
    # -----------------------------------------------------

    elif text == "📈 روند":
        return await glossary_trend_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # نوسان
    # -----------------------------------------------------

    elif text == "📊 نوسان":
        return await volatility_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # نقدشوندگی
    # -----------------------------------------------------

    elif text == "💧 نقدشوندگی":
        return await liquidity_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # پولبک
    # -----------------------------------------------------

    elif text == "↩ پولبک":
        return await pullback_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # بریک اوت
    # -----------------------------------------------------

    elif text == "🚀 بریک اوت":
        return await breakout_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # فیک بریک اوت
    # -----------------------------------------------------

    elif text == "❌ فیک بریک اوت":
        return await fake_breakout_intro(
            update,
            context,
        )

    # -----------------------------------------------------
    # مومنتوم
    # -----------------------------------------------------

    elif text == "⚡ مومنتوم":
        return await momentum_intro(
            update,
            context,
        )

    

    # -----------------------------------------------------
    # لیکوییدیتی گراب
    # -----------------------------------------------------

    elif text == "💰 لیکوییدیتی گراب":
        return await liquidity_grab_intro(
            update,
            context,
        )


    # -----------------------------------------------------
    # بازگشت
    # -----------------------------------------------------

    elif text == "⬅️ بازگشت":

        from handlers.education.technical_analysis.menu import (
            technical_analysis_menu,
        )

        return await technical_analysis_menu(
            update,
            context,
        )

    # -----------------------------------------------------
    # گزینه ناشناخته
    # -----------------------------------------------------

    print(
        "❌ UNKNOWN GLOSSARY OPTION:",
        repr(text),
    )