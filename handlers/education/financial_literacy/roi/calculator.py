from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def roi_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_states[chat_id] = "roi_investment"

    await update.message.reply_text(
        "💰 مبلغ سرمایه اولیه را وارد کنید (تومان):"
    )


async def roi_input(
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

        if state == "roi_investment":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["investment"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "roi_final"

            await update.message.reply_text(
                "💵 ارزش نهایی سرمایه را وارد کنید:"
            )

            return

        elif state == "roi_final":

            user_data[chat_id]["final"] = float(
                update.message.text.replace(",", "")
            )

            investment = user_data[chat_id]["investment"]
            final = user_data[chat_id]["final"]

            profit = final - investment

            roi = (profit / investment) * 100

            if roi > 0:
                status = "✅ سرمایه‌گذاری سودآور بوده است."
            elif roi < 0:
                status = "❌ سرمایه‌گذاری زیان‌ده بوده است."
            else:
                status = "➖ بدون سود و زیان."

            await update.message.reply_text(
                f"""
📈 نتیجه محاسبه ROI

━━━━━━━━━━━━━━

💰 سرمایه اولیه:

{investment:,.0f} تومان

💵 ارزش نهایی:

{final:,.0f} تومان

━━━━━━━━━━━━━━

💹 سود / زیان:

{profit:,.0f} تومان

━━━━━━━━━━━━━━

📊 ROI:

{roi:.2f} %

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