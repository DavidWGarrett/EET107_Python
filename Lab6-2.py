# David Garrett
# EET-107-100 Chapter 6 Lab 2
# 3-10-2021

FILENAME = 'inventory.dat'

def find_item(file):
	# Determine what item they would like to find
    found = False
    while found == False:
        # Ask for name of item or number
        inventory_number_or_name = input('Do you wish to find item by (i)nventory number or by item (n)ame? ')
        if inventory_number_or_name == 'i':  # Finding item by inventory number
            inventory_number_to_find = input('What is the inventory number you would like to locate? ')
            inventory_number = file.readline().rstrip('\n')
            while(not found and inventory_number != ''):
                if(inventory_number_to_find == inventory_number):  # Searches text file for matching inventory number
                    found = True  # Breaks While Loop when program finds a search
                    inventory_description = file.readline().rstrip('\n') # Sets inventory name/description
                    inventory_price = file.readline().rstrip('\n')  # Sets inventory price
                else:
                    file.readline()  # Skips Line
                    file.readline()  # Skips Line
                    inventory_number = file.readline().rstrip('\n')	  # Sets new inventory number
            if(found):
                print('\nInventory number	  :', int(inventory_number))
                print('Inventory description:', inventory_description)
                print('Inventory price		: $', format(float(inventory_price), '.2f'), sep = '')
            else:
                print('\nInventory item', inventory_number_to_find, 'was not found!')
        elif inventory_number_or_name == 'n':  # Find item based on name/description
            inventory_name_to_find = input('What is the name of the item you would like to locate? ')
            inventory_number = file.readline().rstrip('\n')  # Sets inventory number
            inventory_description = file.readline().rstrip('\n')  # Sets inventory name/description
            while(not found and inventory_description != ''):  # While Loop
                if(inventory_name_to_find == inventory_description):  # Searches text file for matching name/description
                    found = True  # Breaks While Loop when program finds a search
                    inventory_price = file.readline().rstrip('\n')  # Sets inventory price
                else:
                    file.readline()  # Skips Line
                    inventory_number = file.readline().rstrip('\n')  # Sets New Inventory Number
                    inventory_description = file.readline().rstrip('\n')  # Sets New name/description to check
            if(found):
                print('\nInventory number	  :', int(inventory_number))
                print('Inventory description:', inventory_description)
                print('Inventory price		: $', format(float(inventory_price), '.2f'), sep = '')
            else:
                print('\nInventory item', inventory_name_to_find, 'was not found!')
                file.seek(0)
        else:
            print('Invalid Input')
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
	