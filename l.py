from picamera import PiCamera
from time import sleep
import config,telebot,json
from telebot import types

camera = PiCamera()
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["photo"])
def send_photo(message):
    camera.start_preview()
    sleep(2)
    camera.capture('./image.jpg')
    camera.stop_preview()
    bot.send_photo(chat_id=message.chat.id, photo=open('./image.jpg', 'rb'))

if __name__ == '__main__':
    bot.polling(none_stop=True)
