from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def budget_50_30_20_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id
    print("🔥 BUDGET CALCULATOR STARTED:", chat_id, user_states)
    user_states[chat_id] = "income"

    await update.message.reply_text(
        "💰 درآمد ماهانه خود را وارد کنید (تومان):"
    )


async def budget_50_30_20_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id
    print("🔥 BUDGET INPUT:", update.message.text, "STATES:", user_states)
    if chat_id not in user_states:
        return

    try:

        income = float(update.message.text.replace(",", ""))

        needs = income * 0.50
        wants = income * 0.30
        invest = income * 0.20

        await update.message.reply_text(
            f"""
📋 بودجه پیشنهادی شما

━━━━━━━━━━━━━━

💰 درآمد:

{income:,.0f} تومان

━━━━━━━━━━━━━━

🏠 نیازها (50٪)

{needs:,.0f}

━━━━━━━━━━━━━━

🎯 خواسته‌ها (30٪)

{wants:,.0f}

━━━━━━━━━━━━━━

📈 سرمایه‌گذاری (20٪)

{invest:,.0f}

━━━━━━━━━━━━━━

✅ این تقسیم‌بندی
یکی از بهترین روش‌های
مدیریت سرمایه شخصی است.
"""
        )

        user_states.pop(chat_id, None)

    except Exception:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )