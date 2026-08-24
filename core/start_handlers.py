from telegram.ext import CommandHandler

# ایمپورت تابع start از همان فایلی که الان داخل bot.py از آن استفاده می‌کنی
from handlers.start import start   # اگر مسیر متفاوت است، همان مسیر فعلی را بنویس


def register_start_handlers(app):
    app.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )