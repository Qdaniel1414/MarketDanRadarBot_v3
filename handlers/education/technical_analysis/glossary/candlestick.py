from telegram import Update
from telegram.ext import ContextTypes


async def candlestick_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🕯 کندل (Candlestick)\n\n"

        "کندل کوچک‌ترین واحد نمایش حرکت قیمت در نمودار است.\n\n"

        "هر کندل شامل ۴ قیمت مهم است:\n\n"

        "🟢 قیمت باز شدن (Open)\n"
        "🔴 قیمت بسته شدن (Close)\n"
        "⬆️ بیشترین قیمت (High)\n"
        "⬇️ کمترین قیمت (Low)\n\n"

        "اگر قیمت بسته شدن بالاتر از قیمت باز شدن باشد:\n"
        "🟢 کندل صعودی است.\n\n"

        "اگر قیمت بسته شدن پایین‌تر از قیمت باز شدن باشد:\n"
        "🔴 کندل نزولی است.\n\n"

        "اجزای کندل:\n\n"

        "📦 بدنه (Body)\n"
        "│ سایه بالا (Upper Shadow)\n"
        "│ سایه پایین (Lower Shadow)\n\n"

        "هر کندل داستان نبرد بین خریداران و فروشندگان را نشان می‌دهد.\n\n"

        "🎯 نکته مهم:\n"
        "تحلیل تکنیکال از همین کندل‌ها آغاز می‌شود."
    )

    await update.message.reply_text(text)