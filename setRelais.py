import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#set Relais
channel = 22
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, 1)
time.sleep(1)
GPIO.output(channel, 0)