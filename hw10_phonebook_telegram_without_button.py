"""
1. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.(дополнительно)
(импорт и экспорт)
"""

from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

bot = Bot(token='5529752966:AAGcq-Ca6ayHJ0rLQirUVwMAAxinh6IRCT8')
updater = Updater(token='5529752966:AAGcq-Ca6ayHJ0rLQirUVwMAAxinh6IRCT8')
dispatcher = updater.dispatcher


NUMBERFIRST = 1
NUMBERSECOND = 2
OPERATION = 3

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в наш телефонный справочник.\n'
                                                       'Если вы хотите прочитать базу данных, введите /read\n'
                                                       'Если вы хотите записать в базу данных, введите /write\n')

    return NUMBERFIRST

def read(update, context):
        with open('hw10_phonebook_telegram_DATABASE.csv', 'r', encoding='utf-8') as hw10_phonebook_telegram_DATABASE:
            data_first = hw10_phonebook_telegram_DATABASE.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            #print(''.join(data_first))
            context.bot.send_message(update.effective_chat.id, ''.join(data_first))
            return data_first

def write_first_name(update, context):
    global name
    context.bot.send_message(update.effective_chat.id, 'Введите имя для записи в базу данных')
    name = update.message.text
    return NUMBERFIRST

def write_second_phone(update, context):
    global phone
    context.bot.send_message(update.effective_chat.id, 'Введите телефон для записи в базу данных')
    phone = update.message.text
    return OPERATION

def write_all(name,phone):
    with open('hw10_phonebook_telegram_DATABASE.csv', 'a', encoding='utf-8') as hw10_phonebook_telegram_DATABASE:
        hw10_phonebook_telegram_DATABASE.write(f'{name}\n;{phone}\n')
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
read_handler = CommandHandler('read', read)
numone_handler = MessageHandler(Filters.text, write_first_name)
numtwo_handler = MessageHandler(Filters.text, write_second_phone)
cancel_handler = CommandHandler('cancel', cancel)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler('read', read))
start_write_handler = dispatcher.add_handler(CommandHandler('write', write_first_name))
dispatcher.add_handler(CommandHandler('cancel', cancel))
print("script.py working now")


conv_handler = ConversationHandler(entry_points=[start_write_handler],
                                   states={
                                       NUMBERFIRST: [numone_handler],
                                       NUMBERSECOND: [numtwo_handler],
                                       OPERATION: [write_all],
                                   },
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()