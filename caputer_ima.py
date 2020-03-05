import picamera

with picamera.PiCamera() as camera:
    #camera.resolution = (1280,720)
    camera.capture("/home/pi/Desktop/uv.png")
print("picture taken")
