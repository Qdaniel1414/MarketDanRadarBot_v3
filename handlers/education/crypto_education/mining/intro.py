from telegram import Update
from telegram.ext import ContextTypes


async def mining_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "⚡ ماینینگ چیست؟\n\n"

        "ماینینگ (Mining) فرآیند تأیید تراکنش‌ها و ایجاد بلاک‌های جدید در برخی شبکه‌های بلاکچینی است.\n\n"

        "ماینرها با استفاده از قدرت پردازشی دستگاه‌های خود، معادلات رمزنگاری را حل می‌کنند.\n\n"

        "در ازای این کار، پاداش دریافت می‌کنند.\n\n"

        "مهم‌ترین ارز قابل استخراج:\n\n"

        "₿ بیت‌کوین\n\n"

        "تجهیزات استخراج:\n\n"

        "🖥 دستگاه ASIC\n"
        "💡 برق\n"
        "❄ سیستم خنک‌کننده\n"
        "🌐 اینترنت پایدار\n\n"

        "مزایا:\n\n"

        "✅ دریافت پاداش بلاک\n"
        "✅ مشارکت در امنیت شبکه\n\n"

        "معایب:\n\n"

        "❌ مصرف برق بالا\n"
        "❌ هزینه خرید دستگاه\n"
        "❌ استهلاک تجهیزات\n"
        "❌ وابستگی سود به قیمت بیت‌کوین\n"
        "❌ سختی شبکه\n\n"

        "انواع استخراج:\n\n"

        "⛏ Solo Mining\n"
        "👥 Pool Mining\n"
        "☁ Cloud Mining\n\n"

        "🎯 امروزه بیشتر استخراج بیت‌کوین توسط استخرهای استخراج انجام می‌شود."
    )

    await update.message.reply_text(text)