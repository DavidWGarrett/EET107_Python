# library goeyzero (gooey zero?) easier library

print('class ex')

import random

class dice():
    def __init__(self, num_sides):
        self.set_num_sides(num_sides)
        self.__side_up = 1

    def dice_roll(self):
        self.__side_up = random.randint(1,self.__num_sides)
        
    def set_num_sides(self, num_sides):
        if num_sides < 2:
            print('1 sided dice?')
        else:
            self.__num_sides = num_sides
        #self reference the object
        self.__side_up = self.dice_roll()
        #two underscores makes attribute hidden
    
        
    def get_sideup(self):
        return self.__side_up
        
    def get_num_sides(self):
        return self.__num_sides
    
    def __str__(self): 
        return "The side up is: " + str(self.__side_up)