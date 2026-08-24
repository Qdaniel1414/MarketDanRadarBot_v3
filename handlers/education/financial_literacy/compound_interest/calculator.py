from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

INITIAL = 1
MONTHLY = 2
RATE = 3
YEARS = 4

user_data = {}


async def compound_interest_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "💰 سرمایه اولیه را وارد کنید:\n\n"
        "مثال:\n"
        "100000000"
    )

    return INITIAL


async def get_initial(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user_data["initial"] = float(update.message.text)

    await update.message.reply_text(
        "💵 واریز ماهانه را وارد کنید.\n\n"
        "اگر ندارید عدد 0 را وارد کنید."
    )

    return MONTHLY


async def get_monthly(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user_data["monthly"] = float(update.message.text)

    await update.message.reply_text(
        "📈 نرخ سود سالانه (%) را وارد کنید."
    )

    return RATE


async def get_rate(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user_data["rate"] = float(update.message.text)

    await update.message.reply_text(
        "📅 مدت سرمایه گذاری (سال) را وارد کنید."
    )

    return YEARS

async def get_years(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user_data["years"] = float(update.message.text)

    initial = user_data["initial"]
    monthly = user_data["monthly"]
    rate = user_data["rate"] / 100
    years = user_data["years"]

    # نرخ ماهانه
    monthly_rate = rate / 12

    # تعداد ماه
    months = int(years * 12)

    future_initial = initial * ((1 + monthly_rate) ** months)

    if monthly > 0:
        future_monthly = monthly * (
            (((1 + monthly_rate) ** months) - 1) / monthly_rate
        )
    else:
        future_monthly = 0

    final_value = future_initial + future_monthly

    total_deposit = initial + (monthly * months)

    profit = final_value - total_deposit

    growth = (profit / total_deposit) * 100

    text = f"""
💹 نتیجه محاسبه بهره مرکب

━━━━━━━━━━━━━━

💰 سرمایه اولیه:
{initial:,.0f} تومان

💵 مجموع واریزی:
{total_deposit:,.0f} تومان

📈 سود کسب شده:
{profit:,.0f} تومان

🏆 سرمایه نهایی:
{final_value:,.0f} تومان

📊 درصد رشد:
{growth:.2f} %

━━━━━━━━━━━━━━

🎯 هرچه زمان بیشتر باشد،
قدرت بهره مرکب بیشتر می‌شود.
"""

    await update.message.reply_text(text)

    return ConversationHandler.END

compound_interest_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex(r"^🧮 ماشین حساب بهره مرکب$"),
            compound_interest_calculator,
        )
    ],
    states={
        INITIAL: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_initial,
            )
        ],
        MONTHLY: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_monthly,
            )
        ],
        RATE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_rate,
            )
        ],
        YEARS: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_years,
            )
        ],
    },
    fallbacks=[],
)