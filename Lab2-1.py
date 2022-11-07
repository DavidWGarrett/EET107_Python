#David Garrett
#EET-107-100 Chapter 2 Lab 1
#2021-02-01

#Program asks for first name, last name, and number of marbles to purchase
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
number_of_marbles = int(input('How many marbles would you like to purchase? '))

#Figure out total cost of marbles
cost_of_marble = 1.27
total_cost = number_of_marbles*cost_of_marble

#Print out an invoice
print('\nThank you for your purchase, ' + first_name + ' ' + last_name + \
'.\nYou have purchased ' + str(number_of_marbles) + ' marbles at a price of $' + \
str(cost_of_marble) + ' each for a total of $' + "{:.2f}".format(total_cost) + '.')