from telegram import Update
from telegram.ext import ContextTypes

staking_sessions = {}


async def staking_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    user_id = update.effective_user.id

    staking_sessions[user_id] = {
        "step": "amount"
    }

    print("========== STAKING INTRO ==========")
    print(staking_sessions)

    await update.message.reply_text(
        """
⚡ ماشین حساب سود استیکینگ

مرحله ۱ از ۳

🪙 مقدار ارز استیک شده را وارد کنید:

مثال:

10

(یعنی 10 واحد ETH)
"""
    )


async def staking_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    print("========== STAKING INPUT ==========")

    user_id = update.effective_user.id

    print("User ID:", user_id)
    print("Current Sessions:", staking_sessions)

    if user_id not in staking_sessions:
        print("❌ USER NOT FOUND")
        return

    print("✅ USER FOUND")

    session = staking_sessions[user_id]

    print("Current Step:", session["step"])

    text = update.message.text.replace(",", "").strip()

    try:

        # ==========================
        # مرحله اول
        # ==========================

        if session["step"] == "amount":

            session["amount"] = float(text)
            session["step"] = "apy"

            print(session)

            await update.message.reply_text(
                """
مرحله ۲ از ۳

📈 درصد سود سالانه APY را وارد کنید:

مثال:

5

(یعنی 5 درصد)
"""
            )

            return

        # ==========================
        # مرحله دوم
        # ==========================

        elif session["step"] == "apy":

            session["apy"] = float(text)
            session["step"] = "time"

            print(session)

            await update.message.reply_text(
                """
مرحله ۳ از ۳

⏳ مدت استیکینگ را وارد کنید:

تعداد ماه

مثال:

12
"""
            )

            return

        # ==========================
        # مرحله سوم
        # ==========================

        elif session["step"] == "time":

            months = float(text)

            amount = session["amount"]
            apy = session["apy"]

            profit = (
                amount
                * (apy / 100)
                * (months / 12)
            )

            final_amount = amount + profit

            await update.message.reply_text(
f"""
📊 نتیجه استیکینگ

━━━━━━━━━━━━━━

🪙 سرمایه اولیه:
{amount}

📈 سود سالانه:
{apy}%

⏳ مدت:
{months} ماه

━━━━━━━━━━━━━━

💰 سود:
{profit:.6f} واحد

🪙 موجودی نهایی:
{final_amount:.6f} واحد

━━━━━━━━━━━━━━

⚠️ توجه:
این محاسبه تقریبی است و کارمزدها و تغییرات APY در آن لحاظ نشده است.
"""
            )

            staking_sessions.pop(user_id, None)

            print("SESSION REMOVED")

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )