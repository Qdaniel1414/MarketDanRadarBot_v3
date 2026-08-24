from telegram import Update
from telegram.ext import ContextTypes

from config import REQUIRED_CHANNELS, CHANNEL_LINKS
from keyboards.membership_keyboard import membership_keyboard


async def check_membership(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> bool:

    user_id = update.effective_user.id

    for channel in REQUIRED_CHANNELS:

        try:

            member = await context.bot.get_chat_member(
                chat_id=channel,
                user_id=user_id,
            )

            if member.status not in (
                "member",
                "administrator",
                "creator",
            ):

                text = (
                    "📢 برای استفاده از ربات ابتدا باید عضو کانال‌ها و گروه‌های زیر شوید:\n\n"
                )

                for ch in REQUIRED_CHANNELS:
                    text += f"🔹 {CHANNEL_LINKS[ch]}\n"

                text += (
                    "\n\n"
                    "✅ بعد از عضویت روی دکمه «عضو شدم» بزنید."
                )

                await update.message.reply_text(
                    text,
                    reply_markup=membership_keyboard(),
                )

                return False

        except Exception as e:

            print(f"Membership Error -> {channel} -> {e}")

            text = (
                "📢 برای استفاده از ربات ابتدا باید عضو کانال‌ها و گروه‌های زیر شوید:\n\n"
            )

            for ch in REQUIRED_CHANNELS:
                text += f"🔹 {CHANNEL_LINKS[ch]}\n"

            text += (
                "\n\n"
                "✅ بعد از عضویت روی دکمه «عضو شدم» بزنید."
            )

            await update.message.reply_text(
                text,
                reply_markup=membership_keyboard(),
            )

            return False

    return True