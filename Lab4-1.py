#David Garrett
#EET-107-100 Chapter 4 Lab 1
#2-21-2021

print('Jane\'s Stuff Store\n')

# Ask user to input number of items to purchase
while True:  # Input validation loop
    try:
        number_of_items = int(input('How many items would you like to purchase? '))
    except ValueError: # Condition fails if input is not an integer
        print('Not a valid number')
        continue
    else:
        break
print()

total_price = 0.00  # accumulator variable

# Count-controlled loop with a range based on number of items inputed earlier
# Asks user to input the price of each item

for item in range(1, number_of_items+1):
    while True:  # Input validation loop
        try:
            price = float(input('Enter the price of item ' + str(item) + ': '))
        except ValueError: # Condition fails if input is not an integer
            print('Not a valid price')
        else:
            break
    total_price = total_price + price  # accumulator

# Calculates the average and total cost of each item and prints it out
print('\nThe total cost of your meal is $' + str(format(total_price, ',.2f')))
print('The average cost of each item is $' + str(format(total_price/number_of_items, ',.2f')))