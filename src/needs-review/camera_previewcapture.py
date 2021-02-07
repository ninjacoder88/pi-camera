from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/camera/pictures/image.jpg')
sleep(2)
camera.stop_preview()