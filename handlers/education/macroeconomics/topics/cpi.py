from telegram import Update
from telegram.ext import ContextTypes


async def cpi(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = """
📊 شاخص قیمت مصرف‌کننده (CPI)

شاخص قیمت مصرف‌کننده یا Consumer Price Index یکی از مهم‌ترین شاخص‌های اقتصادی است که میانگین تغییرات قیمت کالاها و خدمات مصرفی خانوارها را در طول زمان اندازه‌گیری می‌کند. این شاخص میزان تورم و تغییر هزینه‌های زندگی را نشان می‌دهد و معمولاً به صورت ماهانه منتشر می‌شود.

🎯 اهمیت:
CPI یکی از مهم‌ترین گزارش‌های اقتصادی جهان است و تأثیر مستقیمی بر نرخ بهره، ارزش دلار، قیمت طلا، بازار سهام و تصمیمات بانک‌های مرکزی مانند فدرال رزرو دارد.
"""

    await update.message.reply_text(text)