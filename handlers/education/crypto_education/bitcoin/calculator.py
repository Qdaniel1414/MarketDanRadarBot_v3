from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def bitcoin_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    chat_id = update.effective_chat.id

    user_states[chat_id] = "btc_buy"

    await update.message.reply_text(
        "💰 قیمت خرید هر بیت کوین را وارد کنید:"
    )


async def bitcoin_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    chat_id = update.effective_chat.id

    if chat_id not in user_states:
        return

    state = user_states[chat_id]

    try:

        if state == "btc_buy":

            user_data.setdefault(chat_id, {})
            user_data[chat_id]["buy"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "btc_sell"

            await update.message.reply_text(
                "💵 قیمت فروش هر بیت کوین را وارد کنید:"
            )

            return

        elif state == "btc_sell":

            user_data[chat_id]["sell"] = float(
                update.message.text.replace(",", "")
            )

            user_states[chat_id] = "btc_amount"

            await update.message.reply_text(
                "₿ مقدار بیت کوین را وارد کنید:"
            )

            return

        elif state == "btc_amount":

            user_data[chat_id]["amount"] = float(
                update.message.text.replace(",", "")
            )

            buy = user_data[chat_id]["buy"]
            sell = user_data[chat_id]["sell"]
            amount = user_data[chat_id]["amount"]

            cost = buy * amount
            value = sell * amount

            profit = value - cost

            percent = (profit / cost) * 100

            await update.message.reply_text(
                f"""
🧮 نتیجه ماشین حساب بیت کوین

━━━━━━━━━━━━━━

💰 سرمایه اولیه:

{cost:,.2f}

💵 ارزش فروش:

{value:,.2f}

━━━━━━━━━━━━━━

📈 سود / زیان:

{profit:,.2f}

📊 درصد سود:

{percent:.2f} %

━━━━━━━━━━━━━━

₿ مقدار:

{amount}
"""
            )

            user_states.pop(chat_id, None)
            user_data.pop(chat_id, None)

    except:

        await update.message.reply_text(
            "❌ فقط عدد وارد کنید."
        )