from telegram import Update
from telegram.ext import ContextTypes

from database.users import (
    is_registered,
    update_login,
    initialize_user_data,
    create_referral_code_if_missing,
    save_pending_referral_code,
)

from handlers.register import register
from services.membership_service import check_membership
from keyboards.main_keyboard import main_keyboard


# ============================================================
# START HANDLER
# ============================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("🔥 START CALLED")

    # --------------------------------------------------------
    # بررسی وجود پیام
    # --------------------------------------------------------

    if update.message is None:
        print("❌ UPDATE MESSAGE IS NONE")
        return

    print("✅ MESSAGE EXISTS")

    # --------------------------------------------------------
    # بررسی عضویت در کانال‌ها
    # --------------------------------------------------------

    print("🔍 CHECKING MEMBERSHIP...")

    try:

        is_member = await check_membership(
            update,
            context,
        )

        print(
            "✅ MEMBERSHIP RESULT:",
            is_member
        )

    except Exception as e:

        print(
            "❌ MEMBERSHIP ERROR:",
            repr(e)
        )

        try:

            await update.message.reply_text(
                f"❌ خطا در بررسی عضویت:\n\n{e}"
            )

        except Exception as reply_error:

            print(
                "❌ ERROR SENDING MEMBERSHIP ERROR:",
                repr(reply_error)
            )

        return

    # --------------------------------------------------------
    # اگر عضو کانال‌ها نیست
    # --------------------------------------------------------

    if not is_member:

        print(
            "❌ USER IS NOT MEMBER"
        )

        try:

            await update.message.reply_text(
                "❌ عضویت شما در کانال‌های موردنیاز تأیید نشد.\n\n"
                "لطفاً ابتدا در کانال‌های موردنیاز عضو شوید "
                "و سپس دوباره /start را بزنید."
            )

        except Exception as e:

            print(
                "❌ ERROR SENDING NOT-MEMBER MESSAGE:",
                repr(e)
            )

        return

    # --------------------------------------------------------
    # عضویت تأیید شد
    # --------------------------------------------------------

    print(
        "✅ MEMBERSHIP PASSED"
    )

    # --------------------------------------------------------
    # Telegram User ID
    # --------------------------------------------------------

    if update.effective_user is None:

        print(
            "❌ EFFECTIVE USER IS NONE"
        )

        return

    telegram_id = update.effective_user.id

    print(
        "👤 TELEGRAM ID:",
        telegram_id
    )

    # ========================================================
    # ذخیره کد دعوت در صورت وجود
    # ========================================================

    if context.args and len(context.args) > 0:

        referral_code = context.args[0].strip().upper()

        # ذخیره در session کاربر
        context.user_data[
            "pending_referral_code"
        ] = referral_code

        print(
            "🎁 PENDING REFERRAL:",
            referral_code
        )

        # ----------------------------------------------------
        # ذخیره در دیتابیس در صورتی که کاربر قبلاً وجود داشته
        # ----------------------------------------------------

        try:

            if is_registered(telegram_id):

                save_pending_referral_code(
                    telegram_id,
                    referral_code,
                )

                print(
                    "✅ PENDING REFERRAL SAVED TO DATABASE:",
                    referral_code
                )

        except Exception as e:

            print(
                "❌ SAVE PENDING REFERRAL ERROR:",
                repr(e)
            )

    # ========================================================
    # بررسی اینکه کاربر قبلاً ثبت‌نام کرده یا نه
    # ========================================================

    print(
        "🔍 CHECKING USER REGISTRATION..."
    )

    try:

        registered = is_registered(
            telegram_id
        )

        print(
            "✅ IS REGISTERED:",
            registered
        )

    except Exception as e:

        print(
            "❌ IS_REGISTERED ERROR:",
            repr(e)
        )

        try:

            await update.message.reply_text(
                f"❌ خطا در بررسی حساب کاربری:\n\n{e}"
            )

        except Exception as reply_error:

            print(
                "❌ ERROR SENDING REGISTRATION ERROR:",
                repr(reply_error)
            )

        return

    # ========================================================
    # اگر کاربر قبلاً ثبت‌نام کرده
    # ========================================================

    if registered:

        print(
            "✅ USER ALREADY REGISTERED"
        )

        # ----------------------------------------------------
        # مقداردهی اولیه اطلاعات کاربر
        # ----------------------------------------------------

        try:

            initialize_user_data(
                telegram_id,
            )

            print(
                "✅ USER DATA INITIALIZED"
            )

        except Exception as e:

            print(
                "❌ INITIALIZE USER ERROR:",
                repr(e)
            )

        # ----------------------------------------------------
        # بررسی کد دعوت شخص
        # ----------------------------------------------------

        try:

            create_referral_code_if_missing(
                telegram_id,
            )

            print(
                "✅ REFERRAL CODE CHECKED"
            )

        except Exception as e:

            print(
                "❌ REFERRAL CODE ERROR:",
                repr(e)
            )

        # ----------------------------------------------------
        # بروزرسانی ورود
        # ----------------------------------------------------

        try:

            update_login(
                telegram_id,
            )

            print(
                "✅ LOGIN UPDATED"
            )

        except Exception as e:

            print(
                "❌ UPDATE LOGIN ERROR:",
                repr(e)
            )

        # ----------------------------------------------------
        # ارسال منوی اصلی
        # ----------------------------------------------------

        try:

            await update.message.reply_text(
                f"""
👋 سلام {update.effective_user.first_name}

به ربات MARKET DAN RADAR خوش آمدید.

لطفاً یکی از گزینه‌های زیر را انتخاب کنید.
""",
                reply_markup=main_keyboard,
            )

            print(
                "✅ MAIN KEYBOARD SENT"
            )

        except Exception as e:

            print(
                "❌ MAIN KEYBOARD ERROR:",
                repr(e)
            )

        return

    # ========================================================
    # کاربر جدید است → ثبت‌نام
    # ========================================================

    print(
        "🆕 NEW USER → START REGISTRATION"
    )

    try:

        await register(
            update,
            context,
        )

        print(
            "✅ REGISTER FUNCTION FINISHED"
        )

    except Exception as e:

        print(
            "❌ REGISTER ERROR:",
            repr(e)
        )

        try:

            await update.message.reply_text(
                f"❌ خطا در ثبت‌نام:\n\n{e}"
            )

        except Exception as reply_error:

            print(
                "❌ ERROR SENDING REGISTER ERROR:",
                repr(reply_error)
            )


# ============================================================
# JOINED HANDLER
# ============================================================

async def joined_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    print(
        "🔥 JOINED HANDLER CALLED"
    )

    return await start(
        update,
        context,
    )