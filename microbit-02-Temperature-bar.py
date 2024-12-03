def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

recorded_temperature = 0
basic.show_string("Temp bar")

def on_forever():
    global recorded_temperature
    recorded_temperature = input.temperature()
    if recorded_temperature > 27:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif recorded_temperature > 25:
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif recorded_temperature > 23:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
    elif recorded_temperature > 21:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
basic.forever(on_forever)
