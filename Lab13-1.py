# David Garrett
# EET-107-100 Chapter 13 Lab 1
# 5-12-2021

from guizero import App, TextBox, Text, PushButton

class ftin:

    def __init__(self):  # Initializer, creates attributes upon creation of object

        self.app = App(layout='grid')

        inch_text = ''

        self.top_label = Text(self.app, grid=[0, 0], text='Feet and Inches Converter')

        self.feet_label = Text(self.app, grid=[0, 1], text='Feet: ')
        self.feet_textbox = TextBox(self.app, grid=[1, 1])  # Textbox to input feet
        self.inches_label = Text(self.app, grid=[2, 1], text='Inches: ')
        self.inches_textbox = TextBox(self.app, grid=[3, 1])  # Textbox to input inches

        self.total_inches_label = Text(self.app, text='Total Inches: ', grid=[0, 2], align='right')
        self.inches_output = Text(self.app, text=inch_text, grid=[1, 2])  # Attribute displays total inches

        self.convert_button = PushButton(self.app,
                                         text='Convert',
                                         # Push Button calls convert_to_total_in function
                                         command=lambda:convert_to_total_in(self,
                                                                            self.feet_textbox.value,
                                                                            self.inches_textbox.value),
                                         grid=[0, 3])
        self.quit_button = PushButton(self.app, text='Quit', command=quit_app, args=[self.app], grid=[1, 3])
        # Push Button calls the quit_app function, terminates program

        self.app.display()

    def set_total_inches(self, total_in):  # Creates method to display total inches
        self.inches_output = Text(self.app, text=str(total_in), grid=[1, 2])



def main():

    test = ftin()  # Creates Object


def convert_to_total_in(obj, ft_value, in_value):  # Converts feet and inches values to total inches
    ft = float(ft_value)  # gets value from textbox
    inch = float(in_value)
    total_in = ft*12 + inch
    total_inches_output = format(total_in, '.2f')
    obj.set_total_inches(total_inches_output)


def quit_app(app):  # Closes Program
    app.destroy()


main()