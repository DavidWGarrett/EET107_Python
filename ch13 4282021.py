#ff

#gooey gui

#tkinter is main graphical environment, there are others
#portable across diff OS
#entry = textbox widget

import tkinter
#######guizero 

#print(os.getcwd())

#window = tkinter.Tk()
#window.destroy() closes window

class aa:
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.hello_label = tkinter.Label(self.main_window, 
                                        text='hello gui')
        self.hello_label.pack()
        tkinter.mainloop() # creates like a while True loop


#main_gui = aa()

from guizero import App, TextBox, Text, PushButton


#DEFINE FUNCTIONS ABOVE GUIZERO 

def convert_km():
    km = float(km_textbox.value) # gets value from textbox
    miles = km * 0.6214
    mile_output.value = format(miles, '.2f')
    
def quit_app():
    app.destroy()

app = App(layout='grid')

km_label = Text(app, grid=[0,0], text='enter a distance in km: ')
km_textbox = TextBox(app, grid=[1,0])

mile_lab = Text(app, text='converted to miles: ', grid=[0,1], align='right')
mile_output = Text(app, text='', grid=[1,1])

convert_button = PushButton(app, text='convert', command=convert_km, grid=[0,2])
quit_button = PushButton(app, text='Quit', command=quit_app, grid=[1,2])

app.display()  # put at the end







