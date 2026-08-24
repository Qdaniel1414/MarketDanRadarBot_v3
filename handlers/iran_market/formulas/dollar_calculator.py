from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from keyboards.formulas.gold_18_keyboard import (
    cancel_keyboard,
)

from handlers.iran_market.formulas.dollar_states import (
    WEIGHT,
    SOOD,
    TAX,
)

from services.nosan_api import (
    get_dollar_price,
)


async def dollar_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(

        "💵 محاسبه دلار\n\n"
        "تعداد دلار را وارد کنید:",

        reply_markup=cancel_keyboard,

    )

    return WEIGHT


async def get_weight(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["weight"] = float(
            update.message.text
        )

    except ValueError:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return WEIGHT

    await update.message.reply_text(
        "📈 سود فروشنده را وارد کنید (درصد):"
    )

    return SOOD


async def get_sood(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["sood"] = float(
            update.message.text
        )

    except ValueError:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return SOOD

    await update.message.reply_text(
        "🧾 مالیات را وارد کنید (درصد):"
    )

    return TAX


async def get_tax(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["tax"] = float(
            update.message.text
        )

    except ValueError:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return TAX

    try:

        price = get_dollar_price()

    except Exception:

        await update.message.reply_text(
            "❌ دریافت قیمت لحظه‌ای دلار انجام نشد."
        )

        return ConversationHandler.END

    weight = context.user_data["weight"]
    sood = context.user_data["sood"]
    tax = context.user_data["tax"]

    dollar_value = weight * price

    sood_value = dollar_value * sood / 100

    tax_value = sood_value * tax / 100

    final_price = (
        dollar_value
        + sood_value
        + tax_value
    )

    await update.message.reply_text(

f"""
💵 نتیجه محاسبه دلار

━━━━━━━━━━━━━━━

💵 تعداد دلار:
{weight}

💰 قیمت هر دلار:
{price:,.0f} تومان

━━━━━━━━━━━━━━━

💵 ارزش کل:
{dollar_value:,.0f} تومان

📈 سود:
{sood_value:,.0f} تومان

🧾 مالیات:
{tax_value:,.0f} تومان

━━━━━━━━━━━━━━━

✅ مبلغ نهایی:
{final_price:,.0f} تومان
"""

    )

    return ConversationHandler.END