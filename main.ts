function check() {
    
    while (correct_1 == 0 && correct_2 == 0) {
        correct_1 = 0
        correct_2 = 0
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 0)
        pins.digitalWritePin(DigitalPin.P10, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        basic.pause(correct_1)
        pins.digitalWritePin(DigitalPin.P9, 1)
        basic.pause(correct_2)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 0)
        pins.digitalWritePin(DigitalPin.P10, 0)
    }
}

function correct() {
    
    correct_1 = 10000
    correct_2 = 2000
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P10, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
    basic.pause(correct_1)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(correct_2)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P10, 1)
    basic.pause(10000)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    correct_1 = 10000
    correct_2 = 2000
    condition = 1
})
function traffic_light() {
    if (condition == 1) {
        correct()
    }
    
    if (condition == 2) {
        _false()
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    condition = 2
})
function start() {
    
    condition = 0
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P9, 1)
    pins.digitalWritePin(DigitalPin.P10, 1)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P10, 0)
}

function _false() {
    
    if (correct_1 == 0 && correct_2 == 0) {
        correct_1 = 0
        correct_2 = 0
        pins.digitalWritePin(DigitalPin.P10, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 1)
        basic.pause(140)
        pins.digitalWritePin(DigitalPin.P9, 0)
        basic.pause(140)
    } else {
        check()
        correct_1 = 0
        correct_2 = 0
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 0)
        pins.digitalWritePin(DigitalPin.P10, 0)
    }
    
}

let condition = 0
let correct_2 = 0
let correct_1 = 0
start()
basic.forever(function on_forever() {
    traffic_light()
})
