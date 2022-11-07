# David Garrett
# EET-107-100 GUI control part 2
# 5-12-2021

from guizero import App, TextBox, Text, PushButton, Slider, CheckBox, ListBox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def main():

    led_pins_dict = {'Red LED': 20, 'Blue LED': 21}

    for pin in led_pins_dict:
        GPIO.setup(led_pins_dict[pin], GPIO.OUT)
        GPIO.output(led_pins_dict[pin], False)

    pwn_red = GPIO.pwn(20, 250)
    pwm_red.start(0)
    pwn_blue = GPIO.pwn(21, 250)
    pwn_blue.start(0)

    app = App(title='LED Controller', layout='grid')
    led_text = Text(app, grid=[0, 0], text='LED Controls')

    red_led_checkbox = CheckBox(app,
                                text='Red LED',
                                command=lambda: state(red_led_checkbox, red_led_state, led_pins_dict),
                                grid=[0, 1])
    red_led_state = Text(app, grid=[1, 1], text='Off')
    red_slider = Slider(app, grid=[2, 1], command=lambda: slider_changed(red_slider, red_textbox, pwn_red))
    red_textbox = TextBox(app, grid=[3, 1], command=lambda: txtbox_changed(red_slider, red_textbox, pwn_red))

    blue_led_checkbox = CheckBox(app,
                                 text='Blue LED',
                                 command=lambda: state(blue_led_checkbox, blue_led_state, led_pins_dict),
                                 grid=[0, 2])

    blue_led_state = Text(app, grid=[1, 2], text='Off')
    blue_slider = Slider(app, grid=[2, 1], command=lambda: slider_changed(blue_slider, blue_textbox, pwn_blue))
    blue_textbox = TextBox(app, grid=[3, 1], command=lambda: txtbox_changed(blue_slider, blue_textbox, pwn_blue))

    quit_button = PushButton(app, text='Quit',
                             command=quit_app, args=[app],  grid=[4, 4])

    app.display()


def state(checkbox, state, dictio):
    if checkbox.value == 1:
        state.value = 'On'
        for led in dictio:
            if checkbox.text == led:
                GPIO.output(dictio[led], True)
    else:
        state.value = 'Off'
        for led in dictio:
            if checkbox.text == led:
                GPIO.output(dictio[led], False)
    return checkbox, state


def slider_changed(slider, txtbox, pwn):
    slider.value = txtbox.value
    pwm.ChangeDutyCycle(slider.value)
    return slider, txtbox, pwn


def txtbox_changed(slider, txtbox, pwn):
    txtbox.value = slider.value
    pwm.ChangeDutyCycle(txtbox.value)
    return slider, txtbox, pwn


def quit_app(app):
    app.destroy()
    GPIO.cleanup()


main()
