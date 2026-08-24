from telegram import Update
from telegram.ext import ContextTypes

from .sessions import profit_sessions


async def profit_loss_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    user_id = update.effective_user.id


    profit_sessions[user_id] = {
        "step": "buy_price"
    }


    await update.message.reply_text(
        """
📈 ماشین حساب سود و زیان کریپتو


مرحله ۱ از ۳


💰 قیمت خرید ارز را وارد کنید:


مثال:

60000

(قیمت خرید هر واحد به دلار)
"""
    )



async def profit_loss_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    user_id = update.effective_user.id


    if user_id not in profit_sessions:
        return


    session = profit_sessions[user_id]


    text = update.message.text.replace(",", "").strip()



    try:


        # مرحله اول

        if session["step"] == "buy_price":


            session["buy_price"] = float(text)

            session["step"] = "current_price"


            await update.message.reply_text(
                """
مرحله ۲ از ۳


📊 قیمت فعلی یا فروش را وارد کنید:


مثال:

70000
"""
            )

            return



        # مرحله دوم

        elif session["step"] == "current_price":


            session["current_price"] = float(text)

            session["step"] = "amount"


            await update.message.reply_text(
                """
مرحله ۳ از ۳


🪙 مقدار ارز خریداری شده را وارد کنید:


مثال:

0.5
"""
            )

            return



        # مرحله سوم

        elif session["step"] == "amount":


            amount = float(text)


            buy_price = session["buy_price"]

            current_price = session["current_price"]



            buy_value = buy_price * amount

            current_value = current_price * amount


            profit = current_value - buy_value



            profit_percent = (
                (current_price - buy_price)
                /
                buy_price
            ) * 100



            status = "📈 سود" if profit >= 0 else "📉 ضرر"



            await update.message.reply_text(
f"""
📊 نتیجه سود و زیان کریپتو


━━━━━━━━━━━━


🪙 مقدار ارز:

{amount}


💰 قیمت خرید:

{buy_price:,.2f} دلار


📊 قیمت فعلی:

{current_price:,.2f} دلار


━━━━━━━━━━━━


{status}:


{profit:,.2f} دلار


درصد تغییر:


{profit_percent:.2f}%


━━━━━━━━━━━━


💵 ارزش اولیه:

{buy_value:,.2f} دلار


💎 ارزش فعلی:

{current_value:,.2f} دلار


━━━━━━━━━━━━


⚠️ توجه:

این محاسبه فقط تغییر قیمت را نشان می‌دهد
و کارمزدها و مالیات را شامل نمی‌شود.
"""
            )


            profit_sessions.pop(
                user_id,
                None
            )



    except ValueError:


        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )