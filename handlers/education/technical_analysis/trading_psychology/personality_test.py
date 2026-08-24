from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)


# =========================================================
# مراحل تست شخصیت معامله‌گر
# =========================================================

PERSONALITY_Q1 = 1
PERSONALITY_Q2 = 2
PERSONALITY_Q3 = 3
PERSONALITY_Q4 = 4
PERSONALITY_Q5 = 5


# =========================================================
# شروع تست شخصیت معامله‌گر
# =========================================================

async def trading_personality_test(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    # شروع تست برای کاربر
    context.user_data["personality_step"] = PERSONALITY_Q1
    context.user_data["personality_score"] = 0

    print("🔥 PERSONALITY TEST STARTED")

    if update.effective_user:
        print(
            "👤 USER:",
            update.effective_user.id,
        )

    await update.message.reply_text(
        "🧠 تست شخصیت معامله‌گر\n\n"
        "سؤال 1 از 5\n\n"
        "اگر سه معامله پشت سر هم ضرر کنید چه کار می‌کنید؟\n\n"
        "1️⃣ استراحت می‌کنم\n"
        "2️⃣ حجم معامله را بیشتر می‌کنم\n"
        "3️⃣ سریع دوباره وارد معامله می‌شوم\n\n"
        "فقط عدد 1 یا 2 یا 3 را ارسال کنید."
    )

    return PERSONALITY_Q1


# =========================================================
# پردازش پاسخ‌های تست
# =========================================================

async def trading_personality_input(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return ConversationHandler.END

    if update.message.text is None:
        return ConversationHandler.END

    answer = update.message.text.strip()

    print(
        "🔥 PERSONALITY INPUT:",
        repr(answer),
    )

    # =====================================================
    # بررسی پاسخ
    # =====================================================

    if answer not in ("1", "2", "3"):

        await update.message.reply_text(
            "❌ پاسخ نامعتبر است.\n\n"
            "فقط عدد 1 یا 2 یا 3 را ارسال کنید."
        )

        return context.user_data.get(
            "personality_step",
            PERSONALITY_Q1,
        )

    # =====================================================
    # دریافت وضعیت تست
    # =====================================================

    step = context.user_data.get(
        "personality_step",
        PERSONALITY_Q1,
    )

    score = context.user_data.get(
        "personality_score",
        0,
    )

    # =====================================================
    # امتیازدهی
    # =====================================================

    if answer == "1":
        score += 2

    elif answer == "2":
        score -= 2

    elif answer == "3":
        score -= 1

    context.user_data["personality_score"] = score

    print("📌 STEP:", step)
    print("📊 SCORE:", score)

    # =====================================================
    # سؤال 2
    # =====================================================

    if step == PERSONALITY_Q1:

        context.user_data["personality_step"] = PERSONALITY_Q2

        await update.message.reply_text(
            "🧠 تست شخصیت معامله‌گر\n\n"
            "سؤال 2 از 5\n\n"
            "وقتی معامله شما وارد سود می‌شود:\n\n"
            "1️⃣ طبق برنامه خارج می‌شوم\n"
            "2️⃣ طمع می‌کنم و نگه می‌دارم\n"
            "3️⃣ خیلی زود می‌بندم\n\n"
            "فقط عدد 1 یا 2 یا 3 را ارسال کنید."
        )

        return PERSONALITY_Q2

    # =====================================================
    # سؤال 3
    # =====================================================

    if step == PERSONALITY_Q2:

        context.user_data["personality_step"] = PERSONALITY_Q3

        await update.message.reply_text(
            "🧠 تست شخصیت معامله‌گر\n\n"
            "سؤال 3 از 5\n\n"
            "قبل از ورود به معامله:\n\n"
            "1️⃣ همیشه حد ضرر دارم\n"
            "2️⃣ بعضی وقت‌ها\n"
            "3️⃣ اصلاً حد ضرر نمی‌گذارم\n\n"
            "فقط عدد 1 یا 2 یا 3 را ارسال کنید."
        )

        return PERSONALITY_Q3

    # =====================================================
    # سؤال 4
    # =====================================================

    if step == PERSONALITY_Q3:

        context.user_data["personality_step"] = PERSONALITY_Q4

        await update.message.reply_text(
            "🧠 تست شخصیت معامله‌گر\n\n"
            "سؤال 4 از 5\n\n"
            "بعد از یک سود بزرگ:\n\n"
            "1️⃣ همان حجم قبلی را حفظ می‌کنم\n"
            "2️⃣ حجم را زیاد می‌کنم\n"
            "3️⃣ هرچه شد می‌شود!\n\n"
            "فقط عدد 1 یا 2 یا 3 را ارسال کنید."
        )

        return PERSONALITY_Q4

    # =====================================================
    # سؤال 5
    # =====================================================

    if step == PERSONALITY_Q4:

        context.user_data["personality_step"] = PERSONALITY_Q5

        await update.message.reply_text(
            "🧠 تست شخصیت معامله‌گر\n\n"
            "سؤال 5 از 5\n\n"
            "اگر بازار برخلاف تحلیل شما حرکت کند:\n\n"
            "1️⃣ حد ضرر را قبول می‌کنم\n"
            "2️⃣ حد ضرر را جابه‌جا می‌کنم\n"
            "3️⃣ میانگین کم می‌کنم\n\n"
            "فقط عدد 1 یا 2 یا 3 را ارسال کنید."
        )

        return PERSONALITY_Q5

    # =====================================================
    # پایان تست
    # =====================================================

    if step == PERSONALITY_Q5:

        score = context.user_data.get(
            "personality_score",
            0,
        )

        # -------------------------------------------------
        # تعیین شخصیت
        # -------------------------------------------------

        if score >= 8:

            result = (
                "🟢 شخصیت شما:\n"
                "معامله‌گر منظم و منطقی"
            )

            explanation = (
                "شما معمولاً قبل از معامله برنامه دارید "
                "و کنترل احساسات بهتری در تصمیم‌گیری دارید."
            )

        elif score >= 3:

            result = (
                "🟡 شخصیت شما:\n"
                "نسبتاً احساسی"
            )

            explanation = (
                "گاهی اوقات احساسات می‌توانند روی "
                "تصمیم‌های معاملاتی شما تأثیر بگذارند."
            )

        else:

            result = (
                "🔴 شخصیت شما:\n"
                "بسیار احساسی و پرریسک"
            )

            explanation = (
                "احتمال تصمیم‌های عجولانه، احساسی و "
                "پرریسک در معاملات شما بیشتر است."
            )

        # -------------------------------------------------
        # ارسال نتیجه
        # -------------------------------------------------

        await update.message.reply_text(
            "🧠 نتیجه تست شخصیت معامله‌گر\n\n"
            f"{result}\n\n"
            f"📊 امتیاز شما: {score}\n\n"
            f"{explanation}\n\n"
            "📌 پیشنهاد:\n"
            "همیشه قبل از معامله حد ضرر، حد سود و "
            "حجم معامله را مشخص کنید.\n\n"
            "🎯 کنترل احساسات بخش مهمی از مدیریت سرمایه است."
        )

        # -------------------------------------------------
        # پاک کردن اطلاعات تست
        # -------------------------------------------------

        context.user_data.pop(
            "personality_step",
            None,
        )

        context.user_data.pop(
            "personality_score",
            None,
        )

        return ConversationHandler.END

    return ConversationHandler.END


# =========================================================
# لغو تست
# =========================================================

async def trading_personality_cancel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is not None:

        await update.message.reply_text(
            "❌ تست شخصیت لغو شد."
        )

    context.user_data.pop(
        "personality_step",
        None,
    )

    context.user_data.pop(
        "personality_score",
        None,
    )

    return ConversationHandler.END


# =========================================================
# Conversation Handler
# =========================================================

trading_personality_handler = ConversationHandler(

    entry_points=[
        MessageHandler(
            filters.Regex(
                r"^🧮 تست شخصیت معامله‌گر$"
            ),
            trading_personality_test,
        )
    ],

    states={

        # -------------------------------------------------
        # سؤال 1
        # -------------------------------------------------

        PERSONALITY_Q1: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                trading_personality_input,
            )
        ],

        # -------------------------------------------------
        # سؤال 2
        # -------------------------------------------------

        PERSONALITY_Q2: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                trading_personality_input,
            )
        ],

        # -------------------------------------------------
        # سؤال 3
        # -------------------------------------------------

        PERSONALITY_Q3: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                trading_personality_input,
            )
        ],

        # -------------------------------------------------
        # سؤال 4
        # -------------------------------------------------

        PERSONALITY_Q4: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                trading_personality_input,
            )
        ],

        # -------------------------------------------------
        # سؤال 5
        # -------------------------------------------------

        PERSONALITY_Q5: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                trading_personality_input,
            )
        ],
    },

    fallbacks=[
        MessageHandler(
            filters.Regex(r"^❌ لغو تست$"),
            trading_personality_cancel,
        )
    ],

    allow_reentry=True,
)