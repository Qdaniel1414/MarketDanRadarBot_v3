from telegram.ext import MessageHandler, filters

from handlers.calculator import calculator_menu
from handlers.calculator_conversation import calculator_conversation


def register_calculator_handlers(app):

    print("🔥 REGISTERING CALCULATOR MENU")

    # ==========================================
    # منوی اصلی ماشین حساب‌ها
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^🧮 ماشین حساب‌ها$"),
            calculator_menu,
        )
    )

    print("✅ CALCULATOR MENU REGISTERED")

    # ==========================================
    # ماشین حساب‌های تعاملی
    # ==========================================

    app.add_handler(
        calculator_conversation
    )

    print("✅ CALCULATOR CONVERSATION REGISTERED")