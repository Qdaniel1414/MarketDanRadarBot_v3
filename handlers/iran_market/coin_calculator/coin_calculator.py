from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from handlers.iran_market.coin_calculator.coin_states import (
    DOLLAR,
    OUNCE,
    COIN_PRICE,
    RESULT,
)


# =========================================================
# مشخصات انواع سکه
# =========================================================

COIN_DATA = {
    "FULL": {
        "name": "🥇 سکه امامی",
        "weight": 8.133,
        "purity": 0.900,
    },
    "HALF": {
        "name": "🥈 نیم سکه",
        "weight": 4.0665,
        "purity": 0.900,
    },
    "QUARTER": {
        "name": "🥉 ربع سکه",
        "weight": 2.03225,
        "purity": 0.900,
    },
    "GRAM": {
        "name": "🪙 سکه گرمی",
        "weight": 1.000,
        "purity": 0.900,
    },
}


# =========================================================
# تبدیل متن دکمه به نوع سکه
# =========================================================

def get_coin_type_from_text(text: str):
    """
    تشخیص نوع سکه بر اساس متن دکمه
    """

    if not text:
        return None

    text = text.strip()

    for coin_type, data in COIN_DATA.items():
        if text == data["name"]:
            return coin_type

    return None


# =========================================================
# Handler انتخاب نوع سکه
# =========================================================

async def get_coin_type(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    coin_type = get_coin_type_from_text(
        update.message.text
    )

    if coin_type is None:

        await update.message.reply_text(
            "❌ نوع سکه نامعتبر است.\n\n"
            "لطفاً یکی از گزینه‌های منوی سکه را انتخاب کنید."
        )

        return None

    # ذخیره نوع سکه
    context.user_data["coin_type"] = coin_type

    coin = COIN_DATA[coin_type]

    await update.message.reply_text(
        f"🥇 سکه انتخاب شد:\n"
        f"{coin['name']}\n\n"
        "💵 لطفاً قیمت دلار روز را به تومان وارد کنید.\n\n"
        "مثال:\n"
        "175000"
    )

    return DOLLAR


# =========================================================
# دریافت قیمت دلار
# =========================================================

async def get_dollar(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:

        text = (
            update.message.text
            .strip()
            .replace(",", "")
            .replace("٬", "")
            .replace(" ", "")
        )

        dollar = float(text)

        if dollar <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت دلار نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n"
            "مثال:\n"
            "175000"
        )

        return DOLLAR

    context.user_data["dollar"] = dollar

    await update.message.reply_text(
        "🌍 لطفاً قیمت اونس جهانی طلا را به دلار وارد کنید.\n\n"
        "مثال:\n"
        "3400"
    )

    return OUNCE


# =========================================================
# دریافت قیمت اونس جهانی
# =========================================================

async def get_ounce(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:

        text = (
            update.message.text
            .strip()
            .replace(",", "")
            .replace("٬", "")
            .replace(" ", "")
            .replace("$", "")
        )

        ounce = float(text)

        if ounce <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت اونس نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n"
            "مثال:\n"
            "3400"
        )

        return OUNCE

    context.user_data["ounce"] = ounce

    coin_type = context.user_data.get("coin_type")

    coin = COIN_DATA.get(coin_type)

    if coin is None:

        await update.message.reply_text(
            "❌ نوع سکه پیدا نشد.\n\n"
            "لطفاً محاسبه را دوباره شروع کنید."
        )

        return ConversationHandler.END

    await update.message.reply_text(
        f"🪙 لطفاً قیمت روز {coin['name']} را به تومان وارد کنید.\n\n"
        "مثال:\n"
        "176000000"
    )

    return COIN_PRICE


# =========================================================
# دریافت قیمت روز سکه
# =========================================================

async def get_coin_price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    try:

        text = (
            update.message.text
            .strip()
            .replace(",", "")
            .replace("٬", "")
            .replace(" ", "")
        )

        coin_price = float(text)

        if coin_price <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت سکه نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n"
            "مثال:\n"
            "176000000"
        )

        return COIN_PRICE

    context.user_data["coin_price"] = coin_price

    # =====================================================
    # دریافت اطلاعات ذخیره‌شده
    # =====================================================

    coin_type = context.user_data.get("coin_type")
    dollar = context.user_data.get("dollar")
    ounce = context.user_data.get("ounce")

    coin = COIN_DATA.get(coin_type)

    if coin is None or dollar is None or ounce is None:

        await update.message.reply_text(
            "❌ اطلاعات محاسبه ناقص است.\n\n"
            "لطفاً محاسبه را دوباره شروع کنید."
        )

        return ConversationHandler.END

    # =====================================================
    # قیمت هر گرم طلای خالص 24 عیار
    #
    # دلار × اونس ÷ 31.1034768
    # =====================================================

    pure_gold_gram_toman = (
        dollar * ounce / 31.1034768
    )

    # =====================================================
    # مقدار طلای خالص موجود در سکه
    #
    # وزن سکه × عیار
    # =====================================================

    pure_gold_weight = (
        coin["weight"] * coin["purity"]
    )

    # =====================================================
    # ارزش ذاتی سکه
    # =====================================================

    intrinsic_value = (
        pure_gold_weight * pure_gold_gram_toman
    )

    # =====================================================
    # حباب سکه
    #
    # قیمت بازار - ارزش ذاتی
    # =====================================================

    bubble = (
        coin_price - intrinsic_value
    )

    # =====================================================
    # درصد حباب
    #
    # حباب ÷ ارزش ذاتی × 100
    # =====================================================

    if intrinsic_value > 0:

        bubble_percent = (
            bubble / intrinsic_value
        ) * 100

    else:

        bubble_percent = 0

    # =====================================================
    # وضعیت حباب
    # =====================================================

    if bubble > 0:

        bubble_status = "🔴 حباب مثبت"

    elif bubble < 0:

        bubble_status = "🟢 حباب منفی"

    else:

        bubble_status = "⚪ بدون حباب"

    # =====================================================
    # خروجی نهایی
    # =====================================================

    result = (
        "🥇 نتیجه محاسبه سکه\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"🪙 نوع سکه:\n"
        f"{coin['name']}\n\n"

        f"⚖️ وزن سکه:\n"
        f"{coin['weight']:.5f} گرم\n\n"

        f"🔰 عیار سکه:\n"
        f"{coin['purity'] * 100:.1f}%\n\n"

        f"💵 قیمت دلار:\n"
        f"{dollar:,.0f} تومان\n\n"

        f"🌍 قیمت اونس جهانی:\n"
        f"${ounce:,.2f}\n\n"

        f"🧈 قیمت هر گرم طلای خالص:\n"
        f"{pure_gold_gram_toman:,.0f} تومان\n\n"

        f"🪙 وزن طلای خالص سکه:\n"
        f"{pure_gold_weight:.5f} گرم\n\n"

        f"💎 ارزش ذاتی سکه:\n"
        f"{intrinsic_value:,.0f} تومان\n\n"

        f"🏷️ قیمت روز سکه:\n"
        f"{coin_price:,.0f} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"💥 حباب سکه:\n"
        f"{bubble:,.0f} تومان\n\n"

        f"📊 درصد حباب:\n"
        f"{bubble_percent:.2f}%\n\n"

        f"{bubble_status}\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 فرمول ارزش ذاتی:\n"
        "وزن طلای خالص × قیمت هر گرم طلای خالص\n\n"

        "📌 فرمول حباب:\n"
        "قیمت بازار − ارزش ذاتی\n\n"

        "📌 درصد حباب:\n"
        "حباب ÷ ارزش ذاتی × ۱۰۰"
    )

    # =====================================================
    # کیبورد نتیجه
    # =====================================================

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

    return RESULT


# =========================================================
# پایان فایل
# =========================================================