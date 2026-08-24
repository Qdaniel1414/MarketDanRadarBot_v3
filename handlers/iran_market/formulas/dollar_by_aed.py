from telegram import Update
from telegram.ext import ContextTypes

from services.nosan_api import (
    get_all_prices,
)


async def dollar_by_aed(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    try:

        data = get_all_prices()

        aed = float(data["aed"]["value"])

        dollar_value = aed * 3.6725

    except Exception:

        await update.message.reply_text(
            "❌ دریافت قیمت لحظه‌ای انجام نشد."
        )

        return

    await update.message.reply_text(

f"""
💵 ارزش ذاتی دلار بر اساس درهم

🇦🇪 قیمت لحظه‌ای هر درهم:
{aed:,.0f} تومان

🔢 ضریب تبدیل:
3.6725

━━━━━━━━━━━━━━

💰 ارزش ذاتی هر دلار:

{dollar_value:,.0f} تومان
"""

    )