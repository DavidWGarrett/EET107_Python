# David Garrett
# EET-107-100 Pi Lab - Introduction to PWN
# 3-2-2021

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledRed = 21  # Set the red LED to GPIO pin 21

GPIO.setup(ledRed, GPIO.OUT) # Sets GPIO channel as an output
pwmRed = GPIO.PWM(ledRed, 250) # Sets GPIO channel and frequency
pwmRed.start(100) # Default brightness is 100%

print('''This program can be used to alter the brightness of the LED.
Press "e" to exit the program.\n''')

while True:  # Input Validation Loop
    duty = input('Set LED brightness (0 to 100): ')
    if duty == 'e': # Allow user to close the program
        break
    try:
        pwmRed.ChangeDutyCycle(int(duty)) # Sets the brightness of the LED
    except ValueError: # Forces user to input a valid number
        print('Invalid input')

GPIO.cleanup() # Resets all the GPIO settings changed from earlier in the script