from telegram import Update
from telegram.ext import ContextTypes

from services.nosan_api import (
    get_gold18_price,
    get_ounce_usd,
)


async def dollar_by_gold(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    # قیمت هر گرم طلای ۱۸ عیار (تومان)
    gold18 = get_gold18_price()

    # قیمت اونس جهانی (دلار)
    ounce = get_ounce_usd()

    # قیمت هر گرم طلای خالص 24 عیار (دلار)
    pure_gold_per_gram = ounce / 31.1035

    # قیمت هر گرم طلای 18 عیار (دلار)
    gold18_usd = pure_gold_per_gram * 0.75

    # ارزش ذاتی دلار
    intrinsic_usd = gold18 / gold18_usd

    text = (
        "💰 ارزش ذاتی دلار بر اساس طلای ۱۸ عیار\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"🥇 قیمت هر گرم طلای ۱۸ عیار:\n"
        f"{gold18:,.0f} تومان\n\n"

        f"🌍 قیمت اونس جهانی:\n"
        f"{ounce:,.2f} دلار\n\n"

        f"⚖️ قیمت هر گرم طلای خالص:\n"
        f"{pure_gold_per_gram:,.2f} دلار\n\n"

        f"💎 قیمت هر گرم طلای ۱۸ عیار:\n"
        f"{gold18_usd:,.2f} دلار\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💵 ارزش ذاتی هر دلار:\n\n"
        f"{intrinsic_usd:,.0f} تومان"
    )

    await update.message.reply_text(text)