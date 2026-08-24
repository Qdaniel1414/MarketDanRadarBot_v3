from telegram import Update
from telegram.ext import ContextTypes

from keyboards.scenario_keyboard import scenario_keyboard


async def scenario_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🧠 تحلیل سناریو\n\n"
        "لطفاً یکی از سناریوهای زیر را انتخاب کنید:",
        reply_markup=scenario_keyboard,
    )


async def bullish_scenario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📈 سناریوی صعودی\n\n"
        "در این سناریو، شرایط بازار به سمت افزایش قیمت‌ها حرکت می‌کند.\n\n"
        "🔎 عوامل مهم:\n"
        "• افزایش تقاضا\n"
        "• بهبود روند قیمت\n"
        "• افزایش قدرت خریداران\n\n"
        "⚠️ این سناریو قطعی نیست و شرایط بازار می‌تواند تغییر کند."
    )


async def bearish_scenario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📉 سناریوی نزولی\n\n"
        "در این سناریو، فشار فروش و ضعف بازار بیشتر می‌شود.\n\n"
        "🔎 عوامل مهم:\n"
        "• افزایش فشار فروش\n"
        "• کاهش تقاضا\n"
        "• شکست حمایت‌های مهم\n\n"
        "⚠️ این سناریو قطعی نیست و شرایط بازار می‌تواند تغییر کند."
    )


async def neutral_scenario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⚖️ سناریوی خنثی\n\n"
        "در این وضعیت، بازار جهت مشخصی ندارد و قیمت می‌تواند در یک محدوده نوسان کند.\n\n"
        "🔎 نشانه‌ها:\n"
        "• تعادل نسبی خریداران و فروشندگان\n"
        "• نبود روند قدرتمند\n"
        "• نوسان در محدوده مشخص\n\n"
        "⚠️ برای تغییر سناریو باید منتظر شکست محدوده مهم بازار بود."
    )


async def dollar_scenario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "💵 سناریوی دلار\n\n"
        "در تحلیل دلار باید عواملی مانند تورم، نقدینگی، سیاست پولی، "
        "عرضه و تقاضا و شرایط اقتصادی را در نظر گرفت.\n\n"
        "📌 افزایش فشار تورمی و رشد تقاضا می‌تواند از دلار حمایت کند.\n\n"
        "⚠️ این تحلیل آموزشی است و پیش‌بینی قطعی قیمت نیست."
    )


async def gold_scenario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🥇 سناریوی طلا\n\n"
        "قیمت طلای داخلی به عوامل مهمی مانند اونس جهانی طلا و نرخ دلار "
        "وابسته است.\n\n"
        "🔎 عوامل مهم:\n"
        "• اونس جهانی\n"
        "• نرخ دلار\n"
        "• تقاضای داخلی\n"
        "• حباب و شرایط بازار\n\n"
        "⚠️ این تحلیل آموزشی است و توصیه خرید یا فروش نیست."
    )


async def bitcoin_scenario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "₿ سناریوی بیت‌کوین\n\n"
        "در تحلیل بیت‌کوین باید روند قیمت، حجم معاملات، مومنتوم، "
        "شرایط کلی بازار کریپتو و وضعیت بازارهای جهانی بررسی شود.\n\n"
        "📌 تغییر روند و افزایش یا کاهش فشار خرید و فروش می‌تواند "
        "سناریوی بازار را تغییر دهد.\n\n"
        "⚠️ این تحلیل آموزشی است و توصیه خرید یا فروش نیست."
    )