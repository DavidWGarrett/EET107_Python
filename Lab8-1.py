# David Garrett
# EET-107-100 Chapter 8 Lab 1
# 4-7-2021

def main():
    users_name = ask_for_name()  # asks user for name
    corrected_name_order_list = correct_order_name(users_name)
    # Processes the user's input and returns a list with first name as index value 0 and last, index value 1
    correct_capitalization_list = process_name(corrected_name_order_list)
    # Capitalize the first letter of each name and lowercase the rest of the letters
    output_message(correct_capitalization_list)
    # output name if the format of last name, first name


def ask_for_name(): # asks user for name and returns it
    name = input('Please enter your first and last name. ')
    return name


def correct_order_name(name):  # puts user's name into a list where first name is index value 0 and last, index value 1
    name_list = []
    while len(name_list) < 2:  # Loop can't break unless there's at least two strings
        if ', ' not in name:  # If user inputs there name in "firstname lastname" format.
            processing_name = name.split()  # splits strings with spaces into separate strings
            try:
                name_list = [processing_name[0], processing_name[1]]  # Saves first two strings into list
            except IndexError:  # Forces user to input at least two separate names
                print('Invalid Input')
                name = ask_for_name()
        else:
            processing_name = name.split(', ')  # If user inputs there name in "lastname, firstname" format.
            try:
                name_list = [processing_name[1], processing_name[0]]
                if name_list[0].find(' ') > 0:  # If first name has a space and extra characters
                    name_without_extra_chara = name_list[0].split()
                    name_list[0] = name_without_extra_chara[0]  # removes extra characters from first name
                elif name_list[0].find(',') > 0:  # If first name has a comma and extra characters
                    name_without_extra_chara = name_list[0].split(',')
                    name_list[0] = name_without_extra_chara[0]  # removes extra characters from first name
                else:
                    break

            except IndexError:  # Forces user to input at least two separate names
                print('Invalid Input')
                name = ask_for_name()

    return name_list


def process_name(name_list):  # Capitalize the first letter of each name and lowercase the rest of the letters
    lower_cased_name_list = []
    correct_case_name_list = []
    # Initialize two lists

    for name in name_list:  # for loop that processes each name
        lower_cased_name_list.append(name.lower())  # Lower case all characters for each name

    for lower_name in lower_cased_name_list:  # for loop that processes each name
        first_character = lower_name[0]  # Stores first character
        correct_case_name = first_character.upper() + lower_name[1:]
        # concatenate first uppercase letter with the rest of the lowercase letters of each name
        correct_case_name_list.append(correct_case_name)  # names with correct case of each letter added to a new list

    return correct_case_name_list  # return list with names with correct case of each letter


def output_message(name_list):  # output name if the format of last name, first name
    print(name_list[1] + ', ' + name_list[0])


main()