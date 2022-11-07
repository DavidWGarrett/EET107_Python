# David Garrett
# Test Question Chapter 7
# 5-12-2021

print('Joe\'s Number Analysis Program.')

total = 0


go_on = 'Y'
numbers = []  # Initialized a list called numbers (with an s)
# Initialized List kept outside loop so it doesn't get converted back into an empty list

while go_on.upper() == 'Y':
	number = float(input('\nEnter a number: '))  # Changed to float so user can user numbers with decimals

	numbers.append(number)  # Change from "numbers = append(number)" to "numbers.append(number)"
	print(numbers)
	# Now there's a list and the user's input will be appended to that list
	total += number
	go_on = input('Do you have more numbers to enter? Enter "Y" if you do or enter anything else to exit. ')
	# Added more information to the input. User is now told to press "Y" if he or she wants to add more numbers
	
min_number = min(numbers)
max_number = max(numbers)
numbers_entered = len(numbers)
average = total / numbers_entered

print('\nYou entered the values', numbers)
print('A total of', numbers_entered, 'values were entered')
print('The maximum value entered was', max_number)
print('The minimum value entered was', min_number)
print('The average value entered was', format(average, '.2f'))
# Program Requirement didn't specify if average value should be added
print('The total of all values entered was', total)