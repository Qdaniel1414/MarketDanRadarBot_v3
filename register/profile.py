from telegram.ext import MessageHandler, filters

from handlers.profile import profile_handler


def register_profile_handlers(app):

    app.add_handler(
        MessageHandler(
            filters.Regex("^👤 پروفایل من$"),
            profile_handler,
        )
    )