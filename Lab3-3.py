#David Garrett
#EET-107-100 Chapter 3 Lab 3
#2021-02-08

#Ask user if he or she would like to draw a circle, square, or triangle and ask for size of the shape

import turtle

user_shape = input('Would you like to draw a circle, square, or triangle? ')

if user_shape == 'circle' or user_shape == 'Circle':
    radius_of_circle = int(input('What radius would you like the circle to have? (1 - 200) '))
    if radius_of_circle < 1 or radius_of_circle > 200:
        print('Invalid length')
    else:
        turtle.circle(radius_of_circle, 360)

elif user_shape == 'square' or user_shape == 'Square':
    side_of_square = int(input('How long would you like each side of the square to be? (1 - 200) '))
    if side_of_square < 1 or side_of_square > 200:
        print('Invalid length')
    else:
        turtle.forward(side_of_square)
        turtle.left(90)
        turtle.forward(side_of_square)
        turtle.left(90)
        turtle.forward(side_of_square)
        turtle.left(90)
        turtle.forward(side_of_square)

elif user_shape == 'triangle' or user_shape == 'Triangle':
    side_of_triangle = int(input('How long would you like each side of the triangle to be? (1 - 200) '))
    if side_of_triangle < 1 or side_of_triangle > 200:
        print('Invalid length')
    else:
        turtle.setheading(240)
        turtle.forward(side_of_triangle)
        turtle.setheading(0)
        turtle.forward(side_of_triangle)
        turtle.setheading(120)
        turtle.forward(side_of_triangle)

else:
    print('Not a valid choice of shape')