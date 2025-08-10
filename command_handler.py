# command_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Redeem Request", callback_data='redeem')],
        [InlineKeyboardButton("Buy Premium", callback_data='buy_premium')],
        [InlineKeyboardButton("Service", callback_data='service')],
        [InlineKeyboardButton("Dev", callback_data='dev')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"Hello {update.effective_user.first_name}, welcome to LogicX! 🔥",
        reply_markup=reply_markup
    )
