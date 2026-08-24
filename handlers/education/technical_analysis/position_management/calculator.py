from telegram import Update
from telegram.ext import ContextTypes

user_states = {}
user_data = {}


async def position_management_calculator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    user_id = update.effective_user.id

    user_states[user_id] = "pm_capital"

    print("STATE -> pm_capital")

    await update.message.reply_text(
        "💰 سرمایه کل خود را وارد کنید:\n\n"
        "مثال:\n"
        "100000000"
    )


async def position_management_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("POSITION INPUT EXECUTED")

    if update.message is None:
        return

    user_id = update.effective_user.id

    print("USER:", user_id)

    print("CURRENT STATES:", user_states)

    if user_id not in user_states:
        print("USER NOT FOUND IN STATES")
        return

    state = user_states[user_id]

    print("CURRENT STATE:", state)

    try:

        if state == "pm_capital":

            print("INSIDE pm_capital")

            capital = float(update.message.text.replace(",", ""))

            user_data[user_id] = {
                "capital": capital
            }

            user_states[user_id] = "pm_risk"

            print("NEXT STATE -> pm_risk")

            await update.message.reply_text(
                "📊 درصد ریسک معامله را وارد کنید:\n\n"
                "مثال:\n"
                "1"
            )

            return

        elif state == "pm_risk":

            print("INSIDE pm_risk")

            risk_percent = float(update.message.text)

            print("RISK =", risk_percent)

            user_data[user_id]["risk"] = risk_percent

            user_states[user_id] = "pm_entry"

            print("NEXT STATE -> pm_entry")

            print("SENDING ENTRY MESSAGE")

            await update.message.reply_text(
                "📈 قیمت ورود را وارد کنید:"
            )

            return

        elif state == "pm_entry":

            print("INSIDE pm_entry")

            entry = float(update.message.text)

            user_data[user_id]["entry"] = entry

            user_states[user_id] = "pm_stop"

            print("NEXT STATE -> pm_stop")

            await update.message.reply_text(
                "🛑 حد ضرر را وارد کنید:"
            )

            return

        elif state == "pm_stop":

            print("INSIDE pm_stop")

            stop = float(update.message.text)

            capital = user_data[user_id]["capital"]
            risk_percent = user_data[user_id]["risk"]
            entry = user_data[user_id]["entry"]

            risk_money = capital * risk_percent / 100

            difference = abs(entry - stop)

            if difference == 0:

                await update.message.reply_text(
                    "❌ اختلاف ورود و حد ضرر نمی‌تواند صفر باشد."
                )

                del user_states[user_id]
                del user_data[user_id]

                return

            position_size = risk_money / difference

            await update.message.reply_text(

                f"━━━━━━━━━━━━━━\n\n"

                f"💰 سرمایه:\n"
                f"{capital:,.0f}\n\n"

                f"📊 درصد ریسک:\n"
                f"{risk_percent}%\n\n"

                f"⚠️ ریسک مجاز:\n"
                f"{risk_money:,.0f}\n\n"

                f"📈 قیمت ورود:\n"
                f"{entry}\n\n"

                f"🛑 حد ضرر:\n"
                f"{stop}\n\n"

                f"📏 اختلاف:\n"
                f"{difference}\n\n"

                f"✅ حجم مجاز معامله:\n"
                f"{position_size:.2f}\n\n"

                f"━━━━━━━━━━━━━━\n\n"

                f"🎯 هیچ معامله‌ای نباید بیشتر از "
                f"{risk_percent}% سرمایه شما را در معرض ریسک قرار دهد."
            )

            del user_states[user_id]
            del user_data[user_id]

            print("FINISHED")

            return

    except Exception as e:

        print("ERROR:", e)

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )