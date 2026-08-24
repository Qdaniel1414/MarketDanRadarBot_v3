from telegram import Update
from telegram.ext import ContextTypes

from utils.navigation import BACK_HOME


async def app_info_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "ℹ️ اطلاعات برنامه\n\n"
        "📡 MARKET DAN RADAR | مارکت دن رادار\n\n"
        "🤖 این ربات با هدف ارائه ابزارها، "
        "آموزش‌ها و اطلاعات کاربردی در حوزه "
        "اقتصاد و بازارهای مالی طراحی شده است.\n\n"
        "📚 بخش‌های اصلی ربات:\n"
        "• 📊 قیمت‌های لحظه‌ای بازار\n"
        "• 🧮 ماشین حساب‌ها\n"
        "• 📚 آموزش‌ها\n"
        "• 🤖 دستیار هوشمند\n"
        "• 🇮🇷 بازار ایران\n"
        "• 🌍 بازارهای بین‌المللی\n"
        "• 👤 پروفایل کاربر\n"
        "• 🌐 سایت‌های کاربردی بازارهای مالی\n\n"
        "🎯 هدف ما این است که ابزارها و "
        "اطلاعات کاربردی بازارهای مالی را "
        "در یک محیط ساده و قابل استفاده "
        "در اختیار شما قرار دهیم.\n\n"
        "📱 شبکه‌های اجتماعی:\n\n"
        "📲 تلگرام:\n"
        "https://t.me/MarketDanRadar\n\n"
        "📸 اینستاگرام:\n"
        "https://www.instagram.com/market_dan_radar\n\n"
        "🟢 بله:\n"
        "https://ble.ir/MarketDanRadar\n\n"
        "𝕏 X:\n"
        "https://x.com/MarketDanRadar\n\n"
        "💡 برای بازگشت به صفحه اصلی، "
        "دکمه 🏠 خانه را انتخاب کنید."
    )

    await update.message.reply_text(
        text,
        reply_markup=BACK_HOME,
    )