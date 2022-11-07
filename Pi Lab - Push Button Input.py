# David Garrett
# EET-107-100 Pi Lab - Push Button Input
# 3-10-2021

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buttonPin = 13  # Button connected to GPIO pin #12
# Sets up GPIO pin 12 as an input & sets up internal resistance for push button
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print('Press the button!!!\n')
buttonPressCount = 0  # Accumulator variable set to 0

try:
    while True:
        inputState = GPIO.input(buttonPin)
        if not inputState:  # Detects when button is pushed
            buttonPressCount = buttonPressCount + 1  # Adds 1 to button press count everytime button pressed
            print('Button Pressed!! Press Ctrl+c to exit')
            time.sleep(.4)  # Suspends execution of code so you don't accidentally double press button
except KeyboardInterrupt:  # Option to break out of while loop by pressing Ctrl+c
    print('\nYou are done pressing the button')
    print('You pressed the button ' + str(buttonPressCount) + ' times.')  # Tells user how many button presses

GPIO.cleanup  # Resets the pin inputs/outputs