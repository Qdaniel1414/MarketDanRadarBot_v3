from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from handlers.iran_market.dollar_calculator.dollar_states import DIRHAM


async def dollar_from_dirham_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return ConversationHandler.END

    await update.message.reply_text(
        "🇦🇪 محاسبه دلار از درهم\n\n"
        "💡 لطفاً قیمت روز هر درهم را به تومان وارد کنید:\n\n"
        "مثال:\n"
        "52000",
        reply_markup=ReplyKeyboardMarkup(
            [["🚪 خروج از محاسبه"]],
            resize_keyboard=True,
        ),
    )

    return DIRHAM


async def calculate_dollar_from_dirham(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return ConversationHandler.END

    try:
        text = update.message.text.strip().replace(",", "")
        dirham_price = float(text)

        if dirham_price <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await update.message.reply_text(
            "❌ قیمت درهم نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n"
            "مثال:\n"
            "52000"
        )

        return DIRHAM

    # نرخ برابری دلار و درهم
    USD_AED_RATE = 3.67

    dollar_price = dirham_price * USD_AED_RATE

    result = (
        "💵 نتیجه محاسبه دلار از درهم\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🇦🇪 قیمت درهم:\n"
        f"{dirham_price:,.0f} تومان\n\n"
        f"📐 نرخ برابری دلار به درهم:\n"
        f"{USD_AED_RATE}\n\n"
        "🧮 فرمول:\n"
        "قیمت درهم × 3.67\n\n"
        f"💵 قیمت ضمنی دلار:\n"
        f"{dollar_price:,.0f} تومان\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💡 این عدد، قیمت ضمنی دلار بر اساس قیمت درهم است."
    )

    result_keyboard = ReplyKeyboardMarkup(
        [
            ["🔄 محاسبه مجدد"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )

    await update.message.reply_text(
        result,
        reply_markup=result_keyboard,
    )

    return ConversationHandler.END