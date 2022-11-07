# Lab 6.2
# July 23, 2019
# Joe Bob

FILENAME = 'inventory.dat'

def find_item(file):
	# Determine what item they would like to find
	inventory_number_to_find = input('What is the inventory number you would like to locate? ')
	found = False
	inventory_number = file.readline().rstrip('\n')
	while(not found and inventory_number != ''):
		if(inventory_number_to_find == inventory_number):
			found = True
			inventory_description = file.readline().rstrip('\n')
			inventory_price = file.readline().rstrip('\n')
		else:
			file.readline()
			file.readline()
			inventory_number = file.readline().rstrip('\n')	
	if(found):
		print('\nInventory number	  :', int(inventory_number))
		print('Inventory description:', inventory_description)
		print('Inventory price		: $', format(float(inventory_price), '.2f'), sep = '')
	else:
		print('\nInventory item', inventory_number_to_find, 'was not found!')
		
def add_item(file):
	# Get the new data
	inventory_number = input('What is the inventory number? ')
	inventory_description = input('What is the description of the inventory item? ')
	inventory_price = input('What is the price of the inventory item? ')
	# Add the data to the file
	file.write(inventory_number + '\n')
	file.write(inventory_description + '\n')
	file.write(inventory_price + '\n')
	
def read_items(file):
	# Print the header
	print('Current inventory is:\n')
	
	# Priming read
	inventory_number = file.readline().rstrip('\n')
	# Check to see if end of file has been reached
	while(inventory_number != ''):
		inventory_description = file.readline().rstrip('\n')
		inventory_price = file.readline().rstrip('\n')
		# Print
		print('Inventory number     :', int(inventory_number))
		print('Inventory description:', inventory_description)
		print('Inventory price      : $', format(float(inventory_price), '.2f'), sep = '')
		print()
		inventory_number = file.readline().rstrip('\n')

# Find out what the user wants to do
action = \
	input('Do you wish to (l)ist the inventory, (a)dd an item to inventory or (f)ind an item in inventory? ')

# Put the try block around the statement that may generate the exception.
# In this case the if and elif are also included in the try because otherwise
# it makes indenting awkward.
try:	
	# If they want to read the file open it in read mode
	if(action == 'l' or action == 'f'):
		file = open(FILENAME, 'r')
	# If they want to write to the file open it in append mode
	elif(action == 'a'):
		file = open(FILENAME, 'a')
except FileNotFoundError as err:
	print('The file', FILENAME, 'does not exist!')
	exit()

# Find out what they want to do and call the appropriate function
if(action == 'l'):
	read_items(file)
elif(action == 'a'):
	add_item(file)
elif(action == 'f'):
	find_item(file)

# Close the file
file.close()
	