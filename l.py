from picamera import PiCamera
from time import sleep
 
camera = PiCamera()
 
# Запускаем предпросмотр сигнала с камеры на экране поверх всех окон
camera.start_preview()
 
# Даём камере три секунды на автофокусировку и установку баланса белого
sleep(30)
 
# Делаем снимок и сохраняем его на рабочий стол с именем image.jpg
camera.capture('/home/pi/Desktop/image.jpg')
 
# Выключаем режим предпросмотра
camera.stop_preview()
