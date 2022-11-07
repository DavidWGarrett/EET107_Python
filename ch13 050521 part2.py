from guizero import App, Slider, Drawing, Text, Box


##Functions-----------

def red_changed(val):
    red = int(val)
    green = int(green_slider.value)
    blue = int(blue_slider.value)
    draw.rectangle(10,10, 240,240, color=(red, green, blue))

def green_changed(val):
    green = int(val)
    red = int(red_slider.value)
    blue = int(blue_slider.value)
    draw.rectangle(10,10, 240,240, color=(red, green, blue))

def blue_changed(val):
    blue = int(val)
    green = int(green_slider.value)
    red = int(red_slider.value)
    draw.rectangle(10,10, 240,240, color=(red, green, blue))



##App------------

app = App(title='Color Mixer')

draw = Drawing(app, width=250, height=250)
draw.rectangle(10, 10, 240,240, color=(0,0,0))
slider_box = Box(app, layout='grid')
red_slider = Slider(slider_box, start=0, end=255, grid=[0,0], command=red_changed)
red_label = Text(slider_box, text='Red Value', grid=[1,0])

green_slider = Slider(slider_box, start=0, end=255, grid=[0,1], command=green_changed)
green_label = Text(slider_box, text='Green Value', grid=[1,1])

blue_slider = Slider(slider_box, start=0, end=255, grid=[0,2], command=blue_changed)
blue_label = Text(slider_box, text='Blue Value', grid=[1,2])

app.display()