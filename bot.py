# bot.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from config import TOKEN, ADMIN_ID
from handlers.command_handler import start
from handlers.button_handler import button_handler
from handlers.admin_handler import broadcast_message, ban_user, unban_user

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Store admin ID in bot data
    dp.bot_data['admin_id'] = ADMIN_ID

    # Command and button handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))

    # Admin commands
    dp.add_handler(CommandHandler("broadcast", broadcast_message))
    dp.add_handler(CommandHandler("ban", ban_user))
    dp.add_handler(CommandHandler("unban", unban_user))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
