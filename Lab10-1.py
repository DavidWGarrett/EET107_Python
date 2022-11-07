# David Garrett
# EET-107-100 Chapter 10 Lab 1
# 4-21-2021

class Vehicle:  # class is created called vehicle

    def __init__(self, make, color):  # Initializer that sets speed to 0, and requires a vehicle's make and color
        self.__speed = 0
        self.__make = make
        self.__color = color
    # creates hidden attributes which are the speed, make, and color
    
    def set_make(self, make):  # Mutator Method that changes the make
        self.__make = make

    def get_make(self):  # Accessor method that returns the make
        return self.__make
        
    def set_color(self, color):  # Mutator Method that changes the color
        self.__color = color

    def get_color(self):  # Accessor method that returns the color
        return self.__color

    def display_speed(self):  # method that displays object's speed
        print('Current speed: ' + str(self.__speed))

    def accelerate(self):  # method that lets the object's speed go up 1
        print('Accelerating...')
        self.__speed += 1

    def decelerate(self):  # method that lets the object's speed go down 1
        print('Decelerating...')
        self.__speed -= 1


def main():

    vehicle = Vehicle(make='ford', color='black')  # creates object, passes the make and color to the object

    for accel in range(2):  # for loop that accelerates the vehicle object two times
        vehicle.accelerate()
        vehicle.display_speed()

    print()

    for deaccel in range(2):  # for loop that deaccelerates the vehicle object two times
        vehicle.decelerate()
        vehicle.display_speed()
        

main()