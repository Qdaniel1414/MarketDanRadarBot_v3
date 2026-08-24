from telegram.ext import MessageHandler, filters

from handlers.education.menu import (
    education_menu,
    education_router,
)

from handlers.education.macroeconomics.handlers import (
    macroeconomics_handler,
)


def register_education_handlers(app):

    # ======================================
    # باز شدن منوی آموزش
    # ======================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📚 آموزش‌ها$"),
            education_menu,
        )
    )

    # ======================================
    # منوی اصلی آموزش
    # ======================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(💼 آموزش مدیریت سرمایه|"
                r"💰 آموزش سواد مالی|"
                r"📈 آموزش تحلیل تکنیکال|"
                r"🪙 آموزش ارزهای دیجیتال|"
                r"🌍 آموزش اقتصاد کلان|"
                r"🏠 خانه)$"
            ),
            education_router,
        )
    )

    # ======================================
    # موضوعات اقتصاد کلان
    # ======================================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📈 تورم|"
                r"📊 CPI|"
                r"📉 Core CPI|"
                r"🏭 PPI|"
                r"🌍 GDP|"
                r"💰 نرخ بهره|"
                r"🏦 FOMC|"
                r"🎯 Dot Plot|"
                r"💼 NFP|"
                r"🏢 PMI|"
                r"💳 PCE|"
                r"💵 QE|"
                r"📉 QT|"
                r"✂️ Tapering|"
                r"💲 شاخص DXY|"
                r"👥 نرخ بیکاری|"
                r"💸 نقدینگی|"
                r"🏛 پایه پولی|"
                r"💵 عرضه پول|"
                r"📉 رکود|"
                r"🔄 چرخه اقتصادی|"
                r"📈 منحنی بازده|"
                r"🏦 فدرال رزرو|"
                r"🏦 ECB|"
                r"🏦 BOJ|"
                r"💬 انتظارات تورمی|"
                r"🛒 خرده فروشی|"
                r"👥 اعتماد مصرف‌کننده|"
                r"🏭 اعتماد تولیدکننده|"
                r"⚖️ تراز تجاری|"
                r"🌐 حساب جاری|"
                r"📉 کسری بودجه|"
                r"🏛 بدهی دولت|"
                r"💱 نرخ ارز|"
                r"💰 قدرت خرید)$"
            ),
            macroeconomics_handler,
        ),
        group=20,
    )