from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from config import CHANNEL_LINKS


def membership_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "📢 کانال اصلی",
                url=CHANNEL_LINKS["@MarketDanRadar"],
            )
        ],

        [
            InlineKeyboardButton(
                "📢 کانال بکاپ",
                url=CHANNEL_LINKS["@MarketDanRadarBackup"],
            )
        ],

        [
            InlineKeyboardButton(
                "💬 گروه گفتگو",
                url=CHANNEL_LINKS["@MarketDanRadar_Group"],
            )
        ],

        [
            InlineKeyboardButton(
                "✅ عضو شدم",
                callback_data="check_membership",
            )
        ],

    ]

    return InlineKeyboardMarkup(keyboard)