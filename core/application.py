from telegram.ext import Application


def create_application(token: str) -> Application:
    """Create Telegram application."""
    return Application.builder().token(token).build()