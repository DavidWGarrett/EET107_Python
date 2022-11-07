# David Garrett
# EET-107-100 Chapter 13 Lab 2
# 5-12-2021

from guizero import App, Drawing


a = App()

# create drawing object
d = Drawing(a, width=220, height=220)
d.rectangle(100, 100, 210, 210, color="light blue")  # Box for frame of house
d.rectangle(120, 130, 140, 150, color="white", outline=True)  # Window 1
d.rectangle(168, 130, 188, 150, color="white", outline=True)  # Window 2
d.rectangle(145, 160, 165, 210, color="brown")  # Door
d.rectangle(120, 90, 135, 40, color="red")  # Chimney
d.oval(148, 185, 152, 188, color="brown", outline=True)  # Door knob
d.triangle(100, 100, 210, 100, 155, 30, color="black")  # Roof

a.display()

