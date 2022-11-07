# David Garrett
# EET-107-100 Chapter 7 Lab 1
# 3-31-2021

# Program asks user to input the amount of sales for each day of the week. Program then processes that information
# Program will output the total sales, average sales for week, highest sales day/amount, and lowest sales day/amount

def main():
    # List is created for each day of the week
    day_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday')

    amount_list = input_amount_per_day(day_of_the_week)  # User inputs sales for each day into a list
    total_sales = total_all_sales(amount_list)  # Adds up all the sales from the list the user inputted
    average_sales = average_all_sales(total_sales, amount_list)  # Sales inputted by user gets averaged
    max_index_value = find_max_sales_index_value(amount_list)  # Index value of the highest sale gets stored
    min_index_value = find_min_sales_index_value(amount_list)  # Index value of the lowest sale gets stored
    output_sales_info(day_of_the_week, amount_list, total_sales, average_sales, max_index_value, min_index_value)
    # All the values that was inputted and processed gets passed to the output_sales_info function
    # Tells user the total sales, average sales, highest sales day and amount, and lowest sales day and amount

def input_amount_per_day(day_of_the_week):  # Asks users to input sales amount for each day of the week
    input_amount_list = []  # List created for the sales

    for day in day_of_the_week:  # for loop that executes for each day of the week
        while True:  # Input Validation Loop
            try:
                days_amount = float(input('Enter the sales amount for ' + day + ': '))  # User inputs sales amount
            except ValueError:
                print('Invalid Input')
            else:
                input_amount_list.append(days_amount)  # sales gets appended to the list
                break
    return input_amount_list  # List of sales amount gets returned


def total_all_sales(inputs_to_be_totalled):  # Adds all sales together
    accumulated_sales = 0
    for total_weekly_days_amount in inputs_to_be_totalled:  # for loop adds sale to accumalator value till list finishes
        accumulated_sales = accumulated_sales + total_weekly_days_amount
    return accumulated_sales  # returns total sales


def average_all_sales(number_to_average, number_of_inputs):  # Divides the total sales by the number of days (7)
    average_of_all_sales = number_to_average / len(number_of_inputs)
    return average_of_all_sales  # returns the average sales for the week


def find_max_sales_index_value(sales_list):  # Finds the index value on the highest sales day
    max_sales_index_value = sales_list.index(max(sales_list))
    return max_sales_index_value


def find_min_sales_index_value(sales_list):  # Finds the index value on the lowest sales day
    min_sales_index_value = sales_list.index(min(sales_list))
    return min_sales_index_value


def output_sales_info(sales_day, sales_list, accumulated_sales, average_of_all_sales, max_index_value, min_index_value):
    # Tells user the total sales, average sales, highest sales day and amount, and lowest sales day and amount
    print('\nTotal weekly sales: $' + str(format(accumulated_sales, '.2f')))
    print('Average weekly sales: $' + str(format(average_of_all_sales, '.2f')))
    print('The highest sales was $' + str(format(max(sales_list), '.2f')) + ' on day ' + sales_day[max_index_value])
    print('The highest sales was $' + str(format(min(sales_list), '.2f')) + ' on day ' + sales_day[min_index_value])


main()