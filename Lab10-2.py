# David Garrett
# EET-107-100 Chapter 10 Lab 2
# 4-21-2021

class Computer:  # Creates a class called computer

    def __init__(self, cpu_speed, ram_size, drive_size):  # cpu speed, ram size, and drive size gets passed to initializer
        self.__cpu_speed = cpu_speed
        self.__ram_size = ram_size
        self.__drive_size = drive_size
        # Creates hidden attributes for cpu speed, ram size, and drive size

    def set_cpu(self, speed):  # Mutator Method that changes the cpu speed
        self.__cpu_speed = speed

    def get_cpu(self):  # Accessor method that returns the cpu seed
        return self.__cpu_speed

    def set_ram(self, ram_size):  # Mutator Method that changes the ram size
        self.__ram_size = ram_size

    def get_ram(self):  # Accessor method that returns the ram size
        return self.__ram_size

    def set_drive(self, drive_size):  # Mutator Method that changes the drive size
        self.__drive_size = drive_size

    def get_drive(self):  # Accessor method that returns the drive size
        return self.__drive_size

    def __str__(self):  # Method that returns a string that returns that values of each attributes
        return 'The computer has a CPU running at ' + str(self.get_cpu()) + ' GHz with ' + str(self.get_ram()) + \
               ' GB of RAM and ' + str(self.get_drive()) + ' GB of storage.'


def main():

    user_cpu_speed, user_ram_size, user_drive_size = questions_about_computer()
    # asks user for cpu speed, ram size, and drive size

    computer = Computer(cpu_speed=user_cpu_speed, ram_size=user_ram_size, drive_size=user_drive_size)
    # Creates object, passes cpu speed, ram size, and drive size to the Computer class

    print()
    print(computer)  # prints out the state of the computer object


def questions_about_computer():

    print('Describe your computer.\n')

    while True:  # Input validation loop
        try:
            cpu_speed = float(input('How fast is your computer\'s CPU in GHz? '))
            ram_size = float(input('How much RAM does your computer have in GB? '))
            drive_size = float(input('How much drive space does your computer have in GB? '))
            break
        except ValueError:
            print('Invalid Input')

    return cpu_speed, ram_size, drive_size  # function returns user's cpu speed, ram size, and drive size


main()