from telegram import Update
from telegram.ext import ContextTypes

from database.users import (
    add_user,
    get_pending_referral_code,
    clear_pending_referral_code,
)

from keyboards.main_keyboard import main_keyboard

from services.referral_service import (
    get_user_by_referral_code,
    set_referrer,
    increase_referrals,
    add_referral_reward,
    has_referrer,
    save_referral,
    referral_exists,
)

from services.admin_notify import notify_admin


async def contact_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    # ==========================================
    # بررسی وجود پیام
    # ==========================================

    if update.message is None:
        return

    if update.message.contact is None:
        return

    # ==========================================
    # اطلاعات کاربر
    # ==========================================

    user = update.effective_user
    contact = update.message.contact

    if user is None:
        return

    telegram_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    phone_number = contact.phone_number

    # ==========================================
    # ثبت کاربر
    # ==========================================

    add_user(
        telegram_id,
        first_name,
        last_name,
        username,
        phone_number,
    )

    print("====== USER REGISTERED ======")
    print("TELEGRAM ID:", telegram_id)
    print("PHONE:", phone_number)

    # ==========================================
    # بررسی لینک دعوت
    # ==========================================

    # ابتدا رفرال ذخیره‌شده در همین session را می‌خوانیم
    referral_code = context.user_data.get(
        "pending_referral_code"
    )

    # اگر در session نبود، از دیتابیس می‌خوانیم
    if not referral_code:

        referral_code = get_pending_referral_code(
            telegram_id
        )

    print(
        "🎁 REFERRAL CODE USED:",
        referral_code
    )

    # ==========================================
    # پردازش رفرال
    # ==========================================

    if referral_code:

        print(
            "🎁 PENDING REFERRAL:",
            referral_code
        )

        referrer = get_user_by_referral_code(
            referral_code
        )

        # --------------------------------------
        # دعوت‌کننده پیدا شد
        # --------------------------------------

        if referrer:

            print(
                "✅ REFERRER FOUND:",
                referrer["telegram_id"],
            )

            # ----------------------------------
            # جلوگیری از دعوت خود شخص
            # و جلوگیری از ثبت دعوت مجدد
            # ----------------------------------

            if (
                referrer["telegram_id"] != telegram_id
                and not has_referrer(telegram_id)
            ):

                # ------------------------------
                # ثبت دعوت‌کننده
                # ------------------------------

                set_referrer(
                    telegram_id,
                    referrer["telegram_id"],
                )

                print(
                    "✅ REFERRER SET:",
                    referrer["telegram_id"],
                    "->",
                    telegram_id,
                )

                # ------------------------------
                # بررسی وجود رکورد رفرال
                # ------------------------------

                if not referral_exists(
                    referrer["telegram_id"],
                    telegram_id,
                ):

                    # --------------------------
                    # افزایش تعداد دعوت‌ها
                    # --------------------------

                    increase_referrals(
                        referrer["telegram_id"],
                    )

                    # --------------------------
                    # اضافه کردن پاداش
                    # --------------------------

                    add_referral_reward(
                        referrer["telegram_id"],
                        1000,
                    )

                    # --------------------------
                    # ذخیره رکورد رفرال
                    # --------------------------

                    save_referral(
                        referrer["telegram_id"],
                        telegram_id,
                        referral_code,
                    )

                    print(
                        "====== SEND REFERRAL MESSAGE ======"
                    )

                    # --------------------------
                    # اطلاع به ادمین
                    # --------------------------

                    await notify_admin(
                        context,
                        f"""
🎉 دعوت جدید

👤 دعوت کننده:
{referrer["telegram_id"]}

👤 عضو جدید:
{telegram_id}

🎁 جایزه:
1000 اعتبار
""",
                    )

                    print(
                        "====== REFERRAL MESSAGE SENT ======"
                    )

                    print(
                        "✅ REFERRAL REGISTERED:",
                        referrer["telegram_id"],
                        "->",
                        telegram_id,
                    )

                else:

                    print(
                        "⚠️ REFERRAL ALREADY EXISTS"
                    )

            else:

                print(
                    "⚠️ SELF REFERRAL OR USER ALREADY HAS REFERRER"
                )

        else:

            print(
                "❌ REFERRER NOT FOUND:",
                referral_code
            )

        # --------------------------------------
        # پاک کردن رفرال موقت
        # --------------------------------------

        clear_pending_referral_code(
            telegram_id
        )

        # پاک کردن از session
        context.user_data.pop(
            "pending_referral_code",
            None
        )

    # ==========================================
    # اطلاع ثبت نام جدید به ادمین
    # ==========================================

    print(
        "====== SEND ADMIN MESSAGE ======"
    )

    await notify_admin(
        context,
        f"""
🆕 ثبت نام جدید

👤 نام:
{first_name}

🆔 Telegram ID:
{telegram_id}

📱 شماره:
{phone_number}

👤 Username:
@{username if username else "-"}
""",
    )

    print(
        "====== ADMIN MESSAGE SENT ======"
    )

    # ==========================================
    # خوش آمدگویی
    # ==========================================

    await update.message.reply_text(
        f"""
🎉 ثبت‌نام شما با موفقیت انجام شد.

👋 سلام {first_name}

به خانواده MARKET DAN RADAR خوش آمدید.

از این پس به تمام امکانات رایگان ربات دسترسی دارید.

📚 آموزش‌ها
📊 قیمت‌های لحظه‌ای
🧮 ماشین حساب‌ها
🤖 هوش مصنوعی
💰 بازار ایران
🌍 بازارهای جهانی

لطفاً یکی از گزینه‌های زیر را انتخاب کنید.
""",
        reply_markup=main_keyboard,
    )