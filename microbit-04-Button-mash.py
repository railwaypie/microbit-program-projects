def on_button_pressed_a():
    global game_state, start_time, count
    game_state = 1
    start_time = input.running_time()
    count = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global count
    if game_state == 1:
        count = count + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
start_time = 0
game_state = 0
basic.show_string("Q Count")
# Records the current game state:
# 0 - not started
# 1 - game has started
# 2 - game has finished
game_state = 0

def on_forever():
    global game_state
    if game_state == 0:
        basic.show_string("A")
    elif game_state == 1:
        if input.running_time() - start_time > 2000:
            game_state = 2
    else:
        basic.show_number(count)
        if count > 9:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                """)
        elif count > 6:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                # # # # #
                . . . . .
                """)
        else:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
                """)
basic.forever(on_forever)
