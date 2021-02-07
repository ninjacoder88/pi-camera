from picamera import PiCamera, Color
import time
import sys

camera = PiCamera()
camera.annotate_text_size = 16
camera.annotate_background = Color("black")
camera.annotate_foreground = Color("white")
#camera.resolution = (576, 324)
camera.resolution = (1152, 648)
#camera.resolution = (1920, 1080)

aCount = 0
while(True):
    try:
        camera.start_preview(fullscreen=True, window=(100, 100, 1152, 648))
        
        count = 0;
        while(count < 3600):
            #localtime = time.localtime(time.time())
            #timestamp = time.asctime(localtime)
            camera.annotate_text = str(aCount)
            time.sleep(1)
            count = count + 1
            aCount = aCount + 1
    except:
        print("an exception occured:", sys.exc_info()[0])
    finally:
        camera.stop_preview()
        time.sleep(5)