from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def start_compound(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    context.user_data.clear()

    context.user_data["capital"] = None
    context.user_data["rate"] = None
    context.user_data["months"] = None

    await update.message.reply_text(
        "📈 ماشین حساب سود مرکب\n\n"
        "💰 سرمایه اولیه را وارد کنید:"
    )

    return 3


async def compound_handler(
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
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return 3


    if context.user_data["capital"] is None:

        context.user_data["capital"] = value

        await update.message.reply_text(
            "📊 درصد سود ماهانه را وارد کنید:"
        )

        return 3


    if context.user_data["rate"] is None:

        context.user_data["rate"] = value

        await update.message.reply_text(
            "📅 تعداد ماه را وارد کنید:"
        )

        return 3


    context.user_data["months"] = int(value)

    capital = context.user_data["capital"]
    rate = context.user_data["rate"] / 100
    months = context.user_data["months"]

    final = capital * ((1 + rate) ** months)

    profit = final - capital

    await update.message.reply_text(
        f"""📈 نتیجه سود مرکب

💰 سرمایه اولیه:
{capital:,.0f}

📊 سود ماهانه:
{rate*100:.2f}%

📅 مدت:
{months} ماه

━━━━━━━━━━━━━━

💵 سود:
{profit:,.0f}

🏦 سرمایه نهایی:
{final:,.0f}
"""
    )

    context.user_data.clear()

    return ConversationHandler.END