# handlers/admin_handler.py

from telegram import Update
from telegram.ext import CallbackContext
import json

# Load user data
def load_user_data():
    try:
        with open('data/users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(users):
    with open('data/users.json', 'w') as f:
        json.dump(users, f)

def broadcast_message(update: Update, context: CallbackContext) -> None:
    if update.effective_user.id != context.bot_data['admin_id']:
        update.message.reply_text("You are not authorized to use this command.")
        return

    text = ' '.join(context.args)
    if text:
        users = load_user_data()
        for user_id in users.keys():
            context.bot.send_message(chat_id=user_id, text=text)
        update.message.reply_text("Message sent to all users.")
    else:
        update.message.reply_text("Please provide a message to broadcast.")

def ban_user(update: Update, context: CallbackContext) -> None:
    if update.effective_user.id != context.bot_data['admin_id']:
        update.message.reply_text("You are not authorized to use this command.")
        return

    if context.args:
        user_id = context.args[0]
        users = load_user_data()
        if user_id in users:
            users[user_id]['banned'] = True
            save_user_data(users)
            update.message.reply_text(f"User {user_id} has been banned.")
        else:
            update.message.reply_text(f"User {user_id} not found.")
    else:
        update.message.reply_text("Please provide a user ID to ban.")

def unban_user(update: Update, context: CallbackContext) -> None:
    if update.effective_user.id != context.bot_data['admin_id']:
        update.message.reply_text("You are not authorized to use this command.")
        return

    if context.args:
        user_id = context.args[0]
        users = load_user_data()
        if user_id in users and users[user_id].get('banned', False):
            users[user_id]['banned'] = False
            save_user_data(users)
            update.message.reply_text(f"User {user_id} has been unbanned.")
        else:
            update.message.reply_text(f"User {user_id} not found or not banned.")
    else:
        update.message.reply_text("Please provide a user ID to unban.")
