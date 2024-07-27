from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Привет! Я эхо-бот. Напиши мне что-нибудь, и я повторю это обратно!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:

    updater = Updater(
        "6550296076:AAHl0HRwrISvRIxA_o4uCikoaaddzp2Znao", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(
        filters.text & ~filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
