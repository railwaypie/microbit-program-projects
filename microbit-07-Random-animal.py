def on_button_pressed_a():
    global random_choice, choice
    random_choice = randint(0, len(animal_names) - 1)
    choice = animal_names[random_choice]
input.on_button_pressed(Button.A, on_button_pressed_a)

choice = ""
random_choice = 0
animal_names: List[str] = []
basic.show_string("RanAn")
animal_names = ["cow", "dog", "cat"]

def on_forever():
    basic.show_string("" + (choice))
basic.forever(on_forever)
