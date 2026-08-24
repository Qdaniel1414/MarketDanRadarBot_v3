from telegram import Update
from telegram.ext import ContextTypes


async def trading_psychology_example(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "📈 مثال واقعی روانشناسی معامله\n\n"

        "فرض کنید:\n\n"

        "💰 سرمایه شما:\n"
        "100,000,000 تومان\n\n"

        "📉 سه معامله پشت سر هم ضرر کرده‌اید.\n\n"

        "احساس شما:\n"
        "😡 باید ضرر را جبران کنم!\n\n"

        "پس:\n"
        "حجم معامله بعدی را\n"
        "۳ برابر می‌کنید.\n\n"

        "نتیجه:\n"
        "❌ معامله چهارم نیز ضرر می‌شود.\n\n"

        "حالا:\n"
        "بیشتر سرمایه از بین رفته است.\n\n"

        "🎯 معامله‌گر حرفه‌ای چه کار می‌کند؟\n\n"

        "✅ حجم معامله را افزایش نمی‌دهد.\n"
        "✅ چند ساعت یا چند روز استراحت می‌کند.\n"
        "✅ دوباره طبق استراتژی وارد بازار می‌شود.\n\n"

        "قانون طلایی:\n"
        "هرگز اجازه نده احساسات تصمیم بگیرند."
    )

    await update.message.reply_text(text)