from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def active_passive_income_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_states[chat_id] = "active_income"

    await update.message.reply_text(
        "💼 درآمد فعال ماهانه خود را وارد کنید (تومان):"
    )


async def active_passive_income_input(
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

        if state == "active_income":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["active"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "passive_income"

            await update.message.reply_text(
                "💰 درآمد غیرفعال ماهانه خود را وارد کنید (تومان):"
            )

            return

        elif state == "passive_income":

            user_data[chat_id]["passive"] = float(
                update.message.text.replace(",", "")
            )

            active = user_data[chat_id]["active"]
            passive = user_data[chat_id]["passive"]

            total = active + passive

            passive_percent = (passive / total) * 100 if total else 0

            if passive_percent >= 50:
                status = "🟢 وضعیت عالی"
            elif passive_percent >= 20:
                status = "🟡 وضعیت متوسط"
            else:
                status = "🔴 نیاز به افزایش درآمد غیرفعال"

            await update.message.reply_text(
                f"""
💼 نتیجه تحلیل درآمد

━━━━━━━━━━━━━━

💼 درآمد فعال:

{active:,.0f} تومان

💰 درآمد غیرفعال:

{passive:,.0f} تومان

━━━━━━━━━━━━━━

💵 مجموع درآمد:

{total:,.0f} تومان

━━━━━━━━━━━━━━

📊 سهم درآمد غیرفعال:

{passive_percent:.2f} %

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