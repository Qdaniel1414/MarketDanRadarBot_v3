from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def time_value_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_states[chat_id] = "tvm_present_value"

    await update.message.reply_text(
        "💰 سرمایه اولیه را وارد کنید (تومان):"
    )


async def time_value_input(
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

        if state == "tvm_present_value":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["pv"] = float(update.message.text.replace(",", ""))

            user_states[chat_id] = "tvm_rate"

            await update.message.reply_text(
                "📈 نرخ سود سالانه (%) را وارد کنید:"
            )

            return

        if state == "tvm_rate":

            user_data[chat_id]["rate"] = float(update.message.text)

            user_states[chat_id] = "tvm_year"

            await update.message.reply_text(
                "📅 تعداد سال را وارد کنید:"
            )

            return

        if state == "tvm_year":

            user_data[chat_id]["year"] = float(update.message.text)

            pv = user_data[chat_id]["pv"]
            r = user_data[chat_id]["rate"] / 100
            n = user_data[chat_id]["year"]

            fv = pv * ((1 + r) ** n)

            await update.message.reply_text(
                f"""
📊 نتیجه محاسبه

💰 سرمایه اولیه:
{pv:,.0f} تومان

📈 نرخ سود:
{r*100:.2f} %

📅 مدت:
{n:.0f} سال

━━━━━━━━━━━━━━

💵 ارزش آینده:

{fv:,.0f} تومان
"""
            )

            user_states.pop(chat_id, None)
            user_data.pop(chat_id, None)

    except Exception:

        await update.message.reply_text(
            "❌ لطفا فقط عدد وارد کنید."
        )