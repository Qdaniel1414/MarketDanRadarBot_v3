from telegram import Update
from telegram.ext import ContextTypes

from services.global_service import get_global_prices



def format_price(value):

    return f"{value:,.2f}"



async def global_prices(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    prices = get_global_prices()


    if not prices:

        await update.message.reply_text(
            "❌ دریافت اطلاعات بازار جهانی ناموفق بود."
        )

        return



    text = """
🌍 بازارهای جهانی

━━━━━━━━━━━━━━

🥇 انس جهانی طلا:
{}

🥈 انس نقره:
{}

🔶 مس جهانی:
{}

🛢 نفت WTI:
{}

🛢 نفت برنت:
{}

📈 Nasdaq 100:
{}

📊 Dow Jones:
{}

📊 S&P 500:
{}

━━━━━━━━━━━━━━

⏱ بروزرسانی با Yahoo Finance
""".format(

        format_price(
            prices.get("انس جهانی طلا", 0)
        ),

        format_price(
            prices.get("انس نقره", 0)
        ),

        format_price(
            prices.get("مس جهانی", 0)
        ),

        format_price(
            prices.get("نفت WTI", 0)
        ),

        format_price(
            prices.get("نفت برنت", 0)
        ),

        format_price(
            prices.get("Nasdaq 100", 0)
        ),

        format_price(
            prices.get("Dow Jones", 0)
        ),

        format_price(
            prices.get("S&P 500", 0)
        ),

    )


    await update.message.reply_text(
        text
    )