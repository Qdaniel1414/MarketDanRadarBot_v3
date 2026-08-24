from telegram import Update
from telegram.ext import ContextTypes

from services.liquidity_service import (
    intrinsic_dollar,
)


async def dollar_by_liquidity(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    result = intrinsic_dollar()

    text = (

        "📈 ارزش ذاتی دلار بر اساس نقدینگی\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        f"📅 سال مبنا : {result['base_year']}\n"

        f"💵 دلار مبنا : {result['base_usd']:,.0f} تومان\n\n"

        f"🏦 نقدینگی سال مبنا : {result['base_liquidity']:,.0f} همت\n"

        f"🏦 نقدینگی امروز : {result['current_liquidity']:,.0f} همت\n\n"

        f"⚙️ ضریب کالیبراسیون : {result['alpha']}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💰 ارزش ذاتی دلار\n\n"

        f"{result['intrinsic_usd']:,.0f} تومان"

    )

    await update.message.reply_text(text)