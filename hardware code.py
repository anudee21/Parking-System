import RPi.GPIO as GPIO
from firebase import firebase
from datetime import datetime
import time
import serial
import os
import sys

#GPIO connections
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(17,GPIO.IN)

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(4,GPIO.IN)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(18,GPIO.IN)
GPIO.setup(21,GPIO.OUT)
p=GPIO.PWM(21,50)
p.start(5)
p.ChangeDutyCycle(7.5)
time.sleep(5)

#firebase connectivity

firebase=firebase.FirebaseApplication('https://parkandtrack.firebaseio.com/')

while 1:

    slot_status1=firebase.get('/Slots','slot_one')
    slot_status2=firebase.get('/Slots','slot_two')
    slot_status3=firebase.get('/Slots','slot_three')

#slot1     

    if (GPIO.input(17)==False):
        GPIO.output(2,True)
        GPIO.output(3,False)
       

    if (GPIO.input(17)==True):
        GPIO.output(3,True)
        GPIO.output(2,False)
        slot_status1=firebase.put('/Slots','slot_one','False')

#slot2

    if (GPIO.input(4)==False):
        GPIO.output(14,True)
        GPIO.output(15,False)

    if (GPIO.input(4)==True):
        GPIO.output(15,True)
        GPIO.output(14,False)
        slot_status2=firebase.put('/Slots','slot_two','False')


#slot3

    if (GPIO.input(18)==False):
        GPIO.output(22,True)
        GPIO.output(27,False)


    if (GPIO.input(18)==True):
        GPIO.output(27,True)
        GPIO.output(22,False)
        slot_status3=firebase.put('/Slots','slot_three','False')

    
