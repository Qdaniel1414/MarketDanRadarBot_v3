from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from keyboards.formulas.gold_18_keyboard import (
    cancel_keyboard,
)

from handlers.iran_market.formulas.gold_melted_states import (
    WEIGHT,
    SOOD,
    TAX,
)

from services.nosan_api import (
    get_gold18_price,
)


async def gold_melted_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data.clear()

    await update.message.reply_text(

        "🪙 محاسبه طلای آبشده\n\n"
        "وزن را وارد کنید (گرم):",

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

        price18 = get_gold18_price()

        # قیمت تقریبی هر گرم آبشده
        price = int(price18 * 0.965)

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "❌ دریافت قیمت لحظه‌ای انجام نشد."
        )

        return ConversationHandler.END

    weight = context.user_data["weight"]
    sood = context.user_data["sood"]
    tax = context.user_data["tax"]

    gold_value = weight * price

    sood_value = (
        gold_value * sood / 100
    )

    tax_value = (
        sood_value * tax / 100
    )

    final_price = (
        gold_value
        + sood_value
        + tax_value
    )

    await update.message.reply_text(

        f"""
📊 نتیجه محاسبه طلای آبشده

⚖️ وزن:
{weight} گرم

💵 قیمت هر گرم:
{price:,.0f} تومان

💰 ارزش آبشده:
{gold_value:,.0f} تومان

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