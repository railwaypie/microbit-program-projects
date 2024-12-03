def on_button_pressed_a():
    global game_state
    game_state = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def win_animation():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . # . # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
    basic.show_leds("""
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . # # # .
        """)
    basic.show_leds("""
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        . # # # .
        """)
def game_animation():
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . # .
        . . # . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . #
        . . . # .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . # # .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # .
        . . . . #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . # .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . . # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . # . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . # . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . . . .
        . # # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . . . .
        . # . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # . . .
        . . # . .
        . . # . .
        . . . . .
        . . . . .
        """)
    for index in range(3):
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
random_choice = 0
game_state = 0
basic.show_string("Rou")
# 0 - waiting to play
# 1 - playing
game_state = 0

def on_forever():
    global random_choice, game_state
    if game_state == 0:
        basic.show_leds("""
            . # # # .
            # . . . #
            # # # # #
            # . . . #
            # . . . #
            """)
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
    else:
        random_choice = randint(0, 1)
        game_animation()
        if random_choice == 1:
            win_animation()
            game_state = 0
        else:
            basic.show_icon(IconNames.SKULL)
            basic.pause(2000)
            game_state = 0
basic.forever(on_forever)
