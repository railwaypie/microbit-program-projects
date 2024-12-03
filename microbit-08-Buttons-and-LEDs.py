def on_button_pressed_a():
    global current_index
    if current_index < 24:
        current_index = current_index + 1
        LED_indexes[current_index] = on
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global current_index
    if current_index > 0:
        LED_indexes[current_index] = off
        current_index = current_index - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

current_index = 0
LED_indexes: List[number] = []
on = 0
off = 0
basic.show_string("LEDs")
off = 0
on = 1
LED_indexes = []
for index in range(25):
    LED_indexes.insert_at(index, off)
    current_index = -1

def on_forever():
    for index2 in range(25):
        if LED_indexes[index2] == 1:
            if index2 >= 20:
                led.plot(index2 - 20, 4)
            elif index2 >= 15:
                led.plot(index2 - 15, 3)
            elif index2 >= 10:
                led.plot(index2 - 10, 2)
            elif index2 >= 5:
                led.plot(index2 - 5, 1)
            else:
                led.plot(index2, 0)
        else:
            if index2 >= 20:
                led.unplot(index2 - 20, 4)
            elif index2 >= 15:
                led.unplot(index2 - 15, 3)
            elif index2 >= 10:
                led.unplot(index2 - 10, 2)
            elif index2 >= 5:
                led.unplot(index2 - 5, 1)
            else:
                led.unplot(index2, 0)
basic.forever(on_forever)
