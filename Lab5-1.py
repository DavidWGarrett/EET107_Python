# David Garrett
# EET-107-100 Chapter 5 Lab 1
# 3-2-21

def celsius_to_fahrenheit(celsius_temp):  # Function that converts fahrenheit temp to celsius
    fahrenheit_converted = (celsius_temp*1.8) + 32
    return fahrenheit_converted

def fahrenheit_to_celsius(fahrenheit_temp): #Function that converts celsius temp to fahrenheit
    celsius_converted = (fahrenheit_temp-32)*(5/9)
    return celsius_converted

while True:  # Input validation loop
    try:
        current_temp = int(input('What is the current temperature? ')) # Asks user for current temperature
    except ValueError:
        print('Not a valid input, please try again.\n') # Forces user to input a valid temperature
        continue
    else:
        break

while True:
    temperature_scale = input('Is the temperature in fahrenheit or celsius? Enter f or c. ') # Asks user if temperature is celsius or fahrenheit
    if temperature_scale == 'f' or temperature_scale == 'F': # if state that determines if the user's temperature is in fahrenheit
        new_temp_celcius = fahrenheit_to_celsius(current_temp) # Passes current_temp value to the fahrenheit_to_celsius function and stores value in new_temp_celsius
        print('The temperature from fahrenheit to celsius is ' + str(format(new_temp_celcius, '.2f') + '°C')) # Prints converted temperature
        break
    elif temperature_scale == 'c' or temperature_scale == 'C': # if state that determines if the user's temperature is in celsius
        new_temp_fahrenheit = celsius_to_fahrenheit(current_temp) # Passes current_temp value to the celsius_to_fahrenheit function and stores value in new_temp_fahrenheit
        print('The temperature from celsius to fahrenheit is ' + str(format(new_temp_fahrenheit, '.2f') + '°F')) # Prints converted temperature
        break
    else:
        print('Invalid input\n') #Forces user to input f or c. Restarts the loop.