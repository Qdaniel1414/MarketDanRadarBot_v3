from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def goal_saving_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_states[chat_id] = "goal_target"

    await update.message.reply_text(
        "🎯 مبلغ هدف را وارد کنید (تومان):"
    )


async def goal_saving_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    if chat_id not in user_states:
        return

    state = user_states[chat_id]

    try:

        if state == "goal_target":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["target"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "goal_initial"

            await update.message.reply_text(
                "💰 سرمایه اولیه را وارد کنید:"
            )

            return

        elif state == "goal_initial":

            user_data[chat_id]["initial"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "goal_monthly"

            await update.message.reply_text(
                "💵 مبلغ پس‌انداز ماهانه را وارد کنید:"
            )

            return

        elif state == "goal_monthly":

            user_data[chat_id]["monthly"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "goal_rate"

            await update.message.reply_text(
                "📈 نرخ سود سالانه (%) را وارد کنید:"
            )

            return

        elif state == "goal_rate":

            user_data[chat_id]["rate"] = float(update.message.text)

            user_states[chat_id] = "goal_year"

            await update.message.reply_text(
                "📅 مدت (سال) را وارد کنید:"
            )

            return

        elif state == "goal_year":

            user_data[chat_id]["year"] = float(update.message.text)

            target = user_data[chat_id]["target"]
            initial = user_data[chat_id]["initial"]
            monthly = user_data[chat_id]["monthly"]
            rate = user_data[chat_id]["rate"] / 100 / 12
            months = int(user_data[chat_id]["year"] * 12)

            future_initial = initial * ((1 + rate) ** months)

            future_monthly = (
                monthly * (((1 + rate) ** months - 1) / rate)
                if rate != 0
                else monthly * months
            )

            total = future_initial + future_monthly

            total_saved = initial + (monthly * months)

            profit = total - total_saved

            diff = total - target

            if diff >= 0:
                status = f"✅ شما {diff:,.0f} تومان جلوتر از هدف هستید."
            else:
                status = f"❌ شما {abs(diff):,.0f} تومان تا هدف فاصله دارید."

            await update.message.reply_text(
                f"""
🎯 نتیجه ماشین حساب پس‌انداز هدف

━━━━━━━━━━━━━━

🎯 هدف:
{target:,.0f}

💰 سرمایه اولیه:
{initial:,.0f}

💵 پس‌انداز ماهانه:
{monthly:,.0f}

📈 سود سالانه:
{user_data[chat_id]["rate"]:.2f}%

📅 مدت:
{months//12} سال

━━━━━━━━━━━━━━

💰 سرمایه نهایی:

{total:,.0f}

━━━━━━━━━━━━━━

💹 سود کسب شده:

{profit:,.0f}

━━━━━━━━━━━━━━

{status}
"""
            )

            user_states.pop(chat_id, None)
            user_data.pop(chat_id, None)

    except Exception:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )