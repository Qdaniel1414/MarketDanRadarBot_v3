from telegram import Update
from telegram.ext import ContextTypes


async def trend_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
📊 روند (Trend)

━━━━━━━━━━━━━━

روند یعنی جهت کلی حرکت قیمت.

بازار معمولاً
در یکی از سه حالت قرار دارد:

🟢 روند صعودی

🔴 روند نزولی

🟡 روند خنثی

━━━━━━━━━━━━━━

✅ روند صعودی

Higher High
Higher Low

━━━━━━━━━━━━━━

✅ روند نزولی

Lower High
Lower Low

━━━━━━━━━━━━━━

✅ روند خنثی

حرکت قیمت بین
حمایت و مقاومت

━━━━━━━━━━━━━━

🎯 اولین مهارت هر معامله‌گر

تشخیص روند بازار است.
"""
    )