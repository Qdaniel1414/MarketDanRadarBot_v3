from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.inflation_service import (
    get_base_year,
    get_base_usd,
    get_iran_cumulative,
    get_usa_cumulative,
    get_inflation_difference,
    get_theoretical_dollar,
)


async def dollar_by_inflation(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    year = get_base_year()

    base = get_base_usd()

    iran = get_iran_cumulative()

    usa = get_usa_cumulative()

    diff = get_inflation_difference()

    dollar = get_theoretical_dollar()

    text = f"""
📈 <b>ارزش نظری دلار بر اساس تورم تجمعی</b>

━━━━━━━━━━━━━━━━━━━━━━

📅 سال مبنا:
<b>{year}</b>

💵 دلار مبنا:
<b>{base:,}</b> تومان

🇮🇷 تورم تجمعی ایران:
<b>{iran:.0f}%</b>

🇺🇸 تورم تجمعی آمریکا:
<b>{usa:.0f}%</b>

📊 اختلاف تورم:
<b>{diff:.0f}%</b>

━━━━━━━━━━━━━━━━━━━━━━

💰 <b>ارزش نظری هر دلار:</b>

<b>{dollar:,}</b> تومان
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )