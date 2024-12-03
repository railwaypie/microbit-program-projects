def on_gesture_shake():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
    basic.pause(2000)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    """)

def on_forever():
    pass
basic.forever(on_forever)
