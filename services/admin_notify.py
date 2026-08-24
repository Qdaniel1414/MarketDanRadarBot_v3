from config import ADMIN_CHAT_ID


async def notify_admin(
    context,
    text,
):

    try:

        if context is None:
            print("ADMIN NOTIFY -> context is None")
            return

        if context.bot is None:
            print("ADMIN NOTIFY -> bot is None")
            return

        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=text,
        )

        print("✅ ADMIN MESSAGE SENT")

    except Exception as e:

        print("❌ ADMIN NOTIFY ERROR")
        print(repr(e))