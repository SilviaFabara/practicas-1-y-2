def on_button_pressed_a():
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
input.on_button_pressed(Button.A, on_button_pressed_a)

