
from telegram.ext import MessageHandler, filters


# -----------------------------
# Capital Management
# -----------------------------

from handlers.education.capital_management.intro import (
    capital_intro,
)

from handlers.education.capital_management.menu import (
    capital_management_menu,
)

from handlers.education.capital_management.mistakes import (
    mistakes_handler,
)

from handlers.education.capital_management.one_percent import (
    one_percent_router,
)

from handlers.education.capital_management.position_size import (
    position_size_handler,
)

from handlers.education.capital_management.risk_reward import (
    risk_reward_handler,
)


# -----------------------------
# Financial Literacy
# -----------------------------

from handlers.education.financial_literacy.time_value import (
    time_value_menu,
    time_value_router,
    time_value_input,
)

from handlers.education.financial_literacy.purchasing_power import (
    purchasing_power_menu,
    purchasing_power_router,
    purchasing_power_input,
)

from handlers.education.financial_literacy.goal_saving import (
    goal_saving_menu,
    goal_saving_router,
    goal_saving_input,
)

from handlers.education.financial_literacy.real_return import (
    real_return_menu,
    real_return_router,
    real_return_input,
)

from handlers.education.financial_literacy.diversification import (
    diversification_menu,
    diversification_router,
)

from handlers.education.financial_literacy.active_passive_income import (
    active_passive_income_menu,
    active_passive_income_router,
    active_passive_income_input,
)

from handlers.education.financial_literacy.budget_50_30_20 import (
    budget_50_30_20_menu,
    budget_50_30_20_router,
    budget_50_30_20_input,
)


# -----------------------------
# Register
# -----------------------------

def register_finance_education(app):

    # ============================================================
    # مدیریت سرمایه
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💰 مدیریت سرمایه چیست\؟?$"),
            capital_intro,
        )
    )

    # قانون ۱ درصد
    app.add_handler(
        one_percent_router
    )

    # حجم معامله
    app.add_handler(
        position_size_handler
    )

    # ریسک به ریوارد
    app.add_handler(
        risk_reward_handler
    )

    # اشتباهات رایج
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^❌ اشتباهات رایج معامله‌گران$"),
            mistakes_handler,
        )
    )

    # منوی مدیریت سرمایه
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💼 آموزش مدیریت سرمایه$"),
            capital_management_menu,
        )
    )


    # ============================================================
    # ارزش زمانی پول
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^⏳ ارزش زمانی پول$"),
            time_value_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 ارزش زمانی پول چیست؟|📈 مثال واقعی ارزش زمانی پول|🧮 ماشین حساب ارزش زمانی پول)$"
            ),
            time_value_router,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            time_value_input,
            block=False,
        ),
        group=2,
    )


    # ============================================================
    # قدرت خرید
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💵 قدرت خرید$"),
            purchasing_power_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 قدرت خرید چیست؟|📈 مثال واقعی قدرت خرید|🧮 ماشین حساب قدرت خرید)$"
            ),
            purchasing_power_router,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            purchasing_power_input,
            block=False,
        ),
        group=2,
    )


    # ============================================================
    # پس‌انداز هدف
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🎯 پس‌انداز هدف$"),
            goal_saving_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 پس‌انداز هدف چیست؟|📈 مثال واقعی پس‌انداز هدف|🧮 ماشین حساب پس‌انداز هدف)$"
            ),
            goal_saving_router,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            goal_saving_input,
            block=False,
        ),
        group=2,
    )


    # ============================================================
    # بازده واقعی
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📊 بازده واقعی$"),
            real_return_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 بازده واقعی چیست؟|📈 مثال واقعی بازده واقعی|🧮 ماشین حساب بازده واقعی)$"
            ),
            real_return_router,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            real_return_input,
            block=False,
        ),
        group=2,
    )


    # ============================================================
    # تنوع‌بخشی سرمایه
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🧺 تنوع‌بخشی سرمایه$"),
            diversification_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 تنوع‌بخشی سرمایه چیست؟|📈 مثال واقعی تنوع‌بخشی|🧮 ماشین حساب تنوع‌بخشی)$"
            ),
            diversification_router,
        )
    )


    # ============================================================
    # درآمد فعال و غیرفعال
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^💼 درآمد فعال و غیرفعال$"),
            active_passive_income_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 درآمد فعال و غیرفعال چیست؟|📈 مثال واقعی درآمد|🧮 ماشین حساب درآمد)$"
            ),
            active_passive_income_router,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            active_passive_income_input,
            block=False,
        ),
        group=2,
    )


    # ============================================================
    # قانون بودجه 50/30/20
    # ============================================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^📋 قانون بودجه 50/30/20$"),
            budget_50_30_20_menu,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(
                r"^(📘 قانون 50/30/20 چیست؟|📈 مثال واقعی بودجه|🧮 ماشین حساب بودجه)$"
            ),
            budget_50_30_20_router,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            budget_50_30_20_input,
            block=False,
        ),
        group=2,
    )

