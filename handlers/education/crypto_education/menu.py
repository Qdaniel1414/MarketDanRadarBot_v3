from telegram import Update
from telegram.ext import ContextTypes

from keyboards.crypto_education_keyboard import (
    crypto_education_keyboard,
)

from handlers.education.crypto_education.bitcoin import (
    bitcoin_intro,
)

from handlers.education.crypto_education.blockchain import (
    blockchain_intro,
)

# آلت کوین
from handlers.education.crypto_education.altcoin.intro import (
    altcoin_intro,
)

# استیبل کوین
from handlers.education.crypto_education.stablecoin.intro import (
    stablecoin_intro,
)

from handlers.education.crypto_education.usdt import (
    usdt_intro,
)

from handlers.education.crypto_education.smart_contract import (
    smart_contract_intro,
)

from handlers.education.crypto_education.defi import (
    defi_intro,
)

from handlers.education.crypto_education.nft import (
    nft_intro,
)

from handlers.education.crypto_education.mining import (
    mining_intro,
)

from handlers.education.crypto_education.glossary import (
    glossary_intro,
)
from handlers.education.crypto_education.calculators import (
    crypto_calculators_menu,
)


async def crypto_education_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🌑 آموزش ارزهای دیجیتال\n\n"
        "یکی از بخش‌های زیر را انتخاب کنید:",
        reply_markup=crypto_education_keyboard,
    )


async def crypto_education_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = update.message.text.strip()
    print("CRYPTO ROUTER:", text)
    # -----------------------
    # آموزش‌ها
    # -----------------------

    if text == "₿ بیت کوین چیست؟":
        return await bitcoin_intro(update, context)

    elif text == "⛓ بلاکچین چیست؟":
        return await blockchain_intro(update, context)

    elif text == "🪙 آلت کوین چیست؟":
        return await altcoin_intro(update, context)

    elif text == "🏦 استیبل کوین چیست؟":
        return await stablecoin_intro(update, context)

    elif text == "💵 تتر USDT":
        return await usdt_intro(update, context)

    elif text == "🧠 اسمارت کانترکت":
        return await smart_contract_intro(update, context)

    elif text == "💳 دیفای DeFi":
        return await defi_intro(update, context)

    elif text == "🎨 NFT":
        return await nft_intro(update, context)

    elif text == "⚡ ماینینگ":
        return await mining_intro(update, context)

    elif text == "🧾 واژه نامه کریپتو":
        return await glossary_intro(update, context)

    # -----------------------
    # ماشین حساب‌ها
    # -----------------------

    elif text == "🪙 ماشین حساب کریپتو":
         return await crypto_calculators_menu(update, context)

    