from picamera import PiCamera
from time import sleep
import config,telebot,json
from telebot import types

camera = PiCamera()
camera.vflip = True
camera.hflip = True
bot = telebot.TeleBot(config.token)
users=[202226598, 56345999]

@bot.message_handler(commands=["photo"])
def send_photo(message):
    if message.chat.id in users:
        camera.start_preview()
        sleep(5)
        camera.capture('./image.jpg')
        camera.stop_preview()
        bot.send_photo(chat_id=message.chat.id, photo=open('./image.jpg', 'rb'))
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "чтобы получить фото с домофона, нажми /photo")
    print(message.chat.id)

while True:
    print(1)

if __name__ == '__main__':
    bot.polling(none_stop=True)
