# import MySQLdb
#
# #!/usr/bin/python
#
# import MySQLdb
#
#
# # kwargs2['unix_socket'] = '/opt/lampp/var/mysql/mysql.sock'
#
# # Open database connection
# db = MySQLdb.connect("localhost","root","root","CSV_DB" )
#
#
#
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
#
# # Prepare SQL query to INSERT a record into the database.
# sql = """INSERT INTO shayan_TBL(name,
#          fammily)
#          VALUES ('Mac', 'Mohan')"""
# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Commit your changes in the database
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()
#    print("Some Error Accure")
#
# # disconnect from server
# db.close()




# from telegram.ext import Updater
# import os
# from telegram.ext import Updater
#
# updater = Updater(token='545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo')
# dispatcher = updater.dispatcher
#
# import logging
#
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#
#
# def start(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
#
#
# from telegram.ext import CommandHandler
#
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)
#
#
# def echo(bot, update):
#     bot.sendMessage(chat_id="@Shayantut", parse_mode="HTML", text="ADASD")
#
#
# from telegram.ext import MessageHandler, Filters
#
# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)
#
#
# def caps(bot, update, args=''):
#     text_caps = '   '.join(args).upper()
#     bot.send_message(chat_id=update.message.chat_id, text=text_caps)
#
#
# caps_handler = CommandHandler('caps', caps, pass_args=True)
# dispatcher.add_handler(caps_handler)
#
# from telegram import InlineQueryResultArticle, InputTextMessageContent
#
#
# def inline_caps(bot, update):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     bot.answer_inline_query(update.inline_query.id, results)
#
#
# from telegram.ext import InlineQueryHandler
#
# inline_caps_handler = InlineQueryHandler(inline_caps)
# dispatcher.add_handler(inline_caps_handler)
#
#
# def unknown(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
#
#
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)
#
#
# # updater.start_polling()
# TOKEN = "545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo"
# PORT = int(os.environ.get('PORT', '8443'))
# # updater = Updater(TOKEN)
# # add handlers
# updater.start_webhook(listen="0.0.0.0",
#                       port=PORT,
#                       url_path=TOKEN)
# updater.bot.set_webhook("https://bibliotheque-mandarine-74788.herokuapp.com/" + TOKEN)
#
#
#
#
#
#






import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.effective_message.reply_text("Hi!")


def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo"
    NAME = "shayantt"

    # Port is given by Heroku
    PORT = 8443
        # os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()

