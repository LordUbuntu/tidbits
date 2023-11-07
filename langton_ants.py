# Jacobus Burger (2023)
# A demo of Langton's Ants in NCurses

from random import randint
from time import sleep
import curses
from curses import wrapper
SPEED = 0.5


def main(stdscr):
    # begin program
    stdscr.refresh()
    ant_position = [randint(0, curses.COLS), randint(0, curses.LINES)]
    # NOTE: recall taylor series for sin, turning left or right can boil
    # down to [i % 2, (i + 1) % 2] for left, [(i + 1) % 2, i % 2] for right,
    # i just need to figure out how to get correct sign at each point.
    direction = [
        # [dx, dy]
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ] # 0-r, 1-d, 2-l, 3-u
    current_direction = 0
    while True:
        # get current character
        current_character = chr(stdscr.inch(ant_position[1], ant_position[0]) & 0xFF)
        # invert it and turn right or left
        if current_character == ' ':
            stdscr.addch(ant_position[1], ant_position[0], '@')  # dig
            current_direction = (current_direction + 1) % 4  # turn right
        elif current_character == '@':
            stdscr.addch(ant_position[1], ant_position[0], ' ')  # undig
            current_direction = (current_direction - 1) % 4  # turn left
        # update screen
        sleep(SPEED)
        stdscr.refresh()
        # move to next position
        # NOTE: gets stuck on the edge, figure out a way to wraparound
        if ant_position[0] + direction[current_direction][0] < 0 \
                or ant_position[0] + direction[current_direction][0] > curses.COLS:
            pass
        if ant_position[1] + direction[current_direction][1] < 0 \
                or ant_position[1] + direction[current_direction][1] > curses.LINES:
            pass
        ant_position = [
            ant_position[0] + direction[current_direction][0],
            ant_position[1] + direction[current_direction][1],
        ]



if __name__ == "__main__":
    wrapper(main)
