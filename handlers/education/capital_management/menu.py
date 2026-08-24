from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from keyboards.capital_management_keyboard import (
    capital_management_keyboard,
)

from handlers.education.capital_management.intro import (
    capital_intro,
)

from handlers.education.capital_management.one_percent import (
    one_percent,
)

async def capital_management_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "💼 مدیریت سرمایه\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=capital_management_keyboard,
    )


capital_management_router = MessageHandler(
    filters.Regex("^💰 مدیریت سرمایه چیست؟$"),
    capital_intro,
)
one_percent_router = MessageHandler(
    filters.Regex("^📏 قانون ۱٪$"),
    one_percent,
)