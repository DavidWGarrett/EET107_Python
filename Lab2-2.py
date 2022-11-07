#David Garrett
#EET-107-100 Chapter 2 Lab 2
#2021-02-01

#Use turtle graphics to draw my initials
import turtle
turtle.speed(3)
turtle.width(5)

#first initial
turtle.penup()
turtle.goto(-500,350)
turtle.pendown()
turtle.circle(-350, 180)
turtle.forward(75)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(75)

#second initial
turtle.penup()
turtle.goto(250,350)
turtle.pendown()
turtle.circle(-350, 45)
turtle.penup()
turtle.goto(250,350)
turtle.pendown()
turtle.setheading(180)
turtle.circle(350, 265)
turtle.setheading(180)
turtle.forward(250)