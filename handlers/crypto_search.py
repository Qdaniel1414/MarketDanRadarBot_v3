from telegram import Update
from telegram.ext import ContextTypes

from services.provider_crypto import get_crypto_prices


async def crypto_search_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    context.user_data["crypto_search"] = True

    await update.message.reply_text(
        "🔍 نام یا نماد ارز را وارد کنید.\n\n"
        "مثال:\n"
        "BTC\n"
        "ETH\n"
        "SOL",
    )



async def crypto_search_result(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return


    if not context.user_data.get(
        "crypto_search"
    ):
        return


    query = update.message.text.strip().lower()


    prices = get_crypto_prices()


    found = None


    for name, price in prices.items():

        if (
            query in name.lower()
            or query in name.split()[-1].lower()
        ):

            found = (
                name,
                price,
            )

            break


    context.user_data.pop(
        "crypto_search",
        None,
    )


    if found:

        await update.message.reply_text(
            f"₿ {found[0]}\n\n"
            f"💵 قیمت فعلی: ${found[1]}"
        )

    else:

        await update.message.reply_text(
            "❌ ارز مورد نظر پیدا نشد."
        )