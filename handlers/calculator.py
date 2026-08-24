from telegram import Update
from telegram.ext import ContextTypes

from keyboards.calculator_keyboard import calculator_keyboard

async def calculator_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("CALCULATOR MENU CALLED")

    await update.message.reply_text(
        "ماشین حساب باز شد",
        reply_markup=calculator_keyboard,
    )