import os
import time

directoryPath = "/home/pi/camera/pictures"

while(1 == 1):
    now = time.time();
    for file in os.listdir(directoryPath):
        #filename = os.fsdecode(file)
        filename = file
    
        filePath = directoryPath + "/" + filename
    
        if(filename.endswith(".jpg")):
           stat = os.stat(filePath)
       
           diff = now - stat.st_mtime
           #43200 - 12 hours
           #64800 - 18 hours
           if(diff > 43200):
               print("removing: " + filename)
               os.remove(filePath)
           
           #print (filename + " " + str(diff));
        else:
           continue;
    time.sleep(3600)