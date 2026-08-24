from telegram import ReplyKeyboardMarkup


def coin_calculator_keyboard(items):

    keyboard = []

    row = []

    for item in items:

        row.append(item["name"])

        if len(row) == 2:

            keyboard.append(row)

            row = []

    if row:

        keyboard.append(row)

    keyboard.append(
        ["⬅️ بازگشت", "🏠 خانه"]
    )

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )