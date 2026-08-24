from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_loan(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["amount"] = None
    context.user_data["rate"] = None
    context.user_data["months"] = None

    await update.message.reply_text(
        "🏦 ماشین حساب قسط و وام\n\n"
        "💰 مبلغ وام را وارد کنید:"
    )

    return 9


async def loan_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:

        value = float(
            update.message.text.replace(",", "")
        )

    except:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )

        return 9


    if context.user_data["amount"] is None:

        context.user_data["amount"] = value

        await update.message.reply_text(
            "📈 سود سالیانه (%) را وارد کنید:"
        )

        return 9


    if context.user_data["rate"] is None:

        context.user_data["rate"] = value

        await update.message.reply_text(
            "📅 مدت بازپرداخت (ماه) را وارد کنید:"
        )

        return 9


    context.user_data["months"] = value

    amount = context.user_data["amount"]
    annual_rate = context.user_data["rate"]
    months = int(context.user_data["months"])

    monthly_rate = annual_rate / 12 / 100

    if monthly_rate == 0:

        installment = amount / months

    else:

        installment = (
            amount
            * monthly_rate
            * (1 + monthly_rate) ** months
        ) / (
            (1 + monthly_rate) ** months - 1
        )

    total_payment = installment * months
    total_profit = total_payment - amount

    await update.message.reply_text(
        f"""🏦 نتیجه محاسبه وام

💰 مبلغ وام:
{amount:,.0f} تومان

📈 سود سالیانه:
{annual_rate:.2f}%

📅 مدت:
{months} ماه

━━━━━━━━━━━━━━

💳 قسط ماهانه:
{installment:,.0f} تومان

💵 مجموع بازپرداخت:
{total_payment:,.0f} تومان

📈 مجموع سود:
{total_profit:,.0f} تومان
"""
    )

    context.user_data.clear()

    return ConversationHandler.END