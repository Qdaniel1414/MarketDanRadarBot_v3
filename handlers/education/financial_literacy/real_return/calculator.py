from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def real_return_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_states[chat_id] = "real_nominal"

    await update.message.reply_text(
        "📈 بازده اسمی (%) را وارد کنید:"
    )


async def real_return_input(
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

        if state == "real_nominal":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["nominal"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "real_inflation"

            await update.message.reply_text(
                "📉 نرخ تورم (%) را وارد کنید:"
            )

            return

        elif state == "real_inflation":

            user_data[chat_id]["inflation"] = float(
                update.message.text.replace(",", "")
            )

            nominal = user_data[chat_id]["nominal"]
            inflation = user_data[chat_id]["inflation"]

            real = nominal - inflation

            if real > 0:
                status = "✅ سرمایه شما قدرت خرید ایجاد کرده است."
            elif real < 0:
                status = "❌ قدرت خرید سرمایه کاهش یافته است."
            else:
                status = "➖ قدرت خرید ثابت مانده است."

            await update.message.reply_text(
                f"""
📊 نتیجه محاسبه بازده واقعی

━━━━━━━━━━━━━━

📈 بازده اسمی:

{nominal:.2f} %

📉 نرخ تورم:

{inflation:.2f} %

━━━━━━━━━━━━━━

💰 بازده واقعی:

{real:.2f} %

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