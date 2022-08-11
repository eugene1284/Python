"""
Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

Прикрутить бота к задачам с предыдущего семинара:
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
"""

import datetime
from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from lec5_4_spy import log


x = ()
def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['+', '-', '*','/']]

    update.message.reply_text(
        'Hi! I am Calc Bot.'
        'введи число 1',
        )

    return x


OPERATION = ()
def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['+', '-', '*','/']]

    update.message.reply_text(
        'Hi! I am Calc Bot.'
        'I can calc:\n/sum a b\n/dif a b\n/mult a b\n/div a b'
        'Or you can choose operation.\n\n',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder=''
        ),
    )

    return OPERATION


def hello_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello, {update.effective_user.first_name}!')
    update.message.reply_text(f'This bot can calc:\n/sum a b\n/dif a b\n/mult a b\n/div a b')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split() #sum 123 345
    print(msg)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}+{y} = {x+y}')

def dif_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split() #sum 123 345
    print(msg)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}-{y} = {x-y}')

def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split() #sum 123 345
    print(msg)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}*{y} = {x*y}')

def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split() #sum 123 345
    print(msg)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}/{y} = {x/y}')

updater = Updater("token")

updater.dispatcher.add_handler(CommandHandler("start", start))
if (OPERATION == "+"): updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
updater.dispatcher.add_handler(CommandHandler("dif", dif_command))
updater.dispatcher.add_handler(CommandHandler("mult", mult_command))
updater.dispatcher.add_handler(CommandHandler("div", div_command))


print("script.py working now")

updater.start_polling()
updater.idle()
