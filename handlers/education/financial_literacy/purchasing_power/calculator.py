from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def purchasing_power_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_states[chat_id] = "pp_money"

    await update.message.reply_text(
        "💰 مبلغ اولیه را وارد کنید (تومان):"
    )


async def purchasing_power_input(
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

        if state == "pp_money":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["money"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "pp_inflation"

            await update.message.reply_text(
                "📈 نرخ تورم سالانه (%) را وارد کنید:"
            )

            return

        elif state == "pp_inflation":

            user_data[chat_id]["inflation"] = float(update.message.text)

            user_states[chat_id] = "pp_year"

            await update.message.reply_text(
                "📅 تعداد سال را وارد کنید:"
            )

            return

        elif state == "pp_year":

            user_data[chat_id]["year"] = float(update.message.text)

            money = user_data[chat_id]["money"]
            inflation = user_data[chat_id]["inflation"] / 100
            year = user_data[chat_id]["year"]

            real_value = money / ((1 + inflation) ** year)

            loss = money - real_value

            await update.message.reply_text(
                f"""
💵 نتیجه محاسبه قدرت خرید

━━━━━━━━━━━━━━

💰 مبلغ اولیه:
{money:,.0f} تومان

📈 نرخ تورم:
{inflation*100:.2f} %

📅 مدت:
{year:.0f} سال

━━━━━━━━━━━━━━

💵 ارزش واقعی پول:

{real_value:,.0f} تومان

━━━━━━━━━━━━━━

📉 کاهش قدرت خرید:

{loss:,.0f} تومان
"""
            )

            user_states.pop(chat_id, None)
            user_data.pop(chat_id, None)

    except Exception:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )