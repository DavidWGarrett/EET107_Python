import time


def main():
    time_list_p1 = input_number_player_one()
    time_list_p2 = input_number_player_two()
    compare_list = compare_type_speed(time_list_p1, time_list_p2)
    display_winner(compare_list)
    turtle_race(compare_list)


def test():
    start_time = time.time()
    input('Type anykey')
    end_time = time.time()
    print('It took', (end_time - start_time), 'seconds for you to type anykey')


def input_number_player_one():
    time_list_player_one = []
    for a in range(3):
        while True:
            try:
                start_time = time.time()
                number_inputted = int(input('Type in a number: '))
                end_time = time.time()
                time_list_player_one.append(end_time - start_time)
                print('It took', (end_time - start_time), 'seconds for you to type anykey')
                print(time_list_player_one)
            except ValueError:
                print('Invalid Input')
            else:
                break
    return time_list_player_one


def input_number_player_two():
    time_list_player_two = []
    for a in range(3):
        while True:
            try:
                start_time = time.time()
                number_inputted = int(input('Type in a number: '))
                end_time = time.time()
                time_list_player_two.append(end_time - start_time)
                print('It took', (end_time - start_time), 'seconds for you to type anykey')
                print(time_list_player_two)
            except ValueError:
                print('Invalid Input')
            else:
                break
    return time_list_player_two


def compare_type_speed(time_list_player_one, time_list_player_two):
    comparison_time_list = []
    for cc in range(3):
        if time_list_player_one[0+cc] < time_list_player_two[0+cc]:
            aa = 1
            comparison_time_list.append(aa)
        else:
            aa = 0
            comparison_time_list.append(aa)
    print(comparison_time_list)
    return comparison_time_list


def display_winner(comparison_time_list):
    for rrrr in range(3):
        if comparison_time_list[rrrr] == 1:
            print('Player One #' + str(rrrr+1) + ' click is faster')
        else:
            print('Player Two #' + str(rrrr+1) + ' click is faster')

    total_value = 0

    for tttt in comparison_time_list:
        total_value = total_value + tttt

    if total_value > 1:
        print('Player One is the winner!')
    else:
        print('Player Two is the winner!')


def turtle_race(comparison_time_list):
    import turtle

    turtle_1 = turtle.Turtle()
    turtle_2 = turtle.Turtle()

    turtle_1.speed(1)
    turtle_2.speed(1)
    turtle_2.up()
    turtle_2.setpos(0, -50)
    turtle_2.down()

    for gggg in comparison_time_list:
        if comparison_time_list[0+gggg] == 2:
            turtle_1.fd(50)
            turtle_2.fd(25)
        else:
            turtle_1.fd(25)
            turtle_2.fd(50)


    turtle.exitonclick()

main()