from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from Bot_operator.dialogs import answer_to, initial_phrase


def start(update: Update, context: CallbackContext):
    name = update.effective_chat.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Здравствуйте, {name}!"
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=initial_phrase()
    )


def new(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=initial_phrase()
    )


def text(update: Update, context: CallbackContext):
    text_received = update.message.text
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=answer_to(text=text_received)
    )


def main():
    TOKEN = '2119617790:AAEDEYMqdpaSSjveKv7ytj7xRb2Mf5beb14'
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    new_handler = CommandHandler('new', new)
    dispatcher.add_handler(new_handler)

    text_handler = MessageHandler(Filters.text, text)
    dispatcher.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
