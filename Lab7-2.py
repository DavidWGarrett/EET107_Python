# David Garrett
# EET-107-100 Chapter 7 Lab 2
# 3-31-2021

import time

# Program determines the speed of player one and two's clicks and declares the player with two fastest clicks the winner


def main():
    time_list_p1 = input_number_player_one()  # creates list of player one's click speeds
    time_list_p2 = input_number_player_two()  # creates list of player two's click speeds
    compare_list = compare_type_speed(time_list_p1, time_list_p2)  # list that compares speeds of the two players clicks
    display_winner(compare_list)  # Processes the list and determines the winner of each click race and overall winner
    turtle_race(compare_list)  # turtle race that moves the players turtles twice as much if user has a faster click


def input_number_player_one():  # player one is asked to input a number, speed of click gets recorded and stored in list
    time_list_player_one = []  # player one's click speed list is initialized
    for a in range(3):  # for loop that ask user to click three times
        while True:  # Input validation loop
            try:
                start_time = time.time()  # timer starts
                number_inputted = int(input('Type in a number: '))
                end_time = time.time()  # timer ends
                time_list_player_one.append(end_time - start_time)
                print('It took', (end_time - start_time), 'seconds for you to type anykey')
            except ValueError:
                print('Invalid Input')
            else:
                break
    return time_list_player_one  # click speed list is returned


def input_number_player_two():  # player two is asked to input a number, speed of click gets recorded and stored in list
    time_list_player_two = []  # player one's click speed list is initialized
    for a in range(3):  # for loop that ask user to click three times
        while True:  # Input validation loop
            try:
                start_time = time.time()  # timer starts
                number_inputted = int(input('Type in a number: '))
                end_time = time.time()  # timer ends
                time_list_player_two.append(end_time - start_time)
                print('It took', (end_time - start_time), 'seconds for you to type anykey')
                print(time_list_player_two)
            except ValueError:
                print('Invalid Input')
            else:
                break
    return time_list_player_two


def compare_type_speed(time_list_player_one, time_list_player_two):  # compares click speeds of player one and two
    comparison_time_list = []  # list that stores values comparing the click speeds of the players
    # if player one is faster, value that is stored is 1
    # if player two is faster, value that is stored is 0
    for time_list_index_value in range(3):
        if time_list_player_one[0+time_list_index_value] < time_list_player_two[0+time_list_index_value]:
            aa = 1
            comparison_time_list.append(aa)
        else:
            aa = 0
            comparison_time_list.append(aa)
    return comparison_time_list


def display_winner(comparison_time_list):
    for comparison_index_value in range(3):  # Loop that prints out the winner of each click race
        if comparison_time_list[comparison_index_value] == 1:
            print('Player One #' + str(comparison_index_value + 1) + ' click is faster')
        else:
            print('Player Two #' + str(comparison_index_value + 1) + ' click is faster')

    total_value = 0

    for value_for_each_click in comparison_time_list:  # Adds up all the values from the comparison list
        total_value = total_value + value_for_each_click

    # If the comparison list values add up higher than 1, player 1 is winner. If lower than 1, player two is winner

    if total_value > 1:
        print('Player One is the winner!')
    else:
        print('Player Two is the winner!')


def turtle_race(comparison_time_list):  # Two turtles race. Player with the faster clicks makes their turtle go further.
    import turtle

    # Turtles get set up for race

    turtle_1 = turtle.Turtle()
    turtle_2 = turtle.Turtle()

    turtle_1.speed(1)
    turtle_2.speed(1)
    turtle_2.up()
    turtle_2.setpos(0, -50)
    turtle_2.down()

    for gggg in comparison_time_list:  # Determines the winner of each race. Winner moves 50 spaces, loses 25 spaces
        if comparison_time_list[0+gggg] == 1:
            turtle_1.fd(50)
            turtle_2.fd(25)
        else:
            turtle_1.fd(25)
            turtle_2.fd(50)

    turtle.exitonclick()


main()
