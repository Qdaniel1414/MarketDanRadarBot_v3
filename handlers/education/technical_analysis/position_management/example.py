from telegram import Update
from telegram.ext import ContextTypes


async def position_management_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📈 مثال واقعی مدیریت پوزیشن\n\n"

        "فرض کنید:\n\n"

        "💰 سرمایه شما: 100,000,000 تومان\n"
        "🎯 حداکثر ریسک هر معامله: 2%\n\n"

        "حداکثر مبلغی که مجاز هستید در این معامله از دست بدهید:\n\n"

        "2,000,000 تومان\n\n"

        "اگر حد ضرر شما 5٪ باشد:\n\n"

        "حجم معامله = 40,000,000 تومان\n\n"

        "اگر حد ضرر فعال شود فقط 2 میلیون تومان ضرر می‌کنید.\n\n"

        "✅ این همان چیزی است که معامله‌گران حرفه‌ای انجام می‌دهند."
    )