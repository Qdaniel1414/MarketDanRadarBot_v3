from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    filters,
)

from handlers.calculators.percent import (
    start_percent,
    percent_handler,
)

from handlers.calculators.profit import (
    start_profit,
    profit_handler,
)

from handlers.calculators.compound import (
    start_compound,
    compound_handler,
)

from handlers.calculators.average import (
    start_average,
    average_handler,
)

from handlers.calculators.tp_sl import (
    start_tp_sl,
    tp_sl_handler,
)

from handlers.calculators.risk_reward import (
    start_risk_reward,
    risk_reward_handler,
)

from handlers.calculators.currency_converter import (
    start_currency_converter,
    currency_converter_handler,
)

from handlers.calculators.gold_converter import (
    start_gold_converter,
    gold_converter_handler,
)

from handlers.calculators.loan import (
    start_loan,
    loan_handler,
)


# ============================================================
# STATES
# ============================================================

PERCENT = 1
PROFIT = 2
COMPOUND = 3
AVERAGE = 4
TP_SL = 5
RISK_REWARD = 6
CURRENCY = 7
GOLD = 8
LOAN = 9


# ============================================================
# CALCULATOR CONVERSATION
# ============================================================

calculator_conversation = ConversationHandler(

    # ========================================================
    # ENTRY POINTS
    # ========================================================

    entry_points=[

        MessageHandler(
            filters.Regex(r"درصد$"),
            start_percent,
        ),

        MessageHandler(
            filters.Regex(r"سود و زیان$"),
            start_profit,
        ),

        MessageHandler(
            filters.Regex(r"سود مرکب$"),
            start_compound,
        ),

        MessageHandler(
            filters.Regex(r"میانگین خرید$"),
            start_average,
        ),

        MessageHandler(
            filters.Regex(r"حد سود و ضرر$"),
            start_tp_sl,
        ),

        MessageHandler(
            filters.Regex(r"ریسک به ریوارد$"),
            start_risk_reward,
        ),

        MessageHandler(
            filters.Regex(r"تبدیل ارز$"),
            start_currency_converter,
        ),

        MessageHandler(
            filters.Regex(r"تبدیل طلا$"),
            start_gold_converter,
        ),

        MessageHandler(
            filters.Regex(r"قسط و وام$"),
            start_loan,
        ),

    ],


    # ========================================================
    # STATES
    # ========================================================

    states={

        # ----------------------------------------------------
        # درصد
        # ----------------------------------------------------

        PERCENT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                percent_handler,
            ),

        ],


        # ----------------------------------------------------
        # سود و زیان
        # ----------------------------------------------------

        PROFIT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                profit_handler,
            ),

        ],


        # ----------------------------------------------------
        # سود مرکب
        # ----------------------------------------------------

        COMPOUND: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                compound_handler,
            ),

        ],


        # ----------------------------------------------------
        # میانگین خرید
        # ----------------------------------------------------

        AVERAGE: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                average_handler,
            ),

        ],


        # ----------------------------------------------------
        # حد سود و ضرر
        # ----------------------------------------------------

        TP_SL: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                tp_sl_handler,
            ),

        ],


        # ----------------------------------------------------
        # ریسک به ریوارد
        # ----------------------------------------------------

        RISK_REWARD: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                risk_reward_handler,
            ),

        ],


        # ----------------------------------------------------
        # تبدیل ارز
        # ----------------------------------------------------

        CURRENCY: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                currency_converter_handler,
            ),

        ],


        # ----------------------------------------------------
        # تبدیل طلا
        # ----------------------------------------------------

        GOLD: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                gold_converter_handler,
            ),

        ],


        # ----------------------------------------------------
        # قسط و وام
        # ----------------------------------------------------

        LOAN: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                loan_handler,
            ),

        ],

    },


    # ========================================================
    # FALLBACKS
    # ========================================================

    fallbacks=[

        CommandHandler(
            "start",
            lambda update, context: ConversationHandler.END,
        ),


    ],


    # ========================================================
    # OPTIONS
    # ========================================================

    allow_reentry=True,
)