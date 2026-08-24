from telegram import Update
from telegram.ext import ContextTypes

from keyboards.education_keyboard import education_keyboard

# مدیریت سرمایه
from handlers.education.capital_management.menu import (
    capital_management_menu,
)

# سواد مالی
from handlers.education.financial_literacy.menu import (
    financial_literacy_menu,
)

# تحلیل تکنیکال
from handlers.education.technical_analysis.menu import (
    technical_analysis_menu,
)

# آموزش ارزهای دیجیتال
from handlers.education.crypto_education.menu import (
    crypto_education_menu,
)

# اقتصاد کلان
from handlers.education.macroeconomics.menu import (
    macroeconomics_menu,
)


async def education_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    print("EDUCATION MENU EXECUTED")
    if update.message is None:
        return

    await update.message.reply_text(
        "📚 بخش آموزش‌ها\n\n"
        "یکی از دسته‌های آموزشی را انتخاب کنید.",
        reply_markup=education_keyboard,
    )


async def education_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    text = update.message.text.strip()

    print("EDUCATION ROUTER:", text)

    if text == "🏠 خانه":
        return


    # مدیریت سرمایه
    if text == "💼 آموزش مدیریت سرمایه":
        return await capital_management_menu(update, context)

    # سواد مالی
    elif text == "💰 آموزش سواد مالی":
        return await financial_literacy_menu(update, context)

    # تحلیل تکنیکال
    elif text == "📈 آموزش تحلیل تکنیکال":
        return await technical_analysis_menu(update, context)

    # آموزش ارزهای دیجیتال
    elif text == "🪙 آموزش ارزهای دیجیتال":
        return await crypto_education_menu(update, context)

    # اقتصاد کلان
    elif text == "🌍 آموزش اقتصاد کلان":
        return await macroeconomics_menu(update, context)

