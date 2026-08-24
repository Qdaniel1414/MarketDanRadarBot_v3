from telegram import Update
from telegram.ext import ContextTypes


from data.manual_prices import (
    CURRENCY_PRICES,
    GLOBAL_PRICES,
)



async def btc_converter_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    context.user_data["btc_converter_active"] = True


    await update.message.reply_text(
        """
₿ ماشین حساب بیت کوین

مقدار بیت کوین (BTC) را وارد کنید:

مثال:

0.5
"""
    )



async def bitcoin_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("🔥 BTC INPUT RUN")


    if update.message is None:
        return


    if not context.user_data.get(
        "btc_converter_active"
    ):
        return



    try:

        btc = float(
            update.message.text.replace(",", "").strip()
        )


        btc_price = GLOBAL_PRICES["بیت کوین"]

        dollar_price = CURRENCY_PRICES["دلار آمریکا"]



        usd_value = btc * btc_price

        toman_value = usd_value * dollar_price



        await update.message.reply_text(
f"""
📊 نتیجه تبدیل بیت کوین

━━━━━━━━━━━━

₿ مقدار:

{btc} BTC


💵 ارزش دلاری:

{usd_value:,.2f} دلار


🇮🇷 ارزش تومانی:

{toman_value:,.0f} تومان


━━━━━━━━━━━━

📌 قیمت BTC:
{btc_price:,.0f} دلار

💵 نرخ دلار:
{dollar_price:,.0f} تومان
"""
        )


        context.user_data.pop(
            "btc_converter_active",
            None
        )


    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )