from telegram.ext import (
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
)

from core.start_handlers import register_start_handlers


def register_handlers(app):
    register_start_handlers(app)