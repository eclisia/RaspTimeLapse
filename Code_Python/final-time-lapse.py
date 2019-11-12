#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
from time import sleep
import picamera

WAIT_TIME = 10

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    for filename in camera.capture_continuous('/home/shares/public/img{timestamp:%Y%m%d-%H%M%S-%f}.jpg'):
        sleep(WAIT_TIME)
