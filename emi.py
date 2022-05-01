#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
import requests
import re
import logging


def get_emi(message_text):
    x = message_text.split(" ")
    p = float(x[0])*100000
    r=float(x[1])/(12*100)
    n=float(x[2])*12
    emi = p * r * ((1+r)**n)/((1+r)**n - 1)
    return emi

def emi(update: Update, context: CallbackContext):
    text = ' '.join(context.args)
    emi = get_emi(text)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Monthly Emi="+str(emi))
def help(update: Update, context: CallbackContext):
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #                  level=logging.INFO)
    # text = ' '.join(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /emi Lakhs Inerest Years /emi 17 7 15!")
def main():
    updater = Updater(TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('emi',emi))
    help_handler = CommandHandler('help', help)
    dp.add_handler(help_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
