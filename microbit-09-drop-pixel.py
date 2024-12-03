def clear_screen():
    for x in range(5):
        for y in range(5):
            led.unplot(x, y)
def game_win_check():
    global litLED_count, game_state
    litLED_count = 0
    x2 = 0
    while x2 <= len(LEDslitatbottom):
        if LEDslitatbottom[x2] == 1:
            litLED_count = litLED_count + 1
        x2 += 1
    if litLED_count == 5:
        game_state = 2
        basic.show_icon(IconNames.HEART)
        basic.pause(1000)
        basic.show_icon(IconNames.HAPPY)
        basic.pause(1000)
        for x3 in range(5):
            LEDslitatbottom[x3] = empty
        game_state = 0

def on_button_pressed_a():
    global game_state, drop_pixel_xpos, drop_pixel_ypos, lock_drop_pixel
    if game_state == 0:
        game_state = 1
    elif game_state == 1:
        if lock_drop_pixel == 0:
            drop_pixel_xpos = top_pixel_xpos
            drop_pixel_ypos = 0
            lock_drop_pixel = 1
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def secret():
    global game_state
    game_state = 3
    for index in range(2):
        basic.show_leds("""
            . # # # .
            . # # # .
            . . # . .
            . # . # .
            . # . # .
            """)
        basic.show_leds("""
            . . # . .
            . # # # .
            . # # # .
            . # # # .
            . # . # .
            """)
        basic.show_leds("""
            . # # # .
            . # # # .
            . . # . .
            . # . # .
            . # . # .
            """)
        basic.show_leds("""
            . # # # .
            # . # . #
            . . # . .
            . # . # .
            . # . # .
            """)
        basic.show_leds("""
            # # # # #
            . . # . .
            . # # # .
            # . . . #
            . . . . .
            """)
        basic.show_leds("""
            . # # # .
            # . # . #
            . . # . .
            . # . # .
            . # . # .
            """)
        basic.show_leds("""
            . # # # .
            . # # # .
            . . # . .
            . # . # .
            . # . # .
            """)
    game_state = 0
def handle_top_pixel():
    global top_pixel_xpos
    led.plot(top_pixel_xpos, 0)
    led.unplot(top_pixel_xpos - 1, 0)
    if top_pixel_xpos == 0:
        led.unplot(4, 0)
    top_pixel_xpos = top_pixel_xpos + 1
    if top_pixel_xpos == 5:
        top_pixel_xpos = 0
def handle_drop_pixel():
    global drop_pixel_ypos, lock_drop_pixel
    led.plot(drop_pixel_xpos, drop_pixel_ypos)
    led.unplot(drop_pixel_xpos, drop_pixel_ypos - 1)
    drop_pixel_ypos = drop_pixel_ypos + 1
    if drop_pixel_ypos == 5:
        drop_pixel_ypos = -1
        lock_drop_pixel = 0
        LEDslitatbottom[drop_pixel_xpos] = filled

def on_button_pressed_b():
    if game_state == 2:
        secret()
input.on_button_pressed(Button.B, on_button_pressed_b)

drop_pixel_xpos = 0
litLED_count = 0
empty = 0
filled = 0
LEDslitatbottom: List[number] = []
drop_pixel_ypos = 0
lock_drop_pixel = 0
top_pixel_xpos = 0
game_state = 0
game_state = 0
top_pixel_xpos = 0
lock_drop_pixel = 0
drop_pixel_ypos = -1
LEDslitatbottom = [0, 0, 0, 0, 0]
filled = 1
empty = 0

def on_forever():
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
        clear_screen()
    elif game_state == 1:
        handle_top_pixel()
        basic.pause(500)
        if drop_pixel_ypos >= 0:
            handle_drop_pixel()
        game_win_check()
    else:
        pass
basic.forever(on_forever)
