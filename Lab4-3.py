#David Garrett
#EET-107-001 Chapter 4 Lab 3
#2-23-2021

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledRed = 21
redState = False

ledYellow = 20
yellowState = False

ledGreen = 16
greenState = False


lightString = input('What light do you want to toggle?')

if lightString == 'r':
    GPIO.setup(ledRed, GPIO.OUT)
    GPIO.output(ledRed, redState)
elif lightString == 'y':
    GPIO.setup(ledYellow, GPIO.OUT)
    GPIO.output(ledYellow, yellowState)
elif lightString == 'g':
    GPIO.setup(ledGreen, GPIO.OUT)
    GPIO.output(ledGreen, greenState)
else:
    print('Invalid input')