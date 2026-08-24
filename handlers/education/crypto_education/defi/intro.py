from telegram import Update
from telegram.ext import ContextTypes


async def defi_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "💳 دیفای (DeFi) چیست؟\n\n"

        "DeFi مخفف عبارت Decentralized Finance است.\n\n"

        "دیفای مجموعه‌ای از خدمات مالی است که بدون بانک و واسطه، "
        "فقط با استفاده از قراردادهای هوشمند روی بلاکچین انجام می‌شود.\n\n"

        "امکانات دیفای:\n\n"

        "💰 وام گرفتن و وام دادن\n"
        "💱 صرافی‌های غیرمتمرکز (DEX)\n"
        "🏦 استیکینگ\n"
        "🌾 ییلد فارمینگ (Yield Farming)\n"
        "💵 کسب سود از دارایی‌ها\n\n"

        "مزایا:\n\n"

        "✅ بدون واسطه\n"
        "✅ دسترسی جهانی\n"
        "✅ شفافیت بالا\n"
        "✅ کنترل کامل دارایی توسط کاربر\n\n"

        "ریسک‌ها:\n\n"

        "❌ هک قراردادهای هوشمند\n"
        "❌ باگ نرم‌افزاری\n"
        "❌ نوسانات شدید بازار\n"
        "❌ ریسک لیکوئید شدن در وام‌ها\n\n"

        "🎯 بزرگ‌ترین اکوسیستم دیفای روی شبکه اتریوم شکل گرفته است."
    )

    await update.message.reply_text(text)