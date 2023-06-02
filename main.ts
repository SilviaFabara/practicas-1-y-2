input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 2; index++) {
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
    }
    basic.showIcon(IconNames.Happy)
})
input.onGesture(Gesture.ScreenUp, function () {
    basic.showIcon(IconNames.Target)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Scissors)
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showIcon(IconNames.Square)
})
