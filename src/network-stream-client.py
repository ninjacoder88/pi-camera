import socket
import time
import picamera

client_socket = socket.socket()
client_socket.connect(("172.16.10.14", 8000))

connection = client_socket.makefile("wb")
try:
    camera = picamera.PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 24
    
    camera.start_preview()
    time.sleep(2)
    
    camera.start_recording(connection, format="h264")
    camera.wait_recording(60)
    camera.stop_recording()
finally:
    connection.close()
    client_socket.close()

