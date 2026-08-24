from telegram import Update
from telegram.ext import ContextTypes


from data.manual_prices import (
    CURRENCY_PRICES,
    GLOBAL_PRICES,
)



async def eth_converter_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    context.user_data["eth_converter_active"] = True


    await update.message.reply_text(
        """
💎 ماشین حساب اتریوم

مقدار ETH را وارد کنید:

مثال:

2
"""
    )



async def ethereum_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("🔥 ETH INPUT RUN")


    if update.message is None:
        return


    if not context.user_data.get(
        "eth_converter_active"
    ):
        return



    try:

        eth = float(
            update.message.text.replace(",", "").strip()
        )


        eth_price = GLOBAL_PRICES["اتریوم"]

        dollar_price = CURRENCY_PRICES["دلار آمریکا"]



        usd_value = eth * eth_price

        toman_value = usd_value * dollar_price



        await update.message.reply_text(
f"""
📊 نتیجه تبدیل اتریوم

━━━━━━━━━━━━

💎 مقدار:

{eth} ETH


💵 ارزش دلاری:

{usd_value:,.2f} دلار


🇮🇷 ارزش تومانی:

{toman_value:,.0f} تومان


━━━━━━━━━━━━

📌 قیمت ETH:

{eth_price:,.0f} دلار


💵 نرخ دلار:

{dollar_price:,.0f} تومان
"""
        )


        context.user_data.pop(
            "eth_converter_active",
            None
        )


    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )