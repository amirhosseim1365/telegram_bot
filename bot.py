from KEYS import TELEGRAM_KEY
from responses import sample_responses
from telegram.ext import *


print('Bot Started...')

def start_command(update, context):
    update.message.reply_text('Type Something random to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help you can google it!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response=sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def main():
    updater=Updater(TELEGRAM_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler
    (error)

    updater.start_polling()
    updater.idle()

main()