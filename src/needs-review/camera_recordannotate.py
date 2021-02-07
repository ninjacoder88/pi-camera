from picamera import PiCamera, Color
import time

camera = PiCamera()

localtime = time.asctime(time.localtime(time.time()))

camera.annotate_text = localtime
camera.annotate_text_size = 32
camera.annotate_background = Color("black")
camera.annotate_foreground = Color("white")

camera.start_recording("/home/pi/camera/video/video.h264")
time.sleep(10)
camera.stop_recording()