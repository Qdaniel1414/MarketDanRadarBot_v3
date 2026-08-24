from telegram import Update
from telegram.ext import ContextTypes


async def fake_breakout_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "❌ فیک بریک اوت (Fake Breakout)\n\n"

        "فیک بریک اوت یعنی قیمت ظاهراً یک حمایت یا مقاومت را می‌شکند، "
        "اما خیلی سریع دوباره به داخل محدوده قبلی برمی‌گردد.\n\n"

        "📈 مثال:\n"
        "قیمت مقاومت را می‌شکند.\n"
        "بسیاری از معامله‌گران خرید می‌کنند.\n"
        "اما قیمت ناگهان برمی‌گردد و سقوط می‌کند.\n\n"

        "این همان فیک بریک اوت است.\n\n"

        "نشانه‌های فیک بریک اوت:\n\n"

        "❌ حجم پایین\n"
        "❌ بسته نشدن کندل پشت سطح\n"
        "❌ بازگشت سریع قیمت\n\n"

        "چرا اتفاق می‌افتد؟\n\n"

        "🔹 شکار حد ضرر معامله‌گران\n"
        "🔹 جمع‌آوری نقدینگی\n"
        "🔹 ورود پول هوشمند\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "هر شکستی، بریک اوت واقعی نیست.\n"
        "همیشه منتظر تأیید بمان."
    )

    await update.message.reply_text(text)