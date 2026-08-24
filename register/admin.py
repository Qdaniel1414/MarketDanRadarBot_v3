from telegram.ext import CommandHandler

from handlers.admin import (
    set_usd,
    set_usdt,
    set_aed,
    set_eur,
    set_gbp,
    set_try,
    set_gold18,
    set_gold24,
    set_melted,
    set_imami,
    set_bahar,
    set_nim,
    set_rob,
    set_gerami,
    set_ounce,
    set_btc,
    set_eth,

    # کامودیتی‌ها
    set_wti,
    set_brent,
    set_gas,
    set_silver,
    set_copper,

    # شاخص‌ها
    set_sp500,
    set_nasdaq,
    set_dow,
    set_vix,

    # سهام آمریکا
    set_nvda,
    set_aapl,
    set_msft,
    set_googl,
    set_amzn,
    set_meta,
    set_jpm,
)


def register_admin_handlers(app):

    # =====================================
    # ارز
    # =====================================

    app.add_handler(
        CommandHandler(
            "setusd",
            set_usd,
        )
    )

    app.add_handler(
        CommandHandler(
            "setusdt",
            set_usdt,
        )
    )

    app.add_handler(
        CommandHandler(
            "setaed",
            set_aed,
        )
    )

    app.add_handler(
        CommandHandler(
            "seteur",
            set_eur,
        )
    )

    app.add_handler(
        CommandHandler(
            "setgbp",
            set_gbp,
        )
    )

    app.add_handler(
        CommandHandler(
            "settry",
            set_try,
        )
    )

    # =====================================
    # طلا و سکه
    # =====================================

    app.add_handler(
        CommandHandler(
            "setgold18",
            set_gold18,
        )
    )

    app.add_handler(
        CommandHandler(
            "setgold24",
            set_gold24,
        )
    )

    app.add_handler(
        CommandHandler(
            "setmelted",
            set_melted,
        )
    )

    app.add_handler(
        CommandHandler(
            "setimami",
            set_imami,
        )
    )

    app.add_handler(
        CommandHandler(
            "setbahar",
            set_bahar,
        )
    )

    app.add_handler(
        CommandHandler(
            "setnim",
            set_nim,
        )
    )

    app.add_handler(
        CommandHandler(
            "setrob",
            set_rob,
        )
    )

    app.add_handler(
        CommandHandler(
            "setgerami",
            set_gerami,
        )
    )

    # =====================================
    # قیمت‌های جهانی
    # =====================================

    app.add_handler(
        CommandHandler(
            "setounce",
            set_ounce,
        )
    )

    app.add_handler(
        CommandHandler(
            "setbtc",
            set_btc,
        )
    )

    app.add_handler(
        CommandHandler(
            "seteth",
            set_eth,
        )
    )

    # =====================================
    # کامودیتی‌ها
    # =====================================

    app.add_handler(
        CommandHandler(
            "setwti",
            set_wti,
        )
    )

    app.add_handler(
        CommandHandler(
            "setbrent",
            set_brent,
        )
    )

    app.add_handler(
        CommandHandler(
            "setgas",
            set_gas,
        )
    )

    app.add_handler(
        CommandHandler(
            "setsilver",
            set_silver,
        )
    )

    app.add_handler(
        CommandHandler(
            "setcopper",
            set_copper,
        )
    )

    # =====================================
    # شاخص‌های اصلی
    # =====================================

    app.add_handler(
        CommandHandler(
            "setsp500",
            set_sp500,
        )
    )

    app.add_handler(
        CommandHandler(
            "setnasdaq",
            set_nasdaq,
        )
    )

    app.add_handler(
        CommandHandler(
            "setdow",
            set_dow,
        )
    )

    app.add_handler(
        CommandHandler(
            "setvix",
            set_vix,
        )
    )

    # =====================================
    # سهام آمریکا
    # =====================================

    app.add_handler(
        CommandHandler(
            "setnvda",
            set_nvda,
        )
    )

    app.add_handler(
        CommandHandler(
            "setaapl",
            set_aapl,
        )
    )

    app.add_handler(
        CommandHandler(
            "setmsft",
            set_msft,
        )
    )

    app.add_handler(
        CommandHandler(
            "setgoogl",
            set_googl,
        )
    )

    app.add_handler(
        CommandHandler(
            "setamzn",
            set_amzn,
        )
    )

    app.add_handler(
        CommandHandler(
            "setmeta",
            set_meta,
        )
    )

    app.add_handler(
        CommandHandler(
            "setjpm",
            set_jpm,
        )
    )