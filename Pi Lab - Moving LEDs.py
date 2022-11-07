# David Garrett
# EET-107-100 Pi Lab - Moving LED's
# 3-31-2021

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Program flashes LEDs one at a time starting from left to right. Then reverses order from right to left
# Program asks user how long in seconds the LED should flash for before flashing the LEDs

led_pins = [21, 20, 16, 26, 19]


def main():

    try:  # Input Validation Loop
        time_flash = float(input('How long in seconds should the pin flash? '))  # user inputs amount time LED flashes
    except ValueError:
        print('Invalid Input')

    for pin in led_pins:  # Loop executes till all the pin values get passed
        flash_pin(pin, time_flash)  # pin value and amount of time gets passed to flash_pin function

    led_pins.reverse()  # List of pins gets reverse so the program can flash LEDs from right to left

    for pin in led_pins:  # LEDs get flashed like before except in reverse order
        flash_pin(pin, time_flash)


def flash_pin(pin, seconds):  # Sets the pin output to high for a certain amount of time, then low.
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    time.sleep(seconds)
    GPIO.output(pin, False)
    time.sleep(seconds)


main()
