from telegram.ext import MessageHandler, filters


# =========================================================
# Trend
# =========================================================

from handlers.education.technical_analysis.trend import (
    trend_menu,
    trend_router,
    trend_input,
)

from handlers.education.technical_analysis.support_resistance import (
    support_resistance_menu,
    support_resistance_router,
    support_resistance_input,
)


# =========================================================
# Glossary
# =========================================================

from handlers.education.technical_analysis.glossary.menu import (
    glossary_menu,
    glossary_router,
)

from handlers.education.technical_analysis.glossary.dictionary import (
    glossary_dictionary,
)


# =========================================================
# Volume
# =========================================================

from handlers.education.technical_analysis.volume import (
    volume_menu,
    volume_router,
    volume_input,
)


# =========================================================
# Trading Psychology
# =========================================================

from handlers.education.technical_analysis.trading_psychology import (
    trading_psychology_menu,
    trading_psychology_router,
    trading_personality_handler,
)


# =========================================================
# Position Management
# =========================================================

from handlers.education.technical_analysis.position_management import (
    position_management_menu,
    position_management_router,
    position_management_input,
)


# =========================================================
# Capital Management
# =========================================================

from handlers.education.capital_management.position_size import (
    position_size_handler,
)

from handlers.education.capital_management.risk_reward import (
    risk_reward_handler,
)


# =========================================================
# REGISTER TECHNICAL ANALYSIS
# =========================================================

print("######## REGISTER TECHNICAL ANALYSIS ########")


