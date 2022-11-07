# David Garrett
# EET-107-100 Chapter 8 Lab 2
# 4-7-2021

def main():
    sample_file, name_of_file = get_file_to_read()  # Ask user for file name, open file to read, return file/file name
    lines_of_words_list_main = read_lines_from_text_file(sample_file)  # Puts each line of text from the file into list
    total_word_list = split_lines_into_words(lines_of_words_list_main)
    # Splits each line into individual words and puts into list
    lowercase_word_count, capitalize_word_count = count_words(total_word_list)
    # analyzes and counts lower case and upper case words
    output_message(lowercase_word_count, capitalize_word_count, name_of_file)
    # outputs the file name, total words, and total capitalize words


def get_file_to_read():  # Ask user for file name, open file to read, return file/file nam
    import codecs  # Helps decode text file

    while True:  # loop reiterates till user inputs a file that can be found
        file_name = input('What is the name of the file you would like to read? ')
        try:
            sample_file_to_read = codecs.open(file_name, "r", "utf-8")  # opens file and puts it in read mode
            break
        except FileNotFoundError:  # Forces user to try to input file name again
            print('File doesn\'t exist. Try again.')
    return sample_file_to_read, file_name  # returns file and file name


def read_lines_from_text_file(sample_file):  # Puts each line of text from the file into list
    lines_of_words_list = []  # Initialize list

    for each_line in sample_file:  # for loop puts each line of the poem into list
        no_white_space_line = each_line.rstrip()  # strips each line of whitespace
        no_hyphen_line = no_white_space_line.rstrip('–')  # Strips each line of hyphens
        lines_of_words_list.append(no_hyphen_line)  # Adds stripped lines to a new list
    return lines_of_words_list  # Returns list of lines read from file that are stripped of whitespace and hyphens


def split_lines_into_words(line_list):  # Splits each line into individual words and puts into list
    processed_word_list = []  # Initialize list

    for line in line_list:  # for loop split each line into separate words
        unprocessed_word_list = line.split()

        for word in unprocessed_word_list: # for loop appends each word into a big word list
            alpha_word = ''.join(c for c in word if c.isalpha())
            # creates variable with all non-alphabetic characters replaced with empty strings
            # effectively removes all non-alphabetic characters
            processed_word_list.append(alpha_word)  # appends alphabetic words to new list
    return processed_word_list  # returns list that only has real words


def count_words(word_list):  # analyzes and counts lower case and upper case words
    lower_count = 0
    higher_count = 0
    # Initialize the lower and higher count

    for word in word_list:  # for loop iterates over each word in list
        while word.isalpha():  # Only enters loop if the word contains only alphabetic characters
            if not word.islower():
                higher_count += 1  # Adds one to upper case count if word is upper case
            else:
                lower_count += 1  # Adds one to lower case count if word is lower case
            break
    return lower_count, higher_count  # Returns the amount of upper case and lower case words


def output_message(low_count, high_count, file_name):  # outputs the file name, total words, and total capitalize words
    print('The file ' + file_name + ' contains ' + str(low_count+high_count) + ' words of which ' +
          str(high_count) + ' of them are capitalized')


main()