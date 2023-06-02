def on_button_pressed_a():
    for index in range(2):
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.show_icon(IconNames.YES)
        basic.pause(7000)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.show_leds("""
            . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
                        . . # . .
        """)
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.show_icon(IconNames.NO)
        basic.pause(7000)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P1, 0)
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if input.is_gesture(Gesture.SCREEN_UP):
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif input.is_gesture(Gesture.SCREEN_DOWN):
        basic.show_icon(IconNames.SQUARE)
    elif input.is_gesture(Gesture.TILT_RIGHT):
        basic.show_icon(IconNames.SCISSORS)
    else:
        basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)
