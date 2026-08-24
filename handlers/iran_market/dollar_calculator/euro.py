from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from handlers.iran_market.dollar_calculator.dollar_states import (
    EURO,
    EURO_USD,
    RESULT,
)


# =========================================================
# شروع محاسبه دلار از یورو
# =========================================================

async def dollar_from_euro_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    # پاک کردن اطلاعات قبلی
    context.user_data.pop("euro_price", None)
    context.user_data.pop("eur_usd", None)
    context.user_data.pop("implied_dollar", None)

    await update.message.reply_text(
        "🇪🇺 محاسبه دلار از یورو\n\n"
        "لطفاً قیمت روز یورو را به تومان وارد کنید:\n\n"
        "مثال:\n"
        "205000"
    )

    return EURO


# =========================================================
# دریافت قیمت یورو
# =========================================================

async def get_euro_price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:
        text = update.message.text.strip().replace(",", "")

        euro_price = float(text)

        if euro_price <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت یورو نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n\n"
            "مثال:\n"
            "205000"
        )

        return EURO

    context.user_data["euro_price"] = euro_price

    await update.message.reply_text(
        "📊 لطفاً نرخ EUR/USD را وارد کنید:\n\n"
        "مثال:\n"
        "1.16\n\n"
        "💡 یعنی هر ۱ یورو برابر با ۱.۱۶ دلار است."
    )

    return EURO_USD


# =========================================================
# دریافت EUR/USD و محاسبه دلار
# =========================================================

async def get_eur_usd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:
        text = update.message.text.strip().replace(",", "")

        eur_usd = float(text)

        if eur_usd <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ نرخ EUR/USD نامعتبر است.\n\n"
            "لطفاً یک عدد بزرگ‌تر از صفر وارد کنید.\n\n"
            "مثال:\n"
            "1.16"
        )

        return EURO_USD

    context.user_data["eur_usd"] = eur_usd

    # -----------------------------------------------------
    # اطلاعات
    # -----------------------------------------------------

    euro_price = context.user_data.get("euro_price")

    if euro_price is None:
        await update.message.reply_text(
            "❌ اطلاعات قیمت یورو پیدا نشد.\n"
            "لطفاً محاسبه را دوباره شروع کنید."
        )

        return ConversationHandler.END

    # -----------------------------------------------------
    # محاسبه دلار ضمنی
    #
    # قیمت دلار = قیمت یورو ÷ EUR/USD
    # -----------------------------------------------------

    implied_dollar = euro_price / eur_usd

    context.user_data["implied_dollar"] = implied_dollar

    # -----------------------------------------------------
    # خروجی
    # -----------------------------------------------------

    result = (
        "💵 نتیجه ارزش‌گذاری دلار\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🇪🇺 روش محاسبه:\n"
        "دلار از یورو\n\n"

        f"🇪🇺 قیمت یورو:\n"
        f"{euro_price:,.0f} تومان\n\n"

        f"📊 نرخ EUR/USD:\n"
        f"{eur_usd:.4f}\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💵 قیمت ضمنی دلار:\n"
        f"{implied_dollar:,.0f} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 فرمول:\n"
        "قیمت دلار = قیمت یورو ÷ EUR/USD"
    )

    result_keyboard = ReplyKeyboardMarkup(
        [
            ["🔄 محاسبه مجدد"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )

    await update.message.reply_text(
        result,
        reply_markup=result_keyboard,
    )

    return RESULT