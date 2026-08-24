from telegram import Update
from telegram.ext import ContextTypes

from keyboards.technical_analysis_keyboard import (
    technical_analysis_keyboard,
)

from handlers.education.technical_analysis.trend import (
    trend_menu,
)

from handlers.education.technical_analysis.support_resistance import (
    support_resistance_menu,
)

from handlers.education.technical_analysis.volume import (
    volume_menu,
)

from handlers.education.technical_analysis.position_management import (
    position_management_menu,
)

from handlers.education.technical_analysis.trading_psychology import (
    trading_psychology_menu,
)

from handlers.education.technical_analysis.glossary import (
    glossary_menu,
)


async def technical_analysis_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📈 آموزش تحلیل تکنیکال\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=technical_analysis_keyboard,
    )


async def technical_analysis_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = update.message.text

    if text == "📊 روند":
        return await trend_menu(update, context)

    elif text == "🧱 حمایت و مقاومت":
        return await support_resistance_menu(update, context)

    elif text == "📦 حجم معاملات":
        return await volume_menu(update, context)

    elif text == "⚖️ مدیریت پوزیشن":
        return await position_management_menu(update, context)

    elif text == "🧠 روانشناسی معامله":
        return await trading_psychology_menu(update, context)

    elif text == "📚 اصطلاحات تحلیل تکنیکال":
        return await glossary_menu(update, context)