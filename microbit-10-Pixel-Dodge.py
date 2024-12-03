def collision():
    global game_state
    game_state = 3
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.CHESSBOARD)
    show_score()
def move_pixels_down():
    global score, clock
    index = 0
    while index <= pixels_to_drop_total - 1:
        if ypos_of_all_drop_pixels[index] >= 0 or ypos_of_all_drop_pixels[index] <= 5:
            led.plot(xpos_for_all_drop_pixels[index],
                ypos_of_all_drop_pixels[index])
            if ypos_of_all_drop_pixels[index] == 4:
                if player_xpos == xpos_for_all_drop_pixels[index]:
                    collision()
            led.unplot(xpos_for_all_drop_pixels[index],
                ypos_of_all_drop_pixels[index] - 1)
            if ypos_of_all_drop_pixels[index] == 5:
                score = score + 1
        ypos_of_all_drop_pixels[index] = ypos_of_all_drop_pixels[index] + 1
        index += 1
    clock = clock - 1
    if clock == 0:
        move_up_level()
def move_up_level():
    global current_level, game_state
    if current_level < 4:
        current_level = current_level + 1
        game_state = 1
        make_level_2_arrays()
    else:
        basic.show_string("You win!")
        show_score()
def make_level_2_arrays():
    global pixels_to_drop_total, xpos_for_all_drop_pixels, rand_xpos, ypos_of_all_drop_pixels, drop_frequency, clock, game_speed
    pixels_to_drop_total = current_level * 10
    xpos_for_all_drop_pixels = []
    index2 = 0
    while index2 <= pixels_to_drop_total - 1:
        rand_xpos = randint(0, 4)
        xpos_for_all_drop_pixels.append(rand_xpos)
        index2 += 1
    ypos_of_all_drop_pixels = []
    drop_frequency = 5 - current_level
    index3 = 0
    while index3 <= pixels_to_drop_total - 1:
        ypos_of_all_drop_pixels.append(drop_frequency * index3 * -1)
        index3 += 1
    clock = drop_frequency * (pixels_to_drop_total - 1) + 9
    if game_state == 4:
        game_speed = 150
    else:
        game_speed = 200
def clean_screen():
    for x in range(5):
        for y in range(5):
            led.unplot(x, y)

def on_button_pressed_a():
    global game_state, player_xpos
    if game_state == 0 or game_state == 4:
        make_level_2_arrays()
        game_state = 1
    elif game_state == 2:
        if player_xpos > 0:
            player_xpos = player_xpos - 1
            led.plot(player_xpos, 4)
            led.unplot(player_xpos + 1, 4)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global game_state
    if game_state == 0:
        game_state = 4
    else:
        game_state = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global game_state, player_xpos
    if game_state == 0 or game_state == 4:
        make_level_2_arrays()
        game_state = 1
    elif game_state == 2:
        if player_xpos < 4:
            player_xpos = player_xpos + 1
            led.plot(player_xpos, 4)
            led.unplot(player_xpos - 1, 4)
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def show_score():
    global score, current_level, game_state
    basic.show_number(score)
    basic.pause(1000)
    score = 0
    current_level = 1
    game_state = 0
drop_frequency = 0
rand_xpos = 0
clock = 0
xpos_for_all_drop_pixels: List[number] = []
ypos_of_all_drop_pixels: List[number] = []
pixels_to_drop_total = 0
game_speed = 0
player_xpos = 0
current_level = 0
score = 0
game_state = 0
# 0 - before playing
# 1 - playing intro
# 2 - playing game
# 3 - collision detected
# 4 - crazy mode
game_state = 0
score = 0
current_level = 1
player_xpos = 2
game_speed = 200

def on_forever():
    global game_state
    if game_state == 0:
        basic.show_icon(IconNames.GHOST)
    elif game_state == 1:
        for index4 in range(2):
            basic.show_string("L")
            basic.show_number(current_level)
        clean_screen()
        game_state = 2
        led.plot(player_xpos, 4)
    elif game_state == 2:
        move_pixels_down()
        basic.pause(game_speed)
    elif game_state == 4:
        basic.show_icon(IconNames.SKULL)
    else:
        pass
basic.forever(on_forever)
