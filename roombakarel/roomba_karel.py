from stanfordkarel import *


def main():
    while front_is_clear():
        clean_row()
        turn_around()


# Roomba Karel cleans one row picking up all the beepers
def clean_row():
    while front_is_clear():
        pick_up_all_beepers()
        move()
        pick_up_all_beepers()


# Roomba Karel turns at the end of the row and gets into position to clean the next row
def turn_around():
    if facing_east():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
            turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def pick_up_all_beepers():
    while beepers_present():
        pick_beeper()


# don't change this code
if __name__ == '__main__':
    run_karel_program()
