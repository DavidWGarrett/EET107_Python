#David Garrett
#EET-107-100 Chapter 4 Lab 2
#2-21-2021

import turtle

# Assigns value before pretest loop
lines_pyramid = 0

while lines_pyramid < 1 or lines_pyramid > 10: # Input Validation Loop
    try:
        lines_pyramid = int(input('Enter the number of lines in the pyramid (1-10) ')) # Asks user for number of lines
    except ValueError: # Condition fails if input is not an integer
        print('Not a valid number')
        continue
    if lines_pyramid < 1 or lines_pyramid > 10: # Condition fails if input is not within 1-10 range
        print('Not within range')
        continue

# Draws pyramid based on number the user input earlier

for x in range(1, lines_pyramid+1):
    turtle.speed(5)
    turtle.screensize(100,100)
    turtle.forward(x*100)
    turtle.backward(x*200)
    turtle.forward(x*100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.pendown()