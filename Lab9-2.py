# David Garrett
# EET-107-100 Chapter 9 Lab 2
# 4-14-21

def main():
    sample_file, file_name = get_file_to_read()  # Ask user for file name, open file to read, return file/file name
    lines_of_words_list_main = read_lines_from_text_file(sample_file)  # Puts each line of text from the file into list
    unique_word_set = split_lines_into_words(lines_of_words_list_main)
    # splits lines into words and puts unique words into a set
    output_message(unique_word_set, file_name)  # outputs name of file name and number of unique words
    sample_file.close()


def get_file_to_read():  # Ask user for file name, open file to read, return file/file name
    import codecs  # Helps decode text file
    import sys  # For sys.exit function

    while True:  # loop reiterates till user inputs a file that can be found
        file_name = input('What is the name of the file you would like to read? Or type "exit" to close program. ')
        try:
            sample_file_to_read = codecs.open(file_name, "r", "utf-8")  # opens file and puts it in read mode
            break
        except FileNotFoundError:  # Forces user to try to input file name again or exit
            if file_name.lower() == 'exit':
                sys.exit()
            else:
                print('File doesn\'t exist. Try again.')
    return sample_file_to_read, file_name  # returns file and file name


def read_lines_from_text_file(sample_file):  # Puts each line of text from the file into list
    lines_of_words_list = []  # Initialize list

    for each_line in sample_file:  # for loop puts each line of the txt file into list
        no_white_space_line = each_line.strip()  # strips each line of whitespace
        no_hyphen_line = no_white_space_line.rstrip('–')  # Strips each line of hyphens
        lines_of_words_list.append(no_hyphen_line)  # Adds stripped lines to a new list
    return lines_of_words_list  # Returns list of lines read from file that are stripped of whitespace and hyphens


def split_lines_into_words(line_list):  # Splits each line into individual words and puts into a set
    unique_word_set = set()  # Initialize set

    for line in line_list:  # for loop split each line into separate words
        unprocessed_word_list = line.split()

        for word in unprocessed_word_list:  # for loop processes each string. Removes periods, commas from end of words.
            if not word[int(len(word))-1].isalpha():  # if last character of string is not an alphabet character
                word = ''.join(c for c in word if (c.isalnum()  # removes non alphabet characters excluding "-" and "'"
                               or c == '\''
                               or c == '-'))

            acceptable_chara_string = 'abcdefghijklmnopqrstuvwxyz-\''  # only characters that form words
            skip_word = False  # Initialize skip_word variable that'll skip a string that contains non-word characters
            acceptable_chara_verification = 0
            # Counter variable used to compare length of string and acceptable characters

            for acceptable_chara in acceptable_chara_string:
                # loop that compares acceptable characters to the word string
                for chara in word:
                    if acceptable_chara.lower() == chara.lower():
                        acceptable_chara_verification += 1  # counter adds 1 if character is acceptable
            if acceptable_chara_verification != int(len(word)):
                # sets the skip_word value to true if word variable contains unacceptable characters
                skip_word = True
            if (word.isalpha() == True or "'" in word[1:int(len(word))-1] or "-" in word[1:int(len(word))-1]) \
                    and skip_word is not True:  # words have to contain letters or "'" or "-"
                unique_word_set.add(word.lower())  # adds lower case unique word to a set
    return unique_word_set  # returns set that only has unique words


def output_message(word_set, file_name):  # outputs message with the number of unique words and file name
    print('There are ' + str(len(word_set)) + ' unique words in ' + str(file_name) +
          ' .\n\nThanks for using the program!')


main()


