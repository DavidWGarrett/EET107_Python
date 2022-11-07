# David Garrett
# EET-107-100 Pi Lab - Flashing LEDs with Class
# 4-21-2021

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Led:

    def __init__(self, pin):  #initializer requires a pin value
        self.__ledPin = int(pin)
        self.__state = False

## get and set section with material that needs to be added
    def get_ledPin(self):
        return self.__ledPin

    def set_ledPin(self, pin):
        self.__ledPin = int(pin)

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state


#####################################

    def ledOn(self):  #this turns the LED on
        self.__state = True
        self.__pinState()

    def ledOff(self):  #this turns the LED off
        self.__state = False
        self.__pinState()

    def __pinState(self):
        #this is a private Method to actually set the pin state
        #note the two underscores in front of the name
        #this method is not available outside of the class
        GPIO.setup(self.__ledPin, GPIO.OUT)
        GPIO.output(self.__ledPin, self.__state)

    def ledFlash(self, duration):
        self.ledOn()
        time.sleep(duration)
        self.ledOff()
        time.sleep(duration)

    def cleanup(self):
        GPIO.cleanup()

    def __str__(self):
        return 'The state of the LED is on.' if self.__state else 'The state of the LED is off.'
        # returns a string saying LED is on if self.__state is True or says state is off if self.__state is False




