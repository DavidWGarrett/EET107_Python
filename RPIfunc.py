import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def redLed21brightness()
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
        except ValueError: #
            print('Invalid input')

    GPIO.cleanup()

def ledLightToggle():
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