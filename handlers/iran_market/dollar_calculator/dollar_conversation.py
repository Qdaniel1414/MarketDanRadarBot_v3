from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.iran_market.dollar_calculator.dollar_states import (
    METHOD,
    DIRHAM,
    EURO,
    EURO_USD,
    POUND,
    GBP_USD,
    GOLD_18,
    GOLD_OUNCE,
    COIN_PRICE,
    COIN_OUNCE,
    RESULT,
)


# =========================================================
# ساخت منوی روش‌های محاسبه
# =========================================================

def dollar_method_keyboard():

    return ReplyKeyboardMarkup(
        [
            ["🇦🇪 دلار از درهم"],
            ["🥈 دلار از یورو", "🥉 دلار از پوند"],
            ["🔥 دلار ضمنی طلا"],
            ["🔥 دلار ضمنی سکه"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )


# =========================================================
# شروع محاسبه ارزش‌گذاری دلار
# =========================================================

async def dollar_calculator_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    # پاک کردن اطلاعات قبلی
    context.user_data.pop("dollar_method", None)
    context.user_data.pop("dirham", None)
    context.user_data.pop("euro", None)
    context.user_data.pop("eur_usd", None)
    context.user_data.pop("dollar_result", None)

    keyboard = dollar_method_keyboard()

    await update.message.reply_text(
        "💵 محاسبه ارزش‌گذاری دلار\n\n"
        "لطفاً روش محاسبه را انتخاب کنید:",
        reply_markup=keyboard,
    )

    return METHOD

async def get_coin_price(update, context):
    text = update.message.text.strip()

    try:
        coin_price = float(text.replace(",", "").replace("٬", ""))

        if coin_price <= 0:
            raise ValueError

    except ValueError:
        await update.message.reply_text(
            "❌ لطفاً قیمت سکه را به صورت عددی وارد کنید.\n\n"
            "مثال:\n"
            "186500000"
        )
        return COIN_PRICE

    context.user_data["coin_price"] = coin_price

    await update.message.reply_text(
        "🔥 محاسبه دلار ضمنی سکه\n\n"
        "مرحله ۲ از ۲\n\n"
        "🌍 لطفاً قیمت روز اونس جهانی طلا را به دلار وارد کنید:\n\n"
        "مثال:\n"
        "3400"
    )

    return COIN_OUNCE

async def get_coin_ounce(update, context):
    text = update.message.text.strip()

    try:
        gold_ounce = float(text.replace(",", "").replace("٬", ""))

        if gold_ounce <= 0:
            raise ValueError

    except ValueError:
        await update.message.reply_text(
            "❌ لطفاً قیمت اونس جهانی را به صورت عددی وارد کنید.\n\n"
            "مثال:\n"
            "3400"
        )
        return COIN_OUNCE

    coin_price = context.user_data.get("coin_price")

    if coin_price is None:
        await update.message.reply_text(
            "❌ اطلاعات قیمت سکه پیدا نشد.\n"
            "لطفاً محاسبه را از ابتدا شروع کنید."
        )
        return ConversationHandler.END

    # وزن سکه امامی: 8.133 گرم
    # عیار سکه: 900 از 1000
    # طلای خالص موجود در سکه:
    pure_gold_weight = 8.133 * 0.900

    # هر اونس تروا = 31.1034768 گرم
    dollar_value = (
        coin_price * 31.1034768
        / (gold_ounce * pure_gold_weight)
    )

    context.user_data["dollar_result"] = dollar_value

    await update.message.reply_text(
        "🔥 نتیجه ارزش‌گذاری دلار ضمنی سکه\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🥇 قیمت سکه امامی:\n"
        f"{coin_price:,.0f} تومان\n\n"
        f"🌍 قیمت اونس جهانی طلا:\n"
        f"${gold_ounce:,.2f}\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"💵 دلار ضمنی سکه:\n"
        f"{dollar_value:,.0f} تومان\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "📌 این عدد قیمت تئوریک دلار بر اساس "
        "قیمت سکه و اونس جهانی طلاست و حباب سکه، "
        "هزینه‌های بازار و سایر عوامل را در نظر نمی‌گیرد."
    )

    return RESULT

# =========================================================
# انتخاب روش محاسبه
# =========================================================

async def select_method(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    text = update.message.text.strip()

    # -----------------------------------------------------
    # خروج
    # -----------------------------------------------------

    if text == "🚪 خروج از محاسبه":

        context.user_data.clear()

        await update.message.reply_text(
            "🚪 از محاسبه ارزش‌گذاری دلار خارج شدید."
        )

        return ConversationHandler.END

    # -----------------------------------------------------
    # دلار از درهم
    # -----------------------------------------------------

    if text == "🇦🇪 دلار از درهم":

        context.user_data["dollar_method"] = "DIRHAM"

        await update.message.reply_text(
            "🇦🇪 محاسبه دلار از درهم\n\n"
            "لطفاً قیمت روز درهم را به تومان وارد کنید:\n\n"
            "مثال:\n"
            "52000"
        )

        return DIRHAM

    # -----------------------------------------------------
    # دلار از یورو
    # -----------------------------------------------------

    if text == "🥈 دلار از یورو":

        context.user_data["dollar_method"] = "EURO"

        await update.message.reply_text(
            "🥈 محاسبه دلار از یورو\n\n"
            "مرحله ۱ از ۲\n\n"
            "💶 لطفاً قیمت روز یورو را به تومان وارد کنید:\n\n"
            "مثال:\n"
            "220000"
        )

        return EURO

    # -----------------------------------------------------
    # دلار از پوند
    # -----------------------------------------------------

    if text == "🥉 دلار از پوند":

        context.user_data["dollar_method"] = "POUND"

        await update.message.reply_text(
            "🥉 محاسبه دلار از پوند\n\n"
            "مرحله ۱ از ۲\n\n"
            "💷 لطفاً قیمت روز پوند را به تومان وارد کنید:\n\n"
            "مثال:\n"
            "255000"
        )

        return POUND

    # -----------------------------------------------------
    # دلار ضمنی طلا
    # -----------------------------------------------------
    if text == "🔥 دلار ضمنی طلا":
    

        context.user_data["dollar_method"] = "GOLD"

        await update.message.reply_text(
            "🔥 محاسبه دلار ضمنی طلا\n\n"
            "مرحله ۱ از ۲\n\n"
            "🪙 لطفاً قیمت هر گرم طلای ۱۸ عیار "
            "را به تومان وارد کنید:\n\n"
            "مثال:\n"
            "20000000"
        )

        return GOLD_18

    # -----------------------------------------------------
# دلار ضمنی سکه
# -----------------------------------------------------

    if text == "🔥 دلار ضمنی سکه":

     context.user_data["dollar_method"] = "COIN"

    await update.message.reply_text(
        "🔥 محاسبه دلار ضمنی سکه\n\n"
        "مرحله ۱ از ۲\n\n"
        "🪙 لطفاً قیمت روز سکه امامی را به تومان وارد کنید:\n\n"
        "مثال:\n"
        "200000000"
    )

    return COIN_PRICE

    # -----------------------------------------------------
    # گزینه نامعتبر
    # -----------------------------------------------------

    await update.message.reply_text(
        "❌ لطفاً یکی از گزینه‌های منو را انتخاب کنید."
    )

    return METHOD


# =========================================================
# دریافت قیمت درهم
# =========================================================

async def get_dirham(
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

        dirham = float(text)

        if dirham <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت درهم نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n\n"
            "مثال:\n"
            "52000"
        )

        return DIRHAM

    # ذخیره
    context.user_data["dirham"] = dirham

    # -----------------------------------------------------
    # نرخ ثابت دلار به درهم
    # -----------------------------------------------------

    dollar_value = dirham * 3.67

    context.user_data["dollar_result"] = dollar_value

    # -----------------------------------------------------
    # منوی نتیجه
    # -----------------------------------------------------

    result_keyboard = ReplyKeyboardMarkup(
        [
            ["🔄 محاسبه مجدد"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )

    result = (
        "💵 نتیجه ارزش‌گذاری دلار\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🇦🇪 روش محاسبه:\n"
        "دلار از درهم\n\n"

        f"🇦🇪 قیمت درهم:\n"
        f"{dirham:,.0f} تومان\n\n"

        "📐 نرخ برابری دلار به درهم:\n"
        "3.67\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "💵 قیمت ضمنی دلار:\n"
        f"{dollar_value:,.0f} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 فرمول:\n"
        "قیمت دلار = قیمت درهم × 3.67"
    )

    await update.message.reply_text(
        result,
        reply_markup=result_keyboard,
    )

    return RESULT


# =========================================================
# دریافت قیمت یورو
# =========================================================

async def get_euro(
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

        euro = float(text)

        if euro <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت یورو نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n\n"
            "مثال:\n"
            "220000"
        )

        return EURO

    # ذخیره قیمت یورو
    context.user_data["euro"] = euro

    await update.message.reply_text(
        "🌍 مرحله ۲ از ۲\n\n"
        "لطفاً نرخ روز EUR/USD را وارد کنید:\n\n"
        "مثال:\n"
        "1.17\n\n"
        "📌 این نرخ نشان می‌دهد هر ۱ یورو چند دلار آمریکا ارزش دارد."
    )

    return EURO_USD


# =========================================================
# دریافت نرخ EUR/USD و محاسبه دلار
# =========================================================

async def get_eur_usd(
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

        eur_usd = float(text)

        if eur_usd <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ نرخ EUR/USD نامعتبر است.\n\n"
            "لطفاً نرخ را به صورت عددی وارد کنید.\n\n"
            "مثال:\n"
            "1.17"
        )

        return EURO_USD

    euro = context.user_data.get("euro")

    if euro is None:

        await update.message.reply_text(
            "❌ اطلاعات قیمت یورو پیدا نشد.\n"
            "لطفاً محاسبه را دوباره شروع کنید."
        )

        return ConversationHandler.END

    # =====================================================
    # فرمول دلار از یورو
    #
    # قیمت دلار = قیمت یورو ÷ EUR/USD
    # =====================================================

    dollar_value = euro / eur_usd

    context.user_data["eur_usd"] = eur_usd
    context.user_data["dollar_result"] = dollar_value

    # =====================================================
    # منوی نتیجه
    # =====================================================

    result_keyboard = ReplyKeyboardMarkup(
        [
            ["🔄 محاسبه مجدد"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )

    result = (
        "💵 نتیجه ارزش‌گذاری دلار\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🥈 روش محاسبه:\n"
        "دلار از یورو\n\n"

        f"💶 قیمت یورو:\n"
        f"{euro:,.0f} تومان\n\n"

        "🌍 نرخ EUR/USD:\n"
        f"{eur_usd:.4f}\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "💵 قیمت ضمنی دلار:\n"
        f"{dollar_value:,.0f} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 فرمول:\n"
        "قیمت دلار = قیمت یورو ÷ EUR/USD\n\n"

        "💡 یعنی اگر هر ۱ یورو برابر با "
        f"{eur_usd:.4f} دلار باشد،\n"
        "قیمت دلار از تقسیم قیمت یورو بر نرخ EUR/USD "
        "به دست می‌آید."
    )

    await update.message.reply_text(
        result,
        reply_markup=result_keyboard,
    )

    return RESULT

# =========================================================
# دریافت قیمت پوند
# =========================================================

async def get_pound(
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

        pound = float(text)

        if pound <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت پوند نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n\n"
            "مثال:\n"
            "255000"
        )

        return POUND

    # ذخیره قیمت پوند
    context.user_data["pound"] = pound

    await update.message.reply_text(
        "🌍 مرحله ۲ از ۲\n\n"
        "لطفاً نرخ روز GBP/USD را وارد کنید:\n\n"
        "مثال:\n"
        "1.34\n\n"
        "📌 این نرخ نشان می‌دهد هر ۱ پوند چند دلار آمریکا ارزش دارد."
    )

    return GBP_USD

# =========================================================
# دریافت نرخ GBP/USD و محاسبه دلار
# =========================================================

async def get_gbp_usd(
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

        gbp_usd = float(text)

        if gbp_usd <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ نرخ GBP/USD نامعتبر است.\n\n"
            "لطفاً نرخ را به صورت عددی وارد کنید.\n\n"
            "مثال:\n"
            "1.34"
        )

        return GBP_USD

    pound = context.user_data.get("pound")

    if pound is None:

        await update.message.reply_text(
            "❌ اطلاعات قیمت پوند پیدا نشد.\n"
            "لطفاً محاسبه را دوباره شروع کنید."
        )

        return ConversationHandler.END

    # =====================================================
    # فرمول دلار از پوند
    #
    # قیمت دلار = قیمت پوند ÷ GBP/USD
    # =====================================================

    dollar_value = pound / gbp_usd

    context.user_data["gbp_usd"] = gbp_usd
    context.user_data["dollar_result"] = dollar_value

    # =====================================================
    # منوی نتیجه
    # =====================================================

    result_keyboard = ReplyKeyboardMarkup(
        [
            ["🔄 محاسبه مجدد"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )

    result = (
        "💵 نتیجه ارزش‌گذاری دلار\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🥉 روش محاسبه:\n"
        "دلار از پوند\n\n"

        f"💷 قیمت پوند:\n"
        f"{pound:,.0f} تومان\n\n"

        "🌍 نرخ GBP/USD:\n"
        f"{gbp_usd:.4f}\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "💵 قیمت ضمنی دلار:\n"
        f"{dollar_value:,.0f} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 فرمول:\n"
        "قیمت دلار = قیمت پوند ÷ GBP/USD\n\n"

        "💡 یعنی اگر هر ۱ پوند برابر با "
        f"{gbp_usd:.4f} دلار باشد،\n"
        "قیمت دلار از تقسیم قیمت پوند بر نرخ GBP/USD "
        "به دست می‌آید."
    )

    await update.message.reply_text(
        result,
        reply_markup=result_keyboard,
    )

    return RESULT
# =========================================================
# محاسبه مجدد
# =========================================================

async def recalculate(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    text = update.message.text.strip()

    # -----------------------------------------------------
    # محاسبه مجدد
    # -----------------------------------------------------

    if text == "🔄 محاسبه مجدد":

        context.user_data.pop("dollar_method", None)
        context.user_data.pop("dirham", None)
        context.user_data.pop("euro", None)
        context.user_data.pop("eur_usd", None)
        context.user_data.pop("dollar_result", None)

        await update.message.reply_text(
            "💵 محاسبه ارزش‌گذاری دلار\n\n"
            "لطفاً روش محاسبه را انتخاب کنید:",
            reply_markup=dollar_method_keyboard(),
        )

        return METHOD

    # -----------------------------------------------------
    # خروج
    # -----------------------------------------------------

    if text == "🚪 خروج از محاسبه":

        context.user_data.pop("dollar_method", None)
        context.user_data.pop("dirham", None)
        context.user_data.pop("euro", None)
        context.user_data.pop("eur_usd", None)
        context.user_data.pop("dollar_result", None)

        await update.message.reply_text(
            "🚪 از محاسبه ارزش‌گذاری دلار خارج شدید."
        )

        return ConversationHandler.END

    await update.message.reply_text(
        "❌ لطفاً یکی از گزینه‌های زیر را انتخاب کنید."
    )

    return RESULT

# =========================================================
# دریافت قیمت طلای ۱۸ عیار
# =========================================================

async def get_gold_18(
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

        gold_18 = float(text)

        if gold_18 <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت طلای ۱۸ عیار نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n\n"
            "مثال:\n"
            "20000000"
        )

        return GOLD_18

    # ذخیره قیمت طلای ۱۸ عیار
    context.user_data["gold_18"] = gold_18

    # -----------------------------------------------------
    # مرحله دوم: دریافت قیمت اونس جهانی طلا
    # -----------------------------------------------------

    await update.message.reply_text(
        "🌍 مرحله ۲ از ۲\n\n"
        "لطفاً قیمت روز هر اونس طلای جهانی را به دلار وارد کنید:\n\n"
        "مثال:\n"
        "4000\n\n"
        "📌 مثال بالا یعنی قیمت هر اونس طلا "
        "۴۰۰۰ دلار است."
    )

    return GOLD_OUNCE

# =========================================================
# دریافت قیمت اونس جهانی و محاسبه دلار ضمنی طلا
# =========================================================

async def get_gold_ounce(
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

        gold_ounce = float(text)

        if gold_ounce <= 0:
            raise ValueError

    except (ValueError, TypeError):

        await update.message.reply_text(
            "❌ قیمت اونس جهانی نامعتبر است.\n\n"
            "لطفاً فقط عدد وارد کنید.\n\n"
            "مثال:\n"
            "4000"
        )

        return GOLD_OUNCE

    # -----------------------------------------------------
    # دریافت قیمت طلای ۱۸ عیار
    # -----------------------------------------------------

    gold_18 = context.user_data.get("gold_18")

    if gold_18 is None:

        await update.message.reply_text(
            "❌ اطلاعات قیمت طلای ۱۸ عیار پیدا نشد.\n\n"
            "لطفاً محاسبه را دوباره شروع کنید."
        )

        return ConversationHandler.END

    # -----------------------------------------------------
    # ثابت‌ها
    # -----------------------------------------------------

    OUNCE_GRAMS = 31.1035
    GOLD_18_FACTOR = 0.75

    # -----------------------------------------------------
    # فرمول دلار ضمنی طلا
    #
    # قیمت طلای ۱۸ =
    # (اونس × دلار ÷ 31.1035) × 0.75
    #
    # بنابراین:
    #
    # دلار =
    # (قیمت طلای ۱۸ × 31.1035)
    # ÷ (اونس × 0.75)
    # -----------------------------------------------------

    dollar_value = (
        gold_18 * OUNCE_GRAMS
    ) / (
        gold_ounce * GOLD_18_FACTOR
    )

    # ذخیره اطلاعات
    context.user_data["gold_ounce"] = gold_ounce
    context.user_data["dollar_result"] = dollar_value

    # -----------------------------------------------------
    # منوی نتیجه
    # -----------------------------------------------------

    result_keyboard = ReplyKeyboardMarkup(
        [
            ["🔄 محاسبه مجدد"],
            ["🚪 خروج از محاسبه"],
        ],
        resize_keyboard=True,
    )

    result = (
        "💵 نتیجه ارزش‌گذاری دلار\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🔥 روش محاسبه:\n"
        "دلار ضمنی طلا\n\n"

        f"🪙 قیمت طلای ۱۸ عیار:\n"
        f"{gold_18:,.0f} تومان\n\n"

        "🌍 قیمت اونس جهانی:\n"
        f"{gold_ounce:,.2f} دلار\n\n"

        "📏 وزن هر اونس:\n"
        "31.1035 گرم\n\n"

        "🥇 عیار طلای ۱۸:\n"
        "75٪ طلای خالص\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "💵 قیمت ضمنی دلار:\n"
        f"{dollar_value:,.0f} تومان\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "📌 فرمول:\n"
        "دلار ضمنی = "
        "(قیمت طلای ۱۸ × 31.1035) "
        "÷ (اونس × 0.75)"
    )

    await update.message.reply_text(
        result,
        reply_markup=result_keyboard,
    )

    return RESULT
# =========================================================
# Conversation Handler
# =========================================================

dollar_conversation = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(
                r"^💵 فرمول محاسبه دلار$"
            ),
            dollar_calculator_start,
        )
    ],

    states={

        # -------------------------------------------------
        # انتخاب روش
        # -------------------------------------------------

        METHOD: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                select_method,
            )
        ],

        # -------------------------------------------------
        # دلار از درهم
        # -------------------------------------------------

        DIRHAM: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_dirham,
            )
        ],

        # -------------------------------------------------
        # دلار از یورو
        # -------------------------------------------------

        EURO: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_euro,
            )
        ],

        # -------------------------------------------------
        # نرخ EUR/USD
        # -------------------------------------------------

        EURO_USD: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_eur_usd,
            )
        ],

        # -------------------------------------------------
        # دلار از پوند
        # -------------------------------------------------

        POUND: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_pound,
            )
        ],

        # -------------------------------------------------
# نرخ GBP/USD
# -------------------------------------------------

GBP_USD: [
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_gbp_usd,
    )
],

# -------------------------------------------------
# دلار ضمنی طلا
# -------------------------------------------------

GOLD_18: [
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_gold_18,
    )
],

GOLD_OUNCE: [
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_gold_ounce,
    )
],

# -------------------------------------------------
# دلار ضمنی سکه
# -------------------------------------------------

COIN_PRICE: [
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_coin_price,
    )
],

COIN_OUNCE: [
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_coin_ounce,
    )
],
        # -------------------------------------------------
        # نتیجه
        # -------------------------------------------------

        RESULT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                recalculate,
            )
        ],
    },

    # -----------------------------------------------------
    # Fallback
    # -----------------------------------------------------

    fallbacks=[
        MessageHandler(
            filters.Regex(
                r"^🚪 خروج از محاسبه$"
            ),
            recalculate,
        )
    ],

    allow_reentry=True,
)