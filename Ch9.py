# David Garrett
# Test question chapter 9
# 5-12-2021

print('Word Count Program\n')

# Create the dictionary
individual_word_count = {}
filename = input('Enter the name of the file you wish to process: ')

try:
    file = open(filename, 'r')
except FileNotFoundError as err:
    print('The file', filename, 'does not exist!')
    exit()


#####################
# The original code only read the first line of the file. Now it can read all the lines of the file

lines_of_words_list = []  # Initialize list

for each_line in file:
    no_white_space_line = each_line.strip()  # strips each line of whitespace
    lines_of_words_list.append(no_white_space_line)  # Adds each line of the file to a list

file.close()

word_list = []  # List of all unique words

for each_line in lines_of_words_list:  # Splits the lines to individual words
    split_line_list = each_line.split()
    for word in split_line_list:
        word_list.append(word)
######################

#######################################
# Created new code to deal with situations where strings had periods or letters were capitalized
word_list_without_capitalization_and_periods = []

for word in word_list:
    word = word.lower()
    # Lower cases all words so words appear unique even if the letters have different capitalization
    word = ''.join(c for c in word if c.isalnum() or c == "'")
    # Remove all non-alphabetic characters besides apostrophes
    # There was a situation where "unique." was presented as a unique word even though it had a period
    word_list_without_capitalization_and_periods.append(word)
#######################################


# Put all words in a set to remove the duplicates
unique_words = set(word_list_without_capitalization_and_periods)
# Create a dictionary of each unique word
# where the initial count is 0 {'unique word':count}
for word in unique_words:
    individual_word_count[word] = 0

# Add one to the counter for each word found
for word in word_list_without_capitalization_and_periods:
    individual_word_count[word] += 1  # Changed from "= individual_word_count[word] + 22" to "+= 1"
    # Original code would add 22 to key value for each occurrences. Now only adds 1

# Print the results 
print()
print(format('Unique Word', '20'), format('Number of Occurrences', '20'))
print('========================================')
for key in individual_word_count:
    # Get the value of the key
    num_occurences = individual_word_count[key]  # Changed from "key" to "individual_word_count[key]"
    # num_occurences now references the number value associated with the key rather than the key itself
    print(format(key, '20'), format(str(num_occurences), '20'))
