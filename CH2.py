# Modified by David Garrett
# 3-23-2021
# Test - Chapter 2

print('MPG calculator')
miles_driven = float(input('How many miles did you drive? '))
# Eliminated "miles_driven = int(user_input)" line. user_input variable has no assigned value.
# "input('How many miles did you drive? ')" line is now assigned to miles_driven. Allows the calculation later to work.
# Encompassed input function with the float() function. Converts text value to a numerical value. Also, simplifies the code
# Changed int() to float() function to allow for decimal values
gallons_purchased = float(input('How much gas did you use? '))  # Changed int() to float()
mpg = miles_driven / gallons_purchased  # Changed integer division operator to division operator to allow for values with decimals
# Eliminated "mpg = format(mpg, '2f')" line. Format function added to next line. Simplifies code.
print('You got', format(mpg, '.2f'), 'miles per gallon.')
# Changed the format of mpg from '2f' to '.2f' to format value to two decimal places. '2f' doesn't format the number.
