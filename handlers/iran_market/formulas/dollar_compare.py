from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.valuation_service import (
    get_final_dollar_valuation,
)


async def dollar_compare(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    result = get_final_dollar_valuation()

    text = f"""
📊 <b>مقایسه ارزش ذاتی دلار</b>

━━━━━━━━━━━━━━━━━━

🥇 بر اساس طلا
<b>{result["gold"]:,}</b> تومان

📈 بر اساس نقدینگی
<b>{result["liquidity"]:,}</b> تومان

🇮🇷🇺🇸 بر اساس تورم
<b>{result["inflation"]:,}</b> تومان

━━━━━━━━━━━━━━━━━━

⭐ <b>ارزش ذاتی نهایی دلار</b>

💵 <b>{result["final"]:,}</b> تومان

━━━━━━━━━━━━━━━━━━

📌 وزن مدل‌ها

• نقدینگی : 40٪
• طلا : 35٪
• تورم : 25٪
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )