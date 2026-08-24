from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_user
from config import BOT_USERNAME


async def profile_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    telegram_id = update.effective_user.id

    user = get_user(telegram_id)

    if user is None:

        await update.message.reply_text(
            "❌ اطلاعات شما پیدا نشد."
        )

        return

    # ==========================================
    # اطلاعات پایه
    # ==========================================

    full_name = f"{user['first_name']}"

    if user["last_name"]:
        full_name += f" {user['last_name']}"

    username = "-"

    if user["username"]:
        username = f"@{user['username']}"

    status = "🟢 فعال"

    if user["is_active"] == 0:
        status = "🔴 غیرفعال"

    subscription = "🆓 رایگان"

    if user["subscription_type"] == "vip":
        subscription = "💎 VIP"

    elif user["subscription_type"] == "premium":
        subscription = "👑 Premium"

    expire_date = "ندارد"

    if user["subscription_expire"]:
        expire_date = user["subscription_expire"]

    wallet = f"{user['wallet_balance']:,} تومان"

    credit = user["credit"]

    # ==========================================
    # لینک دعوت
    # ==========================================

    referral_link = "-"

    if user["referral_code"]:

        referral_link = (
            f"https://t.me/{BOT_USERNAME}"
            f"?start={user['referral_code']}"
        )

    # ==========================================
    # تعداد دعوت‌ها
    # ==========================================

    referrals_count = user["referrals_count"]

    # ==========================================
    # متن پروفایل
    # ==========================================

    text = f"""
👤 پروفایل کاربری

━━━━━━━━━━━━━━━━━━

🆔 شناسه تلگرام
{user['telegram_id']}

👤 نام
{full_name}

🏷 نام کاربری
{username}

📱 شماره موبایل
{user['phone']}

⭐ سطح کاربری
👤 عضو عادی

💎 نوع اشتراک
{subscription}

📅 انقضای اشتراک
{expire_date}

💰 موجودی کیف پول
{wallet}

🎁 اعتبار
{credit}

🔗 لینک دعوت اختصاصی
{referral_link}

👥 تعداد دعوت‌ها
{referrals_count} نفر

📊 تعداد ورود
{user['login_count']}

🕒 آخرین ورود
{user['last_login']}

⚡ وضعیت حساب
{status}
"""

    await update.message.reply_text(text)