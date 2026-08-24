from telegram import Update
from telegram.ext import ContextTypes



async def satoshi_converter_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    context.user_data["satoshi_active"] = True


    await update.message.reply_text(
        """
₿ تبدیل ساتوشی ↔ بیت کوین


نوع تبدیل را انتخاب کنید:


1️⃣ ساتوشی به بیت کوین

2️⃣ بیت کوین به ساتوشی


یکی از گزینه‌ها را وارد کنید:

مثال:

1
"""
    )



async def satoshi_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    if not context.user_data.get(
        "satoshi_active"
    ):
        return


    text = update.message.text.strip()



    # انتخاب حالت تبدیل

    if text == "1":

        context.user_data["satoshi_mode"] = "to_btc"


        await update.message.reply_text(
            """
مقدار ساتوشی را وارد کنید:

مثال:

50000000
"""
        )

        return



    elif text == "2":

        context.user_data["satoshi_mode"] = "to_satoshi"


        await update.message.reply_text(
            """
مقدار بیت کوین را وارد کنید:

مثال:

0.5
"""
        )

        return



    try:

        mode = context.user_data.get(
            "satoshi_mode"
        )


        value = float(
            text.replace(",", "")
        )



        if mode == "to_btc":


            btc = value / 100000000


            await update.message.reply_text(
f"""
📊 نتیجه تبدیل


⚡ ساتوشی:

{value:,.0f}


₿ بیت کوین:

{btc:.8f} BTC
"""
            )



        elif mode == "to_satoshi":


            satoshi = value * 100000000


            await update.message.reply_text(
f"""
📊 نتیجه تبدیل


₿ بیت کوین:

{value} BTC


⚡ ساتوشی:

{satoshi:,.0f}
"""
            )


        context.user_data.pop(
            "satoshi_active",
            None
        )

        context.user_data.pop(
            "satoshi_mode",
            None
        )


    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً مقدار عددی وارد کنید."
        )