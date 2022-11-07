def main():
    file = get_file_to_read()
    pin_time_list = read_lines_from_text_file(file)
    print('bbb')
    updated_pin_time_list = change_time(pin_time_list)
    print('cccc')
    #cycle_lights(updated_pin_time_list)
    print('aaa')



def get_file_to_read():
    import codecs

    while True:
        file_name = input('What is the name of the file you would like to read? ')
        try:
            sample_file_to_read = codecs.open(file_name, "r", "utf-8")
            break
        except FileNotFoundError:
            print('File doesn\'t exist. Try again.')
    return sample_file_to_read


def read_lines_from_text_file(sample_file):
    pin_time_value_list = []

    for line in sample_file:
        pin_number_time_split_list = line.split()

        for num in pin_number_time_split_list:
            no_comma = num.rstrip(',')
            pin_time_value_list.append(no_comma)

    print(pin_time_value_list)

    return pin_time_value_list

def change_time(list):
    while True:  # Input Validation Loop
        try:
            new_time = float(input('How long in seconds should the pin flash? '))
            break
        except ValueError:
            print('Invalid Input')
            continue

    for time_index in range(1, len(list), 2):
        list[time_index] = new_time

    print(list)
    return list

main()