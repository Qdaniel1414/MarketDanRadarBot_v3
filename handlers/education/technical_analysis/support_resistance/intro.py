from telegram import Update
from telegram.ext import ContextTypes


async def support_resistance_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
🧱 حمایت و مقاومت

━━━━━━━━━━━━━━

حمایت (Support)

سطحی است که معمولاً
خریداران وارد بازار می‌شوند
و مانع افت قیمت می‌شوند.

━━━━━━━━━━━━━━

مقاومت (Resistance)

سطحی است که
فروشندگان فعال می‌شوند
و مانع رشد قیمت می‌شوند.

━━━━━━━━━━━━━━

وقتی مقاومت شکسته شود
اغلب تبدیل به حمایت می‌شود.

وقتی حمایت شکسته شود
اغلب تبدیل به مقاومت می‌شود.

━━━━━━━━━━━━━━

🎯 تقریبا تمام معامله‌گران دنیا
روزانه از حمایت و مقاومت استفاده می‌کنند.
"""
    )