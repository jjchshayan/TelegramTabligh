#!/usr/bin/env python

'''Using Webhook and self-signed certificate'''

# This file is an annotated example of a webhook based bot for
# telegram. It does not do anything useful, other than provide a quick
# template for whipping up a testbot. Basically, fill in the CONFIG
# section and run it.
# Dependencies (use pip to install them):
# - python-telegram-bot: https://github.com/leandrotoledo/python-telegram-bot
# - Flask              : http://flask.pocoo.org/
# Self-signed SSL certificate (make sure 'Common Name' matches your FQDN):
# $ openssl req -new -x509 -nodes -newkey rsa:1024 -keyout server.key -out server.crt -days 3650
# You can test SSL handshake running this script and trying to connect using wget:
# $ wget -O /dev/null https://$HOST:$PORT/
import time
from flask import Flask, request

import telegram

# CONFIG
from telegram.ext import Updater

TOKEN    = '545193892:AAF-i-kxjJBeEiVXL1PokHCCEGNnQ1sOXFo'
HOST     = 'shayantt.herokuapp.com' # Same FQDN used when generating SSL Cert
PORT     = 8443
CERT     = 'path/to/ssl/server.crt'
CERT_KEY = 'path/to/ssl/server.key'

bot = telegram.Bot(TOKEN)
updater = Updater(token=TOKEN)
app = Flask(__name__)
context = (CERT, CERT_KEY)

@app.route('/')
def hello():
    # update = telegram.update.Update.de_json(request.get_json(force=True))
    # bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')
    bot.sendMessage(chat_id="@Shayantut", parse_mode="HTML", text="ADASD")
    return 'Hello World!'


@app.route('/' + TOKEN, methods=['GET'])
def webhook():
    update = telegram.update.Update.de_json(request.get_json(force=True))
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

    return 'OK'


def setWebhook():
    print("AA")
    # add handlers
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=PORT,
    #                       url_path=TOKEN)
    # updater.bot.set_webhook("https://shayantt.herokuapp.com/" + TOKEN)
    # updater.idle()

   # // bot.setWebhook(url='https://%s:%s/%s' % (HOST, PORT, TOKEN)
   #               )

if __name__ == '__main__':
    setWebhook()
    time.sleep(5)
    app.run(debug=True, use_reloader=True)
   # app.run(host='0.0.0.0',
      #      port=PORT,
       #     debug=True)
