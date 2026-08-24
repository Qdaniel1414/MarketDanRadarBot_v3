from telegram import Update
from telegram.ext import ContextTypes


async def pullback_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "↩ پولبک (Pullback)\n\n"

        "پولبک یعنی بازگشت موقت قیمت برخلاف روند اصلی، "
        "قبل از ادامه همان روند.\n\n"

        "📈 در روند صعودی:\n"
        "قیمت کمی اصلاح می‌کند و سپس دوباره رشد می‌کند.\n\n"

        "📉 در روند نزولی:\n"
        "قیمت کمی بالا می‌آید و سپس دوباره کاهش پیدا می‌کند.\n\n"

        "✅ پولبک پایان روند نیست.\n"
        "فقط یک اصلاح کوتاه‌مدت است.\n\n"

        "چرا پولبک مهم است؟\n\n"

        "✔ ورود با ریسک کمتر\n"
        "✔ حد ضرر کوچک‌تر\n"
        "✔ نسبت سود به زیان بهتر\n\n"

        "❌ اشتباه رایج:\n"
        "بعضی معامله‌گران پولبک را با تغییر روند اشتباه می‌گیرند.\n\n"

        "🎯 قانون حرفه‌ای:\n"
        "در جهت روند معامله کن و از پولبک برای ورود استفاده کن."
    )

    await update.message.reply_text(text)