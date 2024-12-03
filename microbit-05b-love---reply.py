def on_button_pressed_a():
    global program_state
    if program_state == 1:
        radio.send_string("Y")
        program_state = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global program_state, msg
    program_state = 1
    msg = receivedString
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global program_state
    if program_state == 1:
        radio.send_string("N")
        program_state = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

msg = ""
program_state = 0
basic.show_string("reply")
radio.set_group(123)
# 0 - waiting
# 1 - received
program_state = 0

def on_forever():
    if program_state == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_string("<Y<")
        basic.show_string(">N>")
basic.forever(on_forever)
