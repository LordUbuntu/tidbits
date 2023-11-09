# Jacobus Burger (2023)
# A demo of Langton's Ants in NCurses

from random import randint
from time import sleep
from itertools import cycle
import curses
from curses import wrapper
SPEED = 0.001  # seconds per step
DIRECTIONS = cycle([[1, 0],[0, 1],[-1, 0],[0, -1]])  # R, D, L, U clockwise
STATE_TRANSITIONS = {   # current state and associated state transition
                        # see: https://en.wikipedia.org/wiki/Langton%27s_ant
    ' ': ('@', 'L'),
    '@': ('+', 'L'),
    '+': ('.', 'R'),
    '.': (' ', 'R'),
}


# state change of automata based on current tile state
def next_state(symbol: str, move: list):
    # get next action
    next_symbol, rotation = STATE_TRANSITIONS.get(symbol)
    # change position
    next_move = [0, 0]
    if rotation == 'R':   # CW
        next_move = next(DIRECTIONS)
    elif rotation == 'L': # CCW
        for _ in range(3):  # 3 forward on a 4-cycle is the same as 1 backward
            next_move = next(DIRECTIONS)
    # return state change tuple
    return (next_symbol, next_move)


def main(stdscr):
    # begin program
    stdscr.refresh()
    ant_position = [randint(0, curses.COLS), randint(0, curses.LINES)]
    move = [1, 0]
    while True:
        # get current character
        symbol = chr(stdscr.inch(ant_position[1], ant_position[0]) & 0xFF)
        # update state of automata
        symbol, move = next_state(symbol, move)
        # update screen
        stdscr.addch(ant_position[1], ant_position[0], symbol)
        stdscr.refresh()
        sleep(SPEED)
        # move to next position
        ant_position = [
            (ant_position[0] + move[0]) % curses.COLS,
            (ant_position[1] + move[1]) % curses.LINES,
        ]



if __name__ == "__main__":
    wrapper(main)
