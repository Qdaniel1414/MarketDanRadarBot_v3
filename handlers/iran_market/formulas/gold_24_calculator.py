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

from services.nosan_api import get_gold24_price


async def gold24_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(
        "🥇 محاسبه طلای ۲۴ عیار\n\n"
        "وزن طلا را وارد کنید (گرم):",
        reply_markup=cancel_keyboard,
    )

    return WEIGHT


async def get_weight(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:
        context.user_data["weight"] = float(update.message.text)
    except ValueError:
        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )
        return WEIGHT

    await update.message.reply_text(
        "💰 اجرت را وارد کنید (درصد):"
    )

    return OJRAT


async def get_ojrat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:
        context.user_data["ojrat"] = float(update.message.text)
    except ValueError:
        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )
        return OJRAT

    await update.message.reply_text(
        "📈 سود فروشنده را وارد کنید (درصد):"
    )

    return SOOD


async def get_sood(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:
        context.user_data["sood"] = float(update.message.text)
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
        context.user_data["tax"] = float(update.message.text)
    except ValueError:
        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )
        return TAX

    try:
        price24 = get_gold24_price()
    except Exception:
        await update.message.reply_text(
            "❌ دریافت قیمت لحظه‌ای از نوسان انجام نشد."
        )
        return ConversationHandler.END

    weight = context.user_data["weight"]
    ojrat = context.user_data["ojrat"]
    sood = context.user_data["sood"]
    tax = context.user_data["tax"]

    gold_value = weight * price24
    ojrat_value = gold_value * ojrat / 100
    sood_value = (gold_value + ojrat_value) * sood / 100
    tax_value = sood_value * tax / 100

    final_price = (
        gold_value
        + ojrat_value
        + sood_value
        + tax_value
    )

    await update.message.reply_text(
        f"""
📊 نتیجه محاسبه طلای ۲۴ عیار

⚖️ وزن:
{weight} گرم

💵 قیمت هر گرم:
{price24:,.0f} تومان

💰 ارزش طلای خام:
{gold_value:,.0f} تومان

🛠 اجرت:
{ojrat_value:,.0f} تومان

📈 سود:
{sood_value:,.0f} تومان

🧾 مالیات:
{tax_value:,.0f} تومان

━━━━━━━━━━━━━━━

✅ قیمت نهایی:
{final_price:,.0f} تومان
"""
    )

    return ConversationHandler.END