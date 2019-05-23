import RPi.GPIO as GPIO
import time

import serial
import os
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
p=GPIO.PWM(21,50)


try:
    while True:
        Rfid='1234'
        print(Rfid)

        if(Rfid=='1234'):
            p.start(2.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
            #Rfid='0'
            #p.stop()
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
