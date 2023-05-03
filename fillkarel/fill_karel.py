from stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while left_is_clear():
        fill_row()
        return_to_start()
        change_row()
    fill_row()


# places beepers on every space in the row
def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


# enables Karel to return to the start of the row
def return_to_start():
    turn_left()
    turn_left()
    while front_is_clear():
        move()


# enables Karel to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# enables Karel to change directions and move to the next row
def change_row():
    turn_right()
    move()
    turn_right()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    run_karel_program()
