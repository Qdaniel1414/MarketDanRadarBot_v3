from telegram import Update
from telegram.ext import ContextTypes

from keyboards.market_lab_keyboard import market_lab_keyboard


async def market_lab_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🔬 آزمایشگاه بازار\n\n"
        "در این بخش می‌توانید چند رابطه مهم بازار را به‌صورت ساده بررسی کنید.\n\n"
        "لطفاً یکی از آزمایش‌ها را انتخاب کنید:",
        reply_markup=market_lab_keyboard,
    )


async def dollar_gold_test(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "💵 اثر دلار روی طلا\n\n"
        "اگر اونس جهانی ثابت بماند، افزایش نرخ دلار "
        "معمولاً باعث افزایش ارزش طلای داخلی می‌شود.\n\n"
        "📌 به زبان ساده:\n"
        "دلار ↑ → طلای داخلی ↑\n"
        "دلار ↓ → طلای داخلی ↓\n\n"
        "البته در بازار واقعی، حباب، عرضه و تقاضا و سایر عوامل "
        "هم می‌توانند نتیجه را تغییر دهند."
    )


async def ounce_gold_test(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🥇 اثر اونس روی طلا\n\n"
        "اگر نرخ دلار ثابت بماند، افزایش اونس جهانی "
        "معمولاً باعث افزایش ارزش طلای داخلی می‌شود.\n\n"
        "📌 به زبان ساده:\n"
        "اونس ↑ → طلای داخلی ↑\n"
        "اونس ↓ → طلای داخلی ↓\n\n"
        "برای تحلیل دقیق‌تر باید نرخ دلار و اونس را همزمان بررسی کرد."
    )


async def price_change_test(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "📊 تغییر درصدی قیمت\n\n"
        "فرمول محاسبه تغییر درصدی قیمت:\n\n"
        "درصد تغییر =\n"
        "((قیمت جدید - قیمت قبلی) ÷ قیمت قبلی) × 100\n\n"
        "مثال:\n"
        "اگر قیمت از 100 به 120 برسد:\n\n"
        "((120 - 100) ÷ 100) × 100 = 20٪\n\n"
        "✅ یعنی قیمت ۲۰ درصد افزایش داشته است."
    )


async def compare_scenarios_test(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "⚖️ مقایسه دو سناریو\n\n"
        "سناریوی اول:\n"
        "💵 دلار ↑ + 🥇 اونس ↑\n"
        "➡️ فشار صعودی بیشتری روی طلای داخلی ایجاد می‌شود.\n\n"
        "سناریوی دوم:\n"
        "💵 دلار ↓ + 🥇 اونس ↓\n"
        "➡️ فشار نزولی بیشتری روی طلای داخلی ایجاد می‌شود.\n\n"
        "📌 اگر یکی صعودی و دیگری نزولی باشد، "
        "باید شدت تغییر هرکدام را جداگانه بررسی کرد.\n\n"
        "⚠️ این بخش آموزشی است و پیش‌بینی قطعی بازار نیست."
    )