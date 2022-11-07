#David Garrett
#EET-107-100 Chapter 3 Lab 1
#2021-02-08

#Ask user for a numeric value (0-7) and the program outputs the corresponding workday to that value

user_input = int(input('Enter in a numeric value (0-7) of the workday you wish to translate: '))

if user_input == 1:
    print('The workday is Monday')
elif user_input == 2:
    print('The workday is Tuesday')
elif user_input == 3:
    print('The workday is Wednesday')
elif user_input == 4:
    print('The workday is Thursday')
elif user_input == 5:
    print('The workday is Friday')
elif user_input == 0 or user_input == 6 or user_input == 7:
    print('The input is actually a weekend day')
else:
    print('Invalid input')