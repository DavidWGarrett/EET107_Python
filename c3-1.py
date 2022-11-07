# Modified by David Garrett
# 3-23-2021
# Test - Chapter 3

print('What are you?')
age = int(input('Enter your age: '))  # Added a parenthesis to allow function to work

if age >= 20:
    print('You are an adult')
# Removed else statement. Changed if to elif in next statement.
# elif has same functionality as an if statement in an else statement. Simplifies and makes code more readable
elif age > 1 and age < 13:
    # Created another condition (age < 13) that must be true.
    # If the inputted numerical value is between 1 and 13, the print function now outputs "You are a child"
    # The uncorrected code would print "You are a teenager" if age variable is between 1 and 20
    print('You are a child')
elif age >= 13 and age < 20:
    print('You are a teenager')  # Changed "child" to "teenager". Teenagers are ages 13 to 19.
else:
    print('You are an infant')