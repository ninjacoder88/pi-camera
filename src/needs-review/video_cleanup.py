import os
import time
import sys

directoryPath = "/home/pi/camera/video"

while(1 == 1):
    try:
        now = time.time();
        for file in os.listdir(directoryPath):
            #filename = os.fsdecode(file)
            filename = file
    
            filePath = directoryPath + "/" + filename
    
            if(filename.endswith(".h264")):
               stat = os.stat(filePath)
       
               diff = now - stat.st_mtime
               #43200 - 12 hours
               #64800 - 18 hours
               if(diff > 129600):
                   print("removing: " + filename)
                   os.remove(filePath)
           
               #print (filename + " " + str(diff));
            else:
               continue;
        time.sleep(3600)#1 hour
    except:
        e = sys.exc_info()[0]
        print(e)