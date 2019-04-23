from telegram.ext import Updater
from telegram import bot, InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize
import json
from threading import Timer

# !/usr/bin/env python
# -*- coding: utf-8 -*-


bot_message_id = 100000

# updater = Updater(token='628591499:AAEM8_wsBtPsldKKLCr-ozepC5RId02nZGo')
updater = Updater(token='628591499:AAEM8_wsBtPsldKKLCr-ozepC5RId02nZGo')  # tablighatRaygan
# updater = Updater(token='660812730:AAEGP-xXkMKoplHR6YsUECqXB8diNgvlfbs') # GoleMaryamBot

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


def manageBot(bot, user_id, chat_id):
    # print(user_id,"KKKKKKKKKKKKKk")
    # bot.kickChatMember(chat_id, user_id, 3710)
    bot.restrictChatMember(chat_id=chat_id, user_id=user_id, until_date=3710, can_send_messages=False,
                           can_send_media_messages=False, can_send_other_messages=False,
                           can_add_web_page_previews=False)


def removeMessageBot(bot, chat_id, message_id):
    bot.deleteMessage(chat_id, message_id)


def manageNewUser(bot, message_id, isOldMemberEqualNewMember, first_name, date, user_id_new, user_id, chat_id):
    #     print(isOldMemberEqualNewMember, chat_id)
    if not isOldMemberEqualNewMember:
        r = requests.post("http://shayan2020.ir/Api/TelegramTabligh/user.php",
                          data={'id': str(user_id_new), 'type': str(1), "lastpost": str(date), 'GroupAllowID': chat_id})


    else:
        r = requests.post("http://shayan2020.ir/Api/TelegramTabligh/user.php",
                          data={'id': str(user_id_new), 'type': str(0), "lastpost": str(date), 'GroupAllowID': chat_id})

        response = json.loads(r.text)
        if response["items"][0]['errorcode'] == 3:
            rose = emojize(":gift:", use_aliases=True)
            s = rose + str(first_name) + ' خوش آمدید ' + rose
            s += "\n" + " برای ثبت پیام لطفا ۱۶ نفر را اضافه کنید " + "\n"
            s += "افراد متوجه دعوت کردن شما نخواهند شد" + " \n"
            keyboard = [[InlineKeyboardButton("محصولات دکوآرت", url='https://t.me/deccoArt', callback_data='@deccoArt'),
                         ]]

            reply_markup = InlineKeyboardMarkup(keyboard)
            result = bot.send_message(chat_id=chat_id,
                                      text=s, disable_notification=True, reply_markup=reply_markup)

            t = Timer(15.0, removeMessageBot, [bot, chat_id, result['message_id']])
            t.start()  # after 30 seconds, "hello, world" will be printed


        else:
            pass


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def manageExistUser(bot, user_id, date, first_name, message_id, chat_id):
    r = requests.post("http://shayan2020.ir/Api/TelegramTabligh/user.php",
                      data={'id': str(user_id), 'type': str(0), "lastpost": str(date), 'GroupAllowID': chat_id})
    print(r.text, "   ", chat_id)
    rr = json.loads(r.text)
    # print("KKKKKKK")
    if len(rr["items"]) > 0:
        if rr["items"][0]['errorcode'] == 1:
            userinvite = rr["items"][0]['userinvite']
            bot.deleteMessage(chat_id, message_id)
            rose = emojize(":gift:", use_aliases=True)
            s = rose + str(first_name) + ' کاربر ' + rose + "\n"
            s += "لطفا افراد بیشتری را دعوت کنید" + ("(" + str(userinvite) + "نفر)")

            keyboard = [[InlineKeyboardButton("محصولات دکوآرت", url='https://t.me/deccoArt', callback_data='@deccoArt'),
                         ]]

            reply_markup = InlineKeyboardMarkup(keyboard)
            result = bot.send_message(chat_id=chat_id,
                                      text=s, disable_notification=True, reply_markup=reply_markup)

            t = Timer(15.0, removeMessageBot, [bot, chat_id, result['message_id']])
            t.start()  # after 30 seconds, "hello, world" will be printed
        elif rr["items"][0]['errorcode'] == 4:
            userinvite = rr["items"][0]['diff']
            bot.deleteMessage(chat_id, message_id)
            rose = emojize(":gift:", use_aliases=True)
            s = rose + str(first_name) + ' کاربر ' + rose + "\n"
            s += "برای ارسال پست جدید لطفا صبر کنید" + ("(" + str(userinvite) + "دقیقه دیگر)")
            result = bot.send_message(chat_id=chat_id,
                                      text=s)
            t = Timer(15.0, removeMessageBot, [bot, chat_id, result['message_id']])
            t.start()  # after 30 seconds, "hello, world" will be printed
        # else:
        #      bot.deleteMessage(chat_id, message_id)


def echo(bot, update):
    global bot_message_id

    # message_id = update['message']['message_id']
    # user_id = update['message']['new_chat_members'][0]['id']
    # bot_message_id = message_id
    # manageBot(bot, user_id, update.message.chat_id)
    # user_id = update['message']['new_chat_members'][0]['id']
    # manageBot(bot, user_id, update.message.chat_id)

    # print(update)
    # print( )
    # print(update['message']['forward_from']['is_bot'])
    user_id = update['message']['from_user']['id']
    date = update['message']['date']
    #
    # print(user_id, date)

    # for i in range(400, 475):
    #     try:
    #         print(i)
    #         bot.deleteMessage(update.message.chat_id, i)
    #         # bot_message_id = message_id
    #     except:
    #         print()

    # 0 is no update count 1 is update count

    # print((update['message']['left_chat_member']), "OOO")
    if update['message']['left_chat_member'] is not None:

        message_id = update['message']['message_id']
        bot.deleteMessage(update.message.chat_id, message_id)
        if update['message']['left_chat_member']['is_bot']:
            # print(bot_message_id,message_id)
            pass

    else:

        if len(update['message']['new_chat_members']):
            # print(type(update['message']['new_chat_members'][0]['is_bot']))
            for u in range(0, len(update['message']['new_chat_members'])):
                #                 print(u,"@@@@@@@@@")
                is_bot = update['message']['new_chat_members'][u]['is_bot']
                if is_bot:
                    try
                        message_id = update['message']['message_id']
                        user_id = update['message']['new_chat_members'][u]['id']
                        bot_message_id = message_id
                        try:
                            manageBot(bot, user_id, update.message.chat_id)
                        except:
                            print()
                        try:
                            user_id_from = update['message']['from_user']['id']
                            manageBot(bot, user_id_from, update.message.chat_id)
                        except:
                            print()
                        # print("AAAAAAAA", update['message']['from_user'])
                        # user_id = update['message']['from_user']['id'][';;']

                        # manageBot(bot, user_id, update.message.chat_id)
                        try:
                         result = bot.deleteMessage(update.message.chat_id, message_id)
                    #                         print(result)
                        except:
                            print()
                    except:
                        print()

                else:
                    message_id = update['message']['message_id']
                    userinvitecount = len(update['message']['new_chat_members'])
                    if u == 0:
                        bot.deleteMessage(update.message.chat_id, message_id)
                        r2 = requests.post("http://shayan2020.ir/Api/TelegramTabligh/userinviteupdate.php",
                                           data={'id': str(user_id), "count": str(userinvitecount)})
                        #         print(r2.text)
                    isOldMemberEqualNewMember = update['message']['from_user']['id'] == \
                                                update['message']['new_chat_members'][u]['id']
                    first_name = update['message']['new_chat_members'][u]['first_name']
                    user_id_new = update['message']['new_chat_members'][u]['id']

                    manageNewUser(bot, message_id, isOldMemberEqualNewMember, first_name, date, user_id_new, user_id,
                                  update.message.chat_id)
        elif update['message']['forward_from'] is not None:
            if update['message']['forward_from']['is_bot']:
                message_id = update['message']['message_id']
                bot.deleteMessage(update.message.chat_id, message_id)
                user_id_from = update['message']['from_user']['id']
                manageBot(bot, user_id_from, update.message.chat_id)

        else:

            first_name = update['message']['from_user']['first_name']
            message_id = update['message']['message_id']
            #             print(update.message.chat_id)
            manageExistUser(bot, user_id, date, first_name, message_id, update.message.chat_id)


from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.all, echo)
dispatcher.add_handler(echo_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling(poll_interval=1.0, timeout=20)
# updater.start_polling()
updater.idle()
