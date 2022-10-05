from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd
import wikipedia

wikipedia.set_lang('ru')

bot = Bot(token='PUT YOUR TOKEN HERE')
updater = Updater(token='PUT YOUR TOKEN HERE')
dispatcher = updater.dispatcher

A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введи строку, а я удалю слова содержащие "абв"')
    return A

def replaceWords(update, context):
    text = update.message.text
    if text == 'хватит':
        context.bot.send_message(update.effective_chat.id, 'введи команду /cancel')
        return B
    for word in text.split():
        if 'абв' in word:
            text = text.replace(word, '')
    context.bot.send_message(update.effective_chat.id, text)
    context.bot.send_message(update.effective_chat.id, 'Попробуем еще?')
    return A


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!!!')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
replaceWords_handler = MessageHandler(Filters.text, replaceWords)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A: [replaceWords_handler],
                                            B: [cancel_handler]},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()  # ctrl + c
