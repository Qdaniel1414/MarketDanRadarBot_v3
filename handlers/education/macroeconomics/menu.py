from telegram import Update
from telegram.ext import ContextTypes

from keyboards.macroeconomics_keyboard import macroeconomics_keyboard


# ===========================
# منوی اقتصاد کلان
# ===========================

async def macroeconomics_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "🌍 آموزش اقتصاد کلان\n\n"
        "یکی از موضوعات زیر را انتخاب کنید.",
        reply_markup=macroeconomics_keyboard,
    )


# ===========================
# Router اقتصاد کلان
# ===========================

async def macroeconomics_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    # تورم
    if text == "📈 تورم":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # CPI
    elif text == "📊 CPI":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # Core CPI
    elif text == "📉 Core CPI":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # PPI
    elif text == "🏭 PPI":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # GDP
    elif text == "🌍 GDP":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # نرخ بهره
    elif text == "💰 نرخ بهره":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # FOMC
    elif text == "🏦 FOMC":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )

    # Dot Plot
    elif text == "🎯 Dot Plot":
        await update.message.reply_text(
            "🚧 این آموزش در حال آماده‌سازی است."
        )