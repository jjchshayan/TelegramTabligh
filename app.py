from telegram.ext import Updater
from telegram import bot
from emoji import emojize
import json
#!/usr/bin/env python
# -*- coding: utf-8 -*-



# updater = Updater(token='628591499:AAEM8_wsBtPsldKKLCr-ozepC5RId02nZGo')
updater = Updater(token='628591499:AAEM8_wsBtPsldKKLCr-ozepC5RId02nZGo')
dispatcher = updater.dispatcher

import logging
import requests

state = 1
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



# def start(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="سلام خوش آمدید لطفا عکس گرفته شده را اضافه نمایید")
#     state = 2
#
#
# from telegram.ext import CommandHandler
#
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)


def manageBot(bot, user_id,chat_id,message_id):
    bot.kickChatMember(chat_id, user_id, 3710)
    bot.deleteMessage(chat_id, message_id)


def manageNewUser(bot, message_id, isOldMemberEqualNewMember, first_name, date, user_id, chat_id):
    bot.deleteMessage(chat_id, message_id)
#     print(isOldMemberEqualNewMember, chat_id)
    if not isOldMemberEqualNewMember:
        r = requests.post("http://shayan2020.ir/Api/TelegramTabligh/user.php",
                          data={'id': str(user_id), 'type': str(1), "lastpost": str(date)})
    else:
        r = requests.post("http://shayan2020.ir/Api/TelegramTabligh/user.php",
                          data={'id': str(user_id), 'type': str(0), "lastpost": str(date)})

    response = json.loads(r.text)
    if response["items"][0]['errorcode'] == 3:
        rose = emojize(":gift:", use_aliases=True)
        s = rose + str(first_name) + 'خوش آمدید ' + rose
        s += "\n" + " برای ثبت پیام لطفا ۵ نفر را اضافه کنید " + "\n"
        s += "افراد متوجه دعوت کردن شما نخواهند شد" + " \n"
        bot.send_message(chat_id=chat_id,
                         text=s)
    else:
        print()


def manageExistUser(bot, user_id, date, first_name, message_id, chat_id):
    r = requests.post("http://shayan2020.ir/Api/TelegramTabligh/user.php",
                      data={'id': str(user_id), 'type': str(0), "lastpost": str(date)})
#     print(r.text)
    rr = json.loads(r.text)

    if len(rr["items"]) > 0:
        if rr["items"][0]['errorcode'] == 1:
            userinvite = rr["items"][0]['userinvite']
            bot.deleteMessage(chat_id, message_id)
            rose = emojize(":gift:", use_aliases=True)
            s = rose + str(first_name) + ' کاربر ' + rose + "\n"
            s += "لطفا افراد بیشتری را دعوت کنید" + ("(" + str(userinvite) + "نفر)")
            bot.send_message(chat_id=chat_id,
                             text=s)
        elif rr["items"][0]['errorcode'] == 4:
            userinvite = rr["items"][0]['diff']
            bot.deleteMessage(chat_id, message_id)
            rose = emojize(":gift:", use_aliases=True)
            s = rose + str(first_name) + ' کاربر ' + rose + "\n"
            s += "برای ارسال پست جدید لطفا صبر کنید" + ("(" + str(userinvite) + "دقیقه دیگر)")
            bot.send_message(chat_id=chat_id,
                             text=s)
        else:
            print()


def echo(bot, update):
    print(update)

    user_id = update['message']['from_user']['id']
    date = update['message']['date']
    #
    print(user_id, date)


    # 0 is no update count 1 is update count


    # print((update['message']['left_chat_member']), "OOO")
    if update['message']['left_chat_member'] is not None:
        message_id = update['message']['message_id']
        bot.deleteMessage(update.message.chat_id, message_id)

    else:

        if len(update['message']['new_chat_members']):
            # print(type(update['message']['new_chat_members'][0]['is_bot']))
           for k in range(0,len(update['message']['new_chat_members'])) 
            is_bot = update['message']['new_chat_members'][k]['is_bot']
            if is_bot:
                user_id = update['message']['new_chat_members'][k]['id']
                message_id = update['message']['message_id']
                manageBot(bot, user_id,update.message.chat_id,message_id)
            else:
                message_id = update['message']['message_id']
                isOldMemberEqualNewMember = update['message']['from_user']['id'] == \
                                            update['message']['new_chat_members'][k]['id']
                first_name = update['message']['new_chat_members'][k]['first_name']
                manageNewUser(bot, message_id, isOldMemberEqualNewMember, first_name, date, user_id,
                              update.message.chat_id)

        else:

            first_name = update['message']['from_user']['first_name']
            message_id = update['message']['message_id']

            manageExistUser(bot, user_id, date, first_name, message_id, update.message.chat_id)


from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.all, echo)
dispatcher.add_handler(echo_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