def register_technical_analysis(app):

    print("🔥 REGISTER TECHNICAL ANALYSIS RUNNING")

    # =====================================================
    # 1. TREND
    # =====================================================

    print("🔥 REGISTER TREND")

    # منوی روند
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📊 روند$"),
            trend_menu,
        )
    )

    # گزینه‌های داخل منوی روند
    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 روند چیست؟|"
                r"📈 مثال واقعی روند|"
                r"🧮 ابزار تشخیص روند)$"
            ),
            trend_router,
        )
    )

    # ورودی‌های محاسبات روند
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            trend_input,
            block=False,
        ),
        group=2,
    )

    print("✅ TREND HANDLERS REGISTERED")

    # =====================================================
    # 2. SUPPORT & RESISTANCE
    # =====================================================

    print("🔥 REGISTER SUPPORT & RESISTANCE")

    # منوی حمایت و مقاومت
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🧱 حمایت و مقاومت$"),
            support_resistance_menu,
        )
    )

    # گزینه‌های حمایت و مقاومت
    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 حمایت و مقاومت چیست؟|"
                r"📈 مثال واقعی حمایت و مقاومت|"
                r"🧮 ماشین حساب حمایت و مقاومت)$"
            ),
            support_resistance_router,
        )
    )

    # ورودی‌های حمایت و مقاومت
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            support_resistance_input,
            block=False,
        ),
        group=2,
    )

    print("✅ SUPPORT & RESISTANCE HANDLERS REGISTERED")

    # =====================================================
    # 3. GLOSSARY
    # =====================================================

    print("🔥 REGISTER GLOSSARY")

    # منوی اصطلاحات تحلیل تکنیکال
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📚 اصطلاحات تحلیل تکنیکال$"),
            glossary_menu,
        )
    )

    # واژه‌نامه کامل
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📖 واژه‌نامه کامل$"),
            glossary_dictionary,
        )
    )

    # سایر اصطلاحات تحلیل تکنیکال
    # 🎯 ریسک به ریوارد عمداً اینجا نیست.
    # Handler مستقل خودش را دارد.
    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(🕯 کندل \(Candlestick\)|"
                r"⏰ تایم فریم|"
                r"📈 روند|"
                r"📊 نوسان|"
                r"💧 نقدشوندگی|"
                r"↩ پولبک|"
                r"🚀 بریک اوت|"
                r"❌ فیک بریک اوت|"
                r"⚡ مومنتوم|"
                r"💰 لیکوییدیتی گراب|"
                r"⬅️ بازگشت)$"
            ),
            glossary_router,
        )
    )

    print("✅ GLOSSARY HANDLERS REGISTERED")

    # =====================================================
    # 4. VOLUME
    # =====================================================

    print("🔥 REGISTER VOLUME")

    # منوی حجم معاملات
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📦 حجم معاملات$"),
            volume_menu,
        )
    )

    # گزینه‌های حجم معاملات
    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 حجم معاملات چیست؟|"
                r"🧮 ماشین حساب حجم معاملات|"
                r"📈 مثال واقعی حجم معاملات)$"
            ),
            volume_router,
        )
    )

    # ورودی حجم معاملات
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            volume_input,
            block=False,
        ),
        group=2,
    )

    print("✅ VOLUME HANDLERS REGISTERED")

    # =====================================================
    # 5. TRADING PSYCHOLOGY
    # =====================================================

    print("🔥 REGISTER TRADING PSYCHOLOGY")

    # منوی اصلی روانشناسی معامله
    #
    # فعلاً در group=-1 ثبت شده تا Handlerهای عمومی
    # گروه‌های پایین‌تر نتوانند این دکمه را بگیرند.
    # بعد از تأیید عملکرد، می‌توان این اولویت را
    # به ساختار نهایی تمیزتری منتقل کرد.
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🧠 روانشناسی معامله$"),
            trading_psychology_menu,
        ),
        group=-1,
    )

    print("✅ TRADING PSYCHOLOGY MENU REGISTERED")

    # گزینه‌های داخل منوی روانشناسی
    #
    # تست شخصیت معامله‌گر اینجا ثبت نمی‌شود؛
    # ConversationHandler خودش Entry Point دارد.
    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 روانشناسی معامله چیست؟|"
                r"📈 مثال واقعی روانشناسی|"
                r"💡 اشتباهات رایج|"
                r"⬅️ بازگشت)$"
            ),
            trading_psychology_router,
        )
    )

    app.add_handler(
    trading_personality_handler,
    group=-1,
)

    print("✅ TRADING PERSONALITY CONVERSATION REGISTERED")
    print("✅ TRADING PSYCHOLOGY HANDLERS REGISTERED")

    # =====================================================
    # 6. POSITION MANAGEMENT
    # =====================================================

    print("🔥 REGISTER POSITION MANAGEMENT")

    # منوی مدیریت پوزیشن
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^⚖️ مدیریت پوزیشن$"),
            position_management_menu,
        )
    )

    # گزینه‌های مدیریت پوزیشن
    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 مدیریت پوزیشن چیست؟|"
                r"🧮 ماشین حساب مدیریت پوزیشن|"
                r"📈 مثال واقعی مدیریت پوزیشن|"
                r"💡 اشتباهات رایج مدیریت پوزیشن|"
                r"⬅️ بازگشت)$"
            ),
            position_management_router,
        )
    )

    # ورودی ماشین حساب مدیریت پوزیشن
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            position_management_input,
            block=False,
        ),
        group=10,
    )

    print("✅ POSITION MANAGEMENT INPUT HANDLER REGISTERED")

    # =====================================================
    # 7. CAPITAL MANAGEMENT
    # =====================================================

    print("🔥 REGISTER CAPITAL MANAGEMENT")

    # Position Size
    app.add_handler(
        position_size_handler
    )

    print("✅ POSITION SIZE HANDLER REGISTERED")

    # Risk / Reward
    app.add_handler(
        risk_reward_handler
    )

    print("✅ RISK REWARD HANDLER REGISTERED")

    # =====================================================
    # DONE
    # =====================================================

    print(
        "🔥🔥🔥 TECHNICAL ANALYSIS HANDLERS "
        "REGISTERED SUCCESSFULLY 🔥🔥🔥"
    )
