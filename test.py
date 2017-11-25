from time import sleep
import config,telebot,json
from telebot import types
import RPi.GPIO as GPIO

bot = telebot.TeleBot(config.token)
users=[202226598, 56345999]
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        bot.send_message(202226598, "кто-то пришел")
        time.sleep(0.2)

if __name__ == '__main__':
    bot.polling(none_stop=True)
