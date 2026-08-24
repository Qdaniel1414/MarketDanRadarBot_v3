from telegram import Update
from telegram.ext import ContextTypes

from services.membership_service import check_membership
from handlers.start import start


async def membership_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    if query.data != "check_membership":
        return

    ok = await check_membership(
        update,
        context,
    )

    if ok:
        await query.message.delete()

        # نگه داشتن اطلاعات Referral
        referral_code = context.user_data.get("pending_referral_code")

        if referral_code:
            context.user_data["referral_code"] = referral_code

        await start(update, context)