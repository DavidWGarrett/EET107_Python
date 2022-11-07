# David Garrett
# EET-107-100 Chapter 8 Lab 2
# 4-7-2021

def main():
    import codecs
    sample_file = codecs.open('sample.txt', "r", "utf-8")

    big_list_of_words = []
    individual_word_list = []

    lines_of_words_list_main = read_lines_from_text_file(sample_file)
    #total_word_list = split_lines_into_words(lines_of_words_list_main)
    #total_count = count_words(total_word_list)
    print(lines_of_words_list_main)


def read_lines_from_text_file(sample_file):
    lines_of_words_list = []

    for each_line in sample_file:
        no_white_space_line = each_line.rstrip()
        no_hyphen_line = no_white_space_line.rstrip('–')
        print(no_hyphen_line)
        lines_of_words_list.append(no_hyphen_line)
        print(lines_of_words_list)
        print('dreadlinesfromtextdddddddd')
    return lines_of_words_list


def split_lines_into_words(line_list):
    processed_word_list = []

    for line in line_list:
        unprocessed_word_list = line.split()
        print(unprocessed_word_list)

        for word in unprocessed_word_list:
            print(word)
            print('Hello?')
            processed_word_list.append(word)
            print(processed_word_list)
    print(processed_word_list)
    print('aaaaaaaaaaaaaaa')
    return processed_word_list

def count_words(word_list):
    print('countwordstesttest')
    for word in word_list:
        print(word)
        if word.isalpha:
            print('is alpha testt rue?')
        else:
            print('nottrueisalpha')


def split_lines(individual_word_list):
    for each_word in individual_word_list:
        print(each_word)
        if each_word.isalpha is False:
            individual_word_list.remove(each_word)
            print(individual_word_list)
            print('bbbbbbbbbbb')
        else:
            big_list_of_words.append(each_word)
            print('asfdasdf')
            print(big_list_of_words)
main()