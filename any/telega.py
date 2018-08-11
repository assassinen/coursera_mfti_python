import telebot
import requests

# token = "676472735:AAHq8-RIu0q0fGoZxfNOOPH2Q4HiAn2A9fg"
token = '571960112:AAHOYCVUu54nwJklf7z3x_RhVHmjhiRqQuM'

from telegram.ext import Updater, CommandHandler


# def hello(bot, update):
#     update.message.reply_text(
#         'Hello {}'.format(update.message.from_user.first_name))
#
#
# updater = Updater(token=token, workers=32)
# dispatcher = updater.dispatcher
#
#
# updater.dispatcher.add_handler(CommandHandler('hello', hello))
#
# updater.start_polling()
# updater.idle()

bot = telebot.TeleBot(token)
#
#
# # bot = telebot.TeleBot('676472735:AAHq8-RIu0q0fGoZxfNOOPH2Q4HiAn2A9fg')
#
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)


# url = "https://api.telegram.org/bot<token>/"
#
#
# def get_updates_json(request):
#     response = requests.get(request + 'getUpdates')
#     return response.json()


# def last_update(data):
#     results = data['result']
#     total_updates = len(results) - 1
#     return results[total_updates]
#
#
# def get_chat_id(update):
#     chat_id = update['message']['chat']['id']
#     return chat_id
#
#
# def send_mess(chat, text):
#     params = {'chat_id': chat, 'text': text}
#     response = requests.post(url + 'sendMessage', data=params)
#     return response
#
#
# chat_id = get_chat_id(last_update(get_updates_json(url)))
#
# send_mess(chat_id, 'Your message goes here')
#
#
# def main():
#     update_id = last_update(get_updates_json(url))['update_id']
#     while True:
#         if update_id == last_update(get_updates_json(url))['update_id']:
#             send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
#             update_id += 1
#     sleep(1)
#
#
# if __name__ == '__main__':
#     main()

#
# # @bot.message_handler(content_types=["test"])
# # def repeat_all_messages(message):
# #     bot.send_message(message.chat.id, message.text)
# #
# #
# # if __name__ == '__main__':
# #     bot.polling(none_stop=True
# # )
#
#
# # API_TOKEN = '210518930:AAF8a4DK5fgmHsq-GgNDuls_KFrN1C0O5DM'
# #
# # bot = telebot.TeleBot(API_TOKEN)
#
#
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """
# Привет!
# Я тестовый бот, и умею я пока немного. Напиши мне и я отвечу!
# """)
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)



# bot.polling()


# import json
# import requests
# payload = json.dumps({"mac":new_mac,"token":token})
# userloginurl = "http://192.168.1.40:9119/uid"
# r = requests.get(userloginurl, data=payload)
# print(r.url)