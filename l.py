from picamera import PiCamera
from time import sleep
import config,telebot,json
from telebot import types

camera = PiCamera()
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["photo"])
def send_photo(message):
    camera.start_preview()
    time.sleep(2)
    camera.capture('./image.jpg')
    camera.stop_preview()
    bot.send_message(chat_id=chat_id,
                     text='<b>bold</b> <i>italic</i> Отправляю.',
                     parse_mode=telegram.ParseMode.HTML)

if __name__ == '__main__':
    bot.polling(none_stop=True)
