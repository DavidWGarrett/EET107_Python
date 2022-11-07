# David Garrett
# EET-107-001 Chapter 5 Lab 1
# 3-2-21

def celcius_to_fahrenheit(current_temp):
    celcius_converted = (current_temp - 32) * (5/9)
    print(format(celcius_converted, '.2f')

def fahrenheit_to_celcius(current_temp):
    fahrenheit_converted = (current_temp*1.8) + 32
    print(format(fahrenheit_converted, '.2f'))


#fahrenheit = int(input('What is the temperature? '))
#celcius = (fahrenheit - 32) * (5/9)
#print(format(celcius, '.2f'))

while True:  # Input validation loop
    try:
        current_temp = int(input('What is the current temperature? '))
    except ValueError:
        print('Not a valid input, please try again.')
        continue
    else:
        break

while True:
    c_or_f = input('Is the temperature in fahrenheit or celcius? Enter f or c. ')
    if c_or_f == 'f':
        celcius_to_fahrenheit(current_temp)
    elif c_or_f == 'c':
        fahrenheit_to_celcius(current_temp)
    else:
        print('Invalid input')