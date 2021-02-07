from picamera import PiCamera, Color
import time

camera = PiCamera()

camera.annotate_text_size = 32
camera.annotate_background = Color("black")
camera.annotate_foreground = Color("white")
camera.resolution = (576, 324)

while (1 == 1):
    try:
        localtime = time.localtime(time.time())
        timestamp = time.asctime(localtime)
        filename = time.strftime("%Y%m%d%H%M%S", localtime)
    
        camera.annotate_text = timestamp
        location = "/home/pi/camera/pictures/" + filename + ".jpg"
        print(location);
        camera.capture(location)
        time.sleep(5)
    except:
        print("an exception occurred")