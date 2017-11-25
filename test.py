from time import sleep
import config,telebot,json
from telebot import types

bot = telebot.TeleBot(config.token)
users=[202226598, 56345999]

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        bot.send_message(chat_id=202226598, "кто-то пришел")
        time.sleep(0.2)

if __name__ == '__main__':
    bot.polling(none_stop=True)
