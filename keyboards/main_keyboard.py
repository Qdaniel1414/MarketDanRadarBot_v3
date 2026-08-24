from telegram import KeyboardButton, ReplyKeyboardMarkup

from buttons import *

main_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(BTN_MARKET),
            KeyboardButton(BTN_CALCULATORS),
        ],
        [
            KeyboardButton(BTN_EDUCATION),
            KeyboardButton(BTN_AI),
        ],
        [
            KeyboardButton(BTN_IRAN),
            KeyboardButton(BTN_GLOBAL),
        ],
        [
            KeyboardButton(BTN_PROFILE),
            KeyboardButton(BTN_APP),
        ],
        [
            KeyboardButton(BTN_HOME),
        ],
    ],
    resize_keyboard=True,
)