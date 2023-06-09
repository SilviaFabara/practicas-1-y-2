input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.showIcon(IconNames.Yes)
    basic.pause(7000)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        `)
    basic.pause(2000)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(2000)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.showIcon(IconNames.No)
    basic.pause(7000)
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(2000)
    pins.digitalWritePin(DigitalPin.P1, 0)
})
