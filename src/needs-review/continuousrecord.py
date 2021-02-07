from picamera import PiCamera, Color
import time
import sys

camera = PiCamera()
camera.annotate_text_size = 32
camera.annotate_background = Color("black")
camera.annotate_foreground = Color("white")
#camera.resolution = (576, 324)
camera.resolution = (1152, 648)
#camera.resolution = (1920, 1080)

#recordtime = 1795 #1 hour - 5 seconds to allow for camera reset
recordtime = 595
aCount = 0
while (1 == 1):
    try:
        localtime = time.localtime(time.time())
        
        filename = time.strftime("%Y%m%d%H%M%S", localtime)
        timestamp = time.asctime(localtime)
        print(timestamp);

        filepath = "/home/pi/camera/video/" + filename + ".h264"
        
        camera.start_preview(fullscreen=False, window=(100,100,1152,648))
        print("start preview")
        camera.start_recording(filepath)
        print("start recording")
        
        #print("Recording started: " + timestamp)
        count = 0
        while(count < recordtime):
            localtime = time.localtime(time.time())
            timestamp = time.asctime(localtime)
            #camera.annotate_text = timestamp
            camera.annotate_text = str(aCount)
            camera.wait_recording(1)
            count = count + 1
            aCount = aCount + 1
    except:
        e = sys.exc_info()[0]
        print(e)
    finally:
        camera.stop_recording()
        print("stop recording")
        camera.stop_preview()
        print("stop preview")
        time.sleep(5)#needed to reset camera