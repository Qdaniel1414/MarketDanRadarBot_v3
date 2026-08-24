from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from keyboards.formulas.gold_18_keyboard import cancel_keyboard

from handlers.iran_market.formulas.gold_18_states import (
    WEIGHT,
    OJRAT,
    SOOD,
    TAX,
)

from handlers.iran_market.formulas.gold_formula_engine import (
    calculate_gold18,
)

from services.nosan_api import (
    get_gold18_price,
)


async def gold18_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(

        "🥇 محاسبه طلای ۱۸ عیار\n\n"
        "وزن طلا را وارد کنید (گرم):",

        reply_markup=cancel_keyboard,

    )

    return WEIGHT


async def get_weight(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        weight = float(update.message.text)

    except ValueError:

        await update.message.reply_text(

            "❌ لطفاً فقط عدد وارد کنید."

        )

        return WEIGHT

    context.user_data["weight"] = weight

    await update.message.reply_text(

        "💰 اجرت را وارد کنید (درصد):"

    )

    return OJRAT


async def get_ojrat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        ojrat = float(update.message.text)

    except ValueError:

        await update.message.reply_text(

            "❌ لطفاً فقط عدد وارد کنید."

        )

        return OJRAT

    context.user_data["ojrat"] = ojrat

    await update.message.reply_text(

        "📈 سود فروشنده را وارد کنید (درصد):"

    )

    return SOOD


async def get_sood(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        sood = float(update.message.text)

    except ValueError:

        await update.message.reply_text(

            "❌ لطفاً فقط عدد وارد کنید."

        )

        return SOOD

    context.user_data["sood"] = sood

    await update.message.reply_text(

        "🧾 مالیات را وارد کنید (درصد):"

    )

    return TAX


async def get_tax(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        tax = float(update.message.text)

    except ValueError:

        await update.message.reply_text(

            "❌ لطفاً فقط عدد وارد کنید."

        )

        return TAX

    context.user_data["tax"] = tax

    weight = context.user_data["weight"]
    ojrat = context.user_data["ojrat"]
    sood = context.user_data["sood"]

    # قیمت لحظه‌ای از نوسان
    price_per_gram = get_gold18_price()

    result = calculate_gold18(

        weight=weight,

        price_per_gram=price_per_gram,

        ojrat_percent=ojrat,

        profit_percent=sood,

        tax_percent=tax,

    )

    await update.message.reply_text(

        "📊 نتیجه محاسبه طلای ۱۸ عیار\n\n"

        f"⚖️ وزن: {weight} گرم\n"

        f"💵 قیمت هر گرم:\n"
        f"{price_per_gram:,} تومان\n\n"

        f"💰 ارزش طلای خام:\n"
        f"{result['base_price']:,} تومان\n\n"

        f"🛠 اجرت:\n"
        f"{result['ojrat_amount']:,} تومان\n\n"

        f"📈 سود:\n"
        f"{result['profit_amount']:,} تومان\n\n"

        f"🧾 مالیات:\n"
        f"{result['tax_amount']:,} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━\n"

        f"✅ قیمت نهایی:\n"
        f"{result['final_price']:,} تومان"

    )

    context.user_data.clear()

    return ConversationHandler.END