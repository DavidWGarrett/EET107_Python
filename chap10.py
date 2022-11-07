# David Garrett
# Test question chapter 10
# 5-12-2021

class Pet:  # Changed from def to class to be able to use the methods for the object below
	def __init__(self, n, t, a):
		self.__name = n
		self.__type = t
		self.__age = a
		
	def get_name(self):
		return self.__name
		
	def set_name(self, n):
		self.__name = n
		
	def get_type(self):
		return self.__type
		
	def set_type(self, t):
		self.__type = t
		
	def get_age(self):
		return self.__age
		
	def set_age(self, a):
		self.__age = a  # Changed from "age" to "a" to reference correct variable
		
	def __str__(self):
		return 'name: ' + self.get_name() + '\n' + \
			   'type: ' + self.get_type() + '\n' + \
			   'age : ' + str(self.get_age())
			   
def main():
	the_pet = Pet('none', '?', 0)

	while the_pet.get_name() == 'none' or the_pet.get_type() == '?' or the_pet.get_age() == 0:
		# Program requirement is for the program to exit by itself when all the required changes are made
		# Changed the while loop to repeat till age, type, and name variable is changed

		print('Current pet data\n\n', the_pet, sep='')
		change_type = input('\nWould you like to change the (n)ame, (t)ype, (a)ge or e(x)it? ')
		if change_type.lower() == 'x':
			break  # Changed to break to give user and option to exit the loop
			# removed variable that was being tested by the while loop
		elif change_type.lower() == 'n':
			new_info = input('What is the name of the pet? ')
			the_pet.set_name(new_info)  # Added "the_pet." to the front
			# Line had a method, but no object
		elif change_type.lower() == 't':
			new_info = input('What type of pet is it? ')
			the_pet.set_type(new_info)
		elif change_type.lower() == 'a':
			new_info = int(input('How old is the pet? '))
			the_pet.set_age(new_info)
			
	print('\nFinal pet data\n\n', the_pet, sep='')
			
		
main()
	