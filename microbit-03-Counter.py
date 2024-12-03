def on_button_pressed_a():
    global count
    count = count + 1
    basic.show_number(count)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global count
    count = 0
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # . .
        . . # . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # .
        . # # . .
        . . # . .
        """)
    basic.show_leds("""
        . # # . .
        . # # # #
        # # # # #
        . # # # .
        # . # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(500)
    basic.show_number(count)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global count
    count = count - 1
    basic.show_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
basic.show_string("Counter")
count = 0

def on_forever():
    pass
basic.forever(on_forever)
