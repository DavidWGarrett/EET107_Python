# David Garrett
# EET-107-100 Chapter 12 Lab 1
# 4-28-2021

# Use a recursive loop to repeat a string a certain amount of times

def main():

    string = input('What string would you like to repeat? ')  # Asks user to input string

    while True:  # Input Validation Loop
        try:
            amount = int(input('How many times would you like to repeat "' + string + '?" '))
            # Asks user the amount of times to repeat character
            break
        except ValueError:
            print('Invalid Input\n')

    print('\n' + factorial_alt(amount, string))  # Prints string with string repeated the specified amount of times

def factorial_alt(n, chara):

    if n == 0: # when n = 0, the recursive loop stops
        # if statement processes information from recursive loop
        # outputs user's string repeated the specified amount of time
        chara_length = len(chara)

        while chara_length % (n+1) == 0:  # figures out how many recursive loops there were
            # does an inverse factorial, starts dividing by one, then two, ect. and sees if there's a remainder
            # when finally there's a remainder, loop stops
            # n = amount of recursive loops
            # chara_length = the original length of the user's string
            chara_length = chara_length / (n+1)
            n += 1

        chara_length = chara_length * n  # multiplication figures out how long the new repeated string should be
        chara = chara[0 : int(chara_length)]
        # removes any extra characters trailing on the string

        return chara

    else:  # Else condition used to create the recursive loop
        chara = chara * n  # Multiplies user's inputted string with the amount the user wants to multiply string
        # Recursive loop multiplies the chara string by n!
        return factorial_alt((n-1), chara)  # Function calls itself, creates recursive loop.
        # It'll stop looping when n = 0, n goes down by one in each loop


main()