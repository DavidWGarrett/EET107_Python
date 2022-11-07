# David Garrett
# EET-107-100 Chapter 8 Lab 2
# 4-7-2021

sample_file = open('sample.txt', 'r')

big_list_of_words = []
line_of_words_list = []


def main():
    for line in sample_file:
        line_of_words_list.append(line)
        print(line_of_words_list)
        print('ddddddddd')
        for word in line_of_words_list:
            individual_word_list = word.split()
            print('aaaaaaaaaaaaaaa')
            split_lines(individual_word_list)


def split_lines(individual_word_list):
    for each_word in individual_word_list:
        if each_word.isalpha is False:
            individual_word_list.remove(each_word)
            print(individual_word_list)
            print('bbbbbbbbbbb')
        else:
            big_list_of_words.append(each_word)
            print('asfdasdf')
main()

sample_file.close()