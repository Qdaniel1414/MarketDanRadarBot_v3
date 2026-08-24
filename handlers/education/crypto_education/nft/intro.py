from telegram import Update
from telegram.ext import ContextTypes


async def nft_intro(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    text = (
        "🎨 NFT چیست؟\n\n"

        "NFT مخفف عبارت:\n"
        "Non-Fungible Token\n\n"

        "به معنی:\n"
        "توکن غیرقابل تعویض\n\n"

        "برخلاف بیت‌کوین یا تتر، هر NFT منحصر‌به‌فرد است.\n\n"

        "کاربردها:\n\n"

        "🖼 آثار هنری\n"
        "🎮 آیتم‌های بازی\n"
        "🎵 موسیقی\n"
        "🎬 فیلم و ویدئو\n"
        "🏠 اسناد مالکیت دیجیتال\n"
        "🎟 بلیت رویدادها\n\n"

        "مزایا:\n\n"

        "✅ مالکیت واقعی فایل دیجیتال\n"
        "✅ قابل خرید و فروش در بلاکچین\n"
        "✅ جلوگیری از جعل\n\n"

        "ریسک‌ها:\n\n"

        "❌ نوسان قیمت\n"
        "❌ احتمال کلاهبرداری پروژه‌ها\n"
        "❌ نقدشوندگی پایین بعضی NFTها\n\n"

        "بازارهای معروف NFT:\n\n"

        "🟦 OpenSea\n"
        "🟪 Blur\n"
        "🟨 Magic Eden\n\n"

        "🎯 بیشتر NFTها روی شبکه اتریوم ایجاد می‌شوند."
    )

    await update.message.reply_text(text)