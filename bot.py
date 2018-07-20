from telegram.ext import Updater

updater = Updater(token='545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo')
dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.sendMessage(chat_id="@Shayantut", parse_mode="HTML", text="ADASD")


from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


def caps(bot, update, args=''):
    text_caps = '   '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


from telegram.ext import InlineQueryHandler

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


TOKEN    = '545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo'
HOST     = 'shayantt.herokuapp.com' # Same FQDN used when generating SSL Cert
PORT     = 8443
# updater.start_webhook(listen="0.0.0.0",
#                       port=PORT,
#                       # url_path=TOKEN)
# updater.bot.set_webhook("https://shayantt.herokuapp.com/" + TOKEN)
# updater.idle()


updater.start_polling()

