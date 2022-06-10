import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#read switch
channel = 17
GPIO.setup(channel, GPIO.IN)
res = GPIO.input(channel)
print("switch=%1", res)