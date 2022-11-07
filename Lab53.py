# David Garrett
# EET-107-100 Chapter 5 Lab 3
# 3-2-2021

def calculate_state_tax(sales_amount, tax_rate):
	return sales_amount * tax_rate  # Removed redundant parentheses
	
def calculate_county_tax(amount, rate):
	return amount * rate  # Changed "taxes =" to return so function has a return value

def TESTTESTT():
    STATE_TAX = .051
    COUNTY_TAX = .024  # Changed from .025 to .024

    print('This program will calculate your taxes!\n')

    sale = float(input('How much is the cost of your purchase? '))
    state_tax = calculate_state_tax(sale, STATE_TAX)  # Created variable state_tax
    county_tax = calculate_county_tax(sale, COUNTY_TAX)  # Switched sale and COUNTY_TAX to match the arguments above
    total_cost = sale + state_tax + county_tax

    print('\nSale amount: $', format(sale, '.2f'), sep = '')
    print('State tax  : $', format(state_tax, '.2f'), sep = '')
    print('County tax : $', format(county_tax, '.2f'), sep = '')
    print('Total cost : $', format(total_cost, '.2f'), sep = '')