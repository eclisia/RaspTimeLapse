from time import sleep
import picamera

WAIT_TIME = 10

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    for filename in camera.capture_continuous('/home/shares/public/img{timestamp:%H-%M-%S-%f}.jpg'):
        sleep(WAIT_TIME)
