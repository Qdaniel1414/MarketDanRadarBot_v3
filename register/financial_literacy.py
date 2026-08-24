from telegram.ext import MessageHandler, filters


# =========================
# منوی سواد مالی
# =========================

from handlers.education.financial_literacy.menu import (
    financial_literacy_menu,
    financial_literacy_router,
)


# =========================
# بهره مرکب
# =========================

from handlers.education.financial_literacy.compound_interest.intro import (
    compound_interest_intro,
)

from handlers.education.financial_literacy.compound_interest.example import (
    compound_interest_example,
)

from handlers.education.financial_literacy.compound_interest.calculator import (
    compound_interest_handler,
)
from handlers.education.financial_literacy.active_passive_income.calculator import (
    active_passive_income_input,
)


# =========================
# ROI
# =========================

from handlers.education.financial_literacy.roi import (
    roi_menu,
    roi_router,
)

from handlers.education.financial_literacy.roi.calculator import (
    roi_input,
)



# =========================
# سایر ماشین حساب‌ها
# =========================

from handlers.education.financial_literacy.real_return import (
    real_return_input,
)

from handlers.education.financial_literacy.time_value.calculator import (
    time_value_input,
)

from handlers.education.financial_literacy.purchasing_power.calculator import (
    purchasing_power_input,
)

from handlers.education.financial_literacy.goal_saving.calculator import (
    goal_saving_input,
)


# =========================
# بودجه 50/30/20
# =========================

from handlers.education.financial_literacy.budget_50_30_20.calculator import (
    budget_50_30_20_input,
)
from handlers.education.financial_literacy.budget_50_30_20.calculator import (
    budget_50_30_20_calculator,
    budget_50_30_20_input,
)


def register_financial_literacy(app):


    # =========================
    # منوی اصلی سواد مالی
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^💰 آموزش سواد مالی$"
            ),
            financial_literacy_menu,
        )
    )



    # =========================
    # Router سواد مالی
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(🧮 بهره مرکب|"
                r"⏳ ارزش زمانی پول|"
                r"💵 قدرت خرید|"
                r"🎯 پس‌انداز هدف|"
                r"📈 ROI|"
                r"📊 بازده واقعی|"
                r"🧺 تنوع‌بخشی سرمایه|"
                r"💼 درآمد فعال و غیرفعال|"
                r"📋 بودجه 50/30/20)$"
            ),
            financial_literacy_router,
        )
    )



    # =========================
    # بهره مرکب
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^📘 بهره مرکب چیست\؟$"
            ),
            compound_interest_intro,
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^📈 مثال واقعی بهره مرکب$"
            ),
            compound_interest_example,
        )
    )


    app.add_handler(
        compound_interest_handler
    )



    # =========================
    # ارزش زمانی پول
    # =========================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            time_value_input,
            block=False,
        ),
        group=3,
    )



    # =========================
    # قدرت خرید
    # =========================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            purchasing_power_input,
            block=False,
        ),
        group=4,
    )



    # =========================
    # پس انداز هدف
    # =========================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            goal_saving_input,
            block=False,
        ),
        group=5,
    )



    # =========================
    # ROI
    # =========================

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^📈 ROI$"
            ),
            roi_menu,
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 ROI چیست\؟|🧮 ماشین حساب ROI|📈 مثال واقعی ROI)$"
            ),
            roi_router,
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            roi_input,
            block=False,
        ),
        group=6,
    )



    # =========================
    # بازده واقعی
    # =========================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            real_return_input,
            block=False,
        ),
        group=7,
    )



    # =========================
    # بودجه 50/30/20
    # =========================

    app.add_handler(
    MessageHandler(
        filters.Regex(r"^🧮 ماشین حساب بودجه$"),
        budget_50_30_20_calculator,
    ),
    group=-1,
)

    app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        budget_50_30_20_input,
        block=False,
    ),
    group=11,
)
    # =========================
# درآمد فعال و غیرفعال
# =========================

    app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        active_passive_income_input,
        block=False,
    ),
    group=9,
)