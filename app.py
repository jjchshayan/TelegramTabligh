from telegram.ext import Updater
from telegram import bot
#!/usr/bin/env python
# -*- coding: utf-8 -*-

updater = Updater(token='660812730:AAEGP-xXkMKoplHR6YsUECqXB8diNgvlfbs')
dispatcher = updater.dispatcher

import logging
import requests
state = 1
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="سلام خوش آمدید لطفا عکس گرفته شده را اضافه نمایید")
    state=2


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
     #my_id = 504335145
    try:
      # print(update)
      user_id = update['message']['chat']['id']
      user_name = update['message']['chat']['first_name'] 

      file_id = bot.get_file(update['message']['photo'][2]['file_id'])
      url =file_id["file_path"]
      r = requests.post("http://shayan2020.ir/Api/Telegram/UploadData.php", data={'url': url,'filename':str(user_id)+'_'+str(user_name)})
      if(r.text =="ok"):
          bot.send_message(chat_id=update.message.chat_id, text="با تشکر از شما برای اضافه کردن عکسی دیگر دگمه /start را مجددا تایپ نمایید")
      else:
          print(r.text)
          bot.send_message(chat_id=update.message.chat_id, text="خطا لطفا مجددا تلاش نمایید")
    except:
        print(update)
        bot.send_message(chat_id=update.message.chat_id, text="لطفا فقط عکس اضافه کنید")



from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.all, echo)
dispatcher.add_handler(echo_handler)


# def caps(bot, update, args=''):
#     text_caps = '   '.join(args).upper()
#     bot.send_message(chat_id=update.message.chat_id, text=text_caps)
#
#
# caps_handler = CommandHandler('caps', caps, pass_args=True)
# dispatcher.add_handler(caps_handler)

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


# from telegram.ext import InlineQueryHandler
#
# inline_caps_handler = InlineQueryHandler(inline_caps)
# dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

#
# TOKEN    = '545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo'
# HOST     = 'shayantt.herokuapp.com' # Same FQDN used when generating SSL Cert
# PORT     = 8443
# updater.start_webhook(listen="0.0.0.0",
#                       port=PORT,
#                       # url_path=TOKEN)
# updater.bot.set_webhook("https://shayantt.herokuapp.com/" + TOKEN)
# updater.idle()


updater.start_polling()

