# David Garrett
# EET-107-100 Pi Lab - Introduction to Interrupts
# 4-14-2021

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def main():
    file = get_file_to_read()  # asks user for
    pin_time_list = read_lines_from_text_file(file)  # reads each line, splits line, and appends to a new list
    updated_pin_time_list = change_time(pin_time_list)  # asks user for a new time
    cycle_lights(updated_pin_time_list)
    # Goes through list and flashes pin for a certain amount of time
    # Sets the pin output to high for a certain amount of time, then low.



def get_file_to_read():  # Ask user for file name, open file to read, return file
    import codecs  # Helps decode text file

    while True:  # loop reiterates till user inputs a file that can be found
        file_name = input('What is the name of the file you would like to read? ')  # asks user for name of file
        try:
            sample_file_to_read = codecs.open(file_name, "r", "utf-8")  # opens file and puts it in read mode
            break
        except FileNotFoundError:  # Forces user to try to input file name again
            print('File doesn\'t exist. Try again.')
    return sample_file_to_read  # return file that is in read mode


def read_lines_from_text_file(sample_file):  # reads each line, splits line, and appends to a new list
    pin_time_value_list = []  # Initialize list

    for line in sample_file:  # for loop that splits each line and puts into list
        pin_number_time_split_list = line.split()

        for num in pin_number_time_split_list:
            no_comma = num.rstrip(',')  # removes any commas
            pin_time_value_list.append(no_comma)  # puts all characters into big list

    return pin_time_value_list  # returns a list that has a certain GPIO pin in even indexes, times in odd indexes


def change_time(list):  # asks user if he or she wants to change amount of time pin flashes
    while True:  # Input Validation Loop
        try:
            new_time = float(input('How long in seconds should the pin flash? '))
            break
        except ValueError:
            print('Invalid Input')
            continue

    for time_index in range(1, len(list), 2):  # for loop replaces previous times with the user's new time
        list[time_index] = new_time

    return list  # returns a list that has a certain GPIO pin in even indexes, times in odd indexes


def flash_pin(pin, seconds):  # Sets the pin output to high for a certain amount of time, then low.
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    time.sleep(seconds)
    GPIO.output(pin, False)
    time.sleep(seconds)


def cycle_lights(pattern):  # Goes through list and flashes pin for a certain amount of time
    for i in range(0, len(pattern), 2):  # for loop that iterates over the entire span of list with step value of 2
        flash_pin(int(pattern[i]), float(pattern[i+1]))  # passes even value indexes as GPIO pin values
        # passes odd value indexes as times that pins flash


main()
