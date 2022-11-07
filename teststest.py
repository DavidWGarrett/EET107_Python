# David Garrett
# EET-107-100 Chapter 13 Lab 1
# 5-12-2021

from guizero import App, TextBox, Text, PushButton


class ftin:

    def __init__(self):

        self.__app = App(layout='grid')

        self.__km_label = Text(app, grid=[0, 0], text='enter a distance in km: ')
        self.__km_textbox = TextBox(app, grid=[1, 0])

        self.__mile_lab = Text(app, text='converted to miles: ', grid=[0, 1], align='right')
        self.__mile_output = Text(app, text='', grid=[1, 1])

        self.__convert_button = PushButton(app, text='convert', command=convert_km, grid=[0, 2])
        self.__quit_button = PushButton(app, text='Quit', command=quit_app, grid=[1, 2])

        self.__app2 = App(display)

def main():

     test = ftin()

     test.ftin(app2)



main()