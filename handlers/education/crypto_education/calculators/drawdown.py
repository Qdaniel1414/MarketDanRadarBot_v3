from telegram import Update
from telegram.ext import ContextTypes


drawdown_sessions = {}



async def drawdown_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    user_id = update.effective_user.id


    drawdown_sessions[user_id] = {
        "step": "peak"
    }


    await update.message.reply_text(
        """
📉 ماشین حساب افت سرمایه Drawdown


مرحله ۱ از ۲


🔝 بالاترین قیمت یا سقف سرمایه را وارد کنید:


مثال:

70000

(دلار یا هر واحد قیمتی)
"""
    )



async def drawdown_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    user_id = update.effective_user.id


    if user_id not in drawdown_sessions:
        return


    session = drawdown_sessions[user_id]


    text = update.message.text.replace(",", "").strip()



    try:


        # مرحله اول

        if session["step"] == "peak":


            peak = float(text)


            if peak <= 0:
                await update.message.reply_text(
                    "❌ مقدار سقف باید بیشتر از صفر باشد."
                )
                return


            session["peak"] = peak

            session["step"] = "current"



            await update.message.reply_text(
                """
مرحله ۲ از ۲


📍 قیمت یا مقدار فعلی را وارد کنید:


مثال:

50000
"""
            )

            return



        # مرحله دوم

        elif session["step"] == "current":


            current = float(text)

            peak = session["peak"]



            if current < 0:
                await update.message.reply_text(
                    "❌ مقدار فعلی نمی‌تواند منفی باشد."
                )
                return



            drawdown = (
                (peak - current)
                /
                peak
            ) * 100



            recovery = (
                (peak - current)
                /
                current
            ) * 100 if current != 0 else 0



            await update.message.reply_text(
f"""
📉 نتیجه محاسبه Drawdown


━━━━━━━━━━━━


🔝 سقف قبلی:

{peak:,.2f}


📍 مقدار فعلی:

{current:,.2f}


━━━━━━━━━━━━


📉 افت سرمایه:

{drawdown:.2f}%


📈 رشد لازم برای بازگشت به سقف:

{recovery:.2f}%


━━━━━━━━━━━━


💡 نکته:

برای جبران یک افت بزرگ،
درصد رشد مورد نیاز بیشتر از درصد افت است.


مثال:

افت 50٪

نیازمند رشد 100٪ برای برگشت است.


━━━━━━━━━━━━
"""
            )


            drawdown_sessions.pop(
                user_id,
                None
            )



    except ValueError:


        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )