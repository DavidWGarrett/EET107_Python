# David Garrett
# EET-107-100 Pi Lab - Introduction to Interrupts
# 4-14-2021

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def main():
    pins = {'button1': 13, 'led_red':21, 'led_yellow':20}  # Dictionary for correspond LEDs and button to pin number
    stateFlashing = True

    GPIO.setup(pins['button1'], GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sets up button, adds pullup resistor to avoid short circuit
    
    GPIO.add_event_detect(pins['button1'], GPIO.FALLING, callback=buttonPressed, bouncetime=300)
    
    buttonPressed(pins['button1'])
    

    while True:
        if stateFlashing == True: # if button isn't pressed
            print(stateFlashing)
            buttonPressed(pins['button1'])
            for LEDs in pins: # for loop cycles through both LEDs if button isn't pressed
                if 'led' in LEDs:
                    setPin(pins[LEDs], True)
                    time.sleep(.2)
                    setPin(pins[LEDs], False)
                    time.sleep(.2)
        if stateFlashing == False:
            for pin_num in pin:
                setPin(pins[pin_num], False)

def buttonPressed(channel):  # Stops the LEDs from flashing if button is pressed
    global stateFlashing
    print('helllo')
    stateFlashing = False


def setPin(pin, state):  # passes pin value and sets it up as an output and sets its state
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, state)


main()
