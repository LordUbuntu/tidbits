# Jacobus Burger (2023)
# A demo of Langton's Ants in NCurses

from random import randint
from time import sleep
from itertools import cycle
import curses
from curses import wrapper
SPEED = 0.02  # seconds per step


ACTION = {  # character and associated action, add your own!
            # see: https://en.wikipedia.org/wiki/Langton%27s_ant
    ' ': ('@', 'R'),
    '@': ('+', 'L'),
    '+': (' ', 'R'),
}
# state change of automata based on current tile state
def step(symbol: str, direction: list):
    # get next action
    next_symbol, rotation = ACTION.get(symbol)
    # change position
    # TODO: use cycle here instead
    next_direction = [0, 0]
    if rotation == 'R':
        if direction == [1, 0]:
            next_direction = [0, 1]
        if direction == [0, 1]:
            next_direction = [-1, 0]
        if direction == [-1, 0]:
            next_direction = [0, -1]
        if direction == [0, -1]:
            next_direction = [1, 0]
    elif rotation == 'L':
        if direction == [1, 0]:
            next_direction = [0, -1]
        if direction == [0, -1]:
            next_direction = [-1, 0]
        if direction == [-1, 0]:
            next_direction = [0, 1]
        if direction == [0, 1]:
            next_direction = [1, 0]
    # return state change tuple
    return (next_symbol, next_direction)


def main(stdscr):
    # begin program
    stdscr.refresh()
    ant_position = [randint(0, curses.COLS), randint(0, curses.LINES)]
    # NOTE: recall taylor series for sin, turning left or right can boil
    # down to [i % 2, (i + 1) % 2] for left, [(i + 1) % 2, i % 2] for right,
    # i just need to figure out how to get correct sign at each point.
    # TODO: represent direction as a cycle, just increment each time. If you want to
    # turn left, then increment by 3 instead, thus "rotating" the 4-cycle, with no
    # need for a variable to track direction or whatever
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
            stdscr.addch(ant_position[1], ant_position[0], '@')
            current_direction = (current_direction + 1) % 4  # turn right
        elif current_character == '@':
            stdscr.addch(ant_position[1], ant_position[0], '+')
            current_direction = (current_direction - 1) % 4  # turn left
        elif current_character == '+':
            stdscr.addch(ant_position[1], ant_position[0], ' ')
            current_direction = (current_direction + 1) % 4  # turn right
        # update screen
        sleep(SPEED)
        stdscr.refresh()
        # move to next position
        ant_position = [
            (ant_position[0] + direction[current_direction][0]) % curses.COLS,
            (ant_position[1] + direction[current_direction][1]) % curses.LINES,
        ]



if __name__ == "__main__":
    wrapper(main)
