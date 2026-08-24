from telegram import Update
from telegram.ext import ContextTypes

from keyboards.trading_psychology_keyboard import (
    trading_psychology_keyboard,
)

from .intro import trading_psychology_intro
from .example import trading_psychology_example
from .mistakes import trading_psychology_mistakes
from .personality_test import (
    trading_personality_test,
)


async def trading_psychology_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🧠 روانشناسی معامله\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=trading_psychology_keyboard,
    )


async def trading_psychology_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()

    if text == "📘 روانشناسی معامله چیست؟":
        return await trading_psychology_intro(update, context)

    elif text == "🧮 تست شخصیت معامله‌گر":
        print("TEXT =", repr(text))
        return await trading_personality_test(update, context)

    elif text == "📈 مثال واقعی روانشناسی":
        return await trading_psychology_example(update, context)

    elif text == "💡 اشتباهات رایج":
        return await trading_psychology_mistakes(update, context)

    elif text == "⬅️ بازگشت":
        from handlers.education.technical_analysis.menu import (
            technical_analysis_menu,
        )

        return await technical_analysis_menu(update, context)