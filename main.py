def check():
    global correct_1, correct_2
    while correct_1 == 0 and correct_2 == 0:
        correct_1 = 0
        correct_2 = 0
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.digital_write_pin(DigitalPin.P10, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        basic.pause(correct_1)
        pins.digital_write_pin(DigitalPin.P9, 1)
        basic.pause(correct_2)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.digital_write_pin(DigitalPin.P10, 0)
def correct():
    global correct_1, correct_2
    correct_1 = 10000
    correct_2 = 2000
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(correct_1)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(correct_2)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 1)
    basic.pause(10000)

def on_button_pressed_a():
    global correct_1, correct_2, condition
    correct_1 = 10000
    correct_2 = 2000
    condition = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def traffic_light():
    if condition == 1:
        correct()
    if condition == 2:
        _false()

def on_button_pressed_b():
    global condition
    condition = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def start():
    global condition
    condition = 0
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P9, 1)
    pins.digital_write_pin(DigitalPin.P10, 1)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 0)
def _false():
    global correct_1, correct_2
    if correct_1 == 0 and correct_2 == 0:
        correct_1 = 0
        correct_2 = 0
        pins.digital_write_pin(DigitalPin.P10, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        basic.pause(140)
        pins.digital_write_pin(DigitalPin.P9, 0)
        basic.pause(140)
    else:
        check()
        correct_1 = 0
        correct_2 = 0
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.digital_write_pin(DigitalPin.P10, 0)
condition = 0
correct_2 = 0
correct_1 = 0
start()

def on_forever():
    traffic_light()
basic.forever(on_forever)
