from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from keyboards.formulas.gold_18_keyboard import (
    cancel_keyboard,
)

from handlers.iran_market.formulas.ons_states import (
    WEIGHT,
    SOOD,
    TAX,
)

from services.nosan_api import (
    get_ounce_usd,
    get_ounce_toman,
)


async def ons_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(

        "🌍 محاسبه انس جهانی\n\n"
        "وزن را وارد کنید (اونس):",

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

        price_usd = get_ounce_usd()
        price_toman = get_ounce_toman()

    except Exception:

        await update.message.reply_text(
            "❌ دریافت قیمت لحظه‌ای انجام نشد."
        )

        return ConversationHandler.END

    weight = context.user_data["weight"]
    sood = context.user_data["sood"]
    tax = context.user_data["tax"]

    gold_value_usd = weight * price_usd
    gold_value_toman = weight * price_toman

    sood_value = (
        gold_value_toman * sood / 100
    )

    tax_value = (
        sood_value * tax / 100
    )

    final_price = (
        gold_value_toman
        + sood_value
        + tax_value
    )

    await update.message.reply_text(

f"""
🌍 نتیجه محاسبه انس جهانی

━━━━━━━━━━━━━━━

⚖️ وزن:
{weight} اونس

💵 قیمت هر اونس:
{price_usd:,.2f} دلار

🇮🇷 قیمت هر اونس:
{price_toman:,.0f} تومان

━━━━━━━━━━━━━━━

💰 ارزش دلاری:
{gold_value_usd:,.2f} دلار

💰 ارزش ریالی:
{gold_value_toman:,.0f} تومان

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