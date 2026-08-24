from telegram.ext import MessageHandler, filters

from handlers.contact import contact_handler


def register_contact_handlers(app):

    app.add_handler(
        MessageHandler(
            filters.CONTACT,
            contact_handler,
        )
    )