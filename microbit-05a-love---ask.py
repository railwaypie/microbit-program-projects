def on_button_pressed_a():
    if program_state == 0:
        radio.send_string("love me?")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global program_state
    program_state = 2
    if receivedString == "Y":
        for index in range(4):
            basic.show_icon(IconNames.HEART)
    else:
        for index2 in range(4):
            basic.show_icon(IconNames.NO)
    program_state = 0
radio.on_received_string(on_received_string)

program_state = 0
basic.show_string("Ask")
radio.set_group(123)
# 0 - waiting
# 1 - question sent
# 2 - reply received
program_state = 0

def on_forever():
    if program_state == 0:
        basic.show_string("ask q?")
basic.forever(on_forever)
