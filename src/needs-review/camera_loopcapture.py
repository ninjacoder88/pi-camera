from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
    sleep(5)
    location = "/home/pi/camera/pictures/image" + str(i) + ".jpg"
    camera.capture(location)
camera.stop_preview()