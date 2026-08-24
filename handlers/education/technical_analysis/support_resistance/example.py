from telegram import Update
from telegram.ext import ContextTypes


async def support_resistance_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        """
📈 مثال واقعی

فرض کنید قیمت طلا:

4200

⬆️

4250

⬆️

4300

اما هر بار
در 4300
برمی‌گردد.

━━━━━━━━━━━━━━

پس:

4300

مقاومت است.

━━━━━━━━━━━━━━

اگر روزی

4300

شکسته شود

همان سطح

تبدیل به حمایت خواهد شد.
"""
    )