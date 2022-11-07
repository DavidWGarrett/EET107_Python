#David Garrett
#EET-107-100 Chapter 4 Lab 3
#2-23-2021

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# Assigns each LED to a certain GPIO pin

GPIO.setmode(GPIO.BCM)

ledRed = 21
redState = False

ledYellow = 20
yellowState = False

ledGreen = 16
greenState = False

# Asks user which light to toggle or exit program.

while True:
    lightString = input('What light do you want to toggle?(r, y, or g) or press e for exit ')
    if lightString == 'r':
        GPIO.setup(ledRed, GPIO.OUT)
        redState = not(redState)
        GPIO.output(ledRed, redState)
    elif lightString == 'y':
        GPIO.setup(ledYellow, GPIO.OUT)
        yellowState = not(yellowState)
        GPIO.output(ledYellow, yellowState)
    elif lightString == 'g':
        GPIO.setup(ledGreen, GPIO.OUT)
        greenState = not(greenState)
        GPIO.output(ledGreen, greenState)
    elif lightString == 'e':
        exit()
    else:
        print('Invalid input')