from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from .states import (
    BUY_PRICE,
    CURRENT_PRICE,
    AMOUNT,
)


# =====================================
# شروع
# =====================================

async def profit_loss_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        """
📈 ماشین حساب سود و زیان کریپتو

مرحله ۱ از ۳

💰 قیمت خرید هر واحد را وارد کنید:

مثال:

60000
"""
    )

    return BUY_PRICE


# =====================================
# مرحله اول
# =====================================

async def profit_loss_buy_price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["buy_price"] = float(
            update.message.text.replace(",", "")
        )

        await update.message.reply_text(
            """
مرحله ۲ از ۳

📊 قیمت فعلی یا فروش را وارد کنید:

مثال:

70000
"""
        )

        return CURRENT_PRICE

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return BUY_PRICE


# =====================================
# مرحله دوم
# =====================================

async def profit_loss_current_price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        context.user_data["current_price"] = float(
            update.message.text.replace(",", "")
        )

        await update.message.reply_text(
            """
مرحله ۳ از ۳

🪙 مقدار ارز خریداری شده را وارد کنید:

مثال:

0.5
"""
        )

        return AMOUNT

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return CURRENT_PRICE


# =====================================
# مرحله سوم
# =====================================

async def profit_loss_amount(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        amount = float(
            update.message.text.replace(",", "")
        )

        buy_price = context.user_data["buy_price"]
        current_price = context.user_data["current_price"]

        buy_value = buy_price * amount
        current_value = current_price * amount

        profit = current_value - buy_value

        percent = (
            (current_price - buy_price)
            / buy_price
        ) * 100

        status = "📈 سود" if profit >= 0 else "📉 ضرر"

        await update.message.reply_text(
f"""
📊 نتیجه سود و زیان کریپتو

━━━━━━━━━━━━

💰 قیمت خرید:
{buy_price:,.2f}$

📊 قیمت فروش:
{current_price:,.2f}$

🪙 مقدار:
{amount}

━━━━━━━━━━━━

{status}

{profit:,.2f}$

درصد تغییر:

{percent:.2f}%

━━━━━━━━━━━━

💵 ارزش اولیه:
{buy_value:,.2f}$

💎 ارزش فعلی:
{current_value:,.2f}$
"""
        )

        context.user_data.clear()

        return ConversationHandler.END

    except ValueError:

        await update.message.reply_text(
            "❌ لطفاً فقط عدد وارد کنید."
        )

        return AMOUNT


# =====================================
# ConversationHandler
# =====================================

profit_loss_handler = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(r"^📈 سود و زیان کریپتو$"),
            profit_loss_intro,
        )
    ],

    states={

        BUY_PRICE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                profit_loss_buy_price,
            )
        ],

        CURRENT_PRICE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                profit_loss_current_price,
            )
        ],

        AMOUNT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                profit_loss_amount,
            )
        ],

    },

    fallbacks=[],

)