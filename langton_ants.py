# Jacobus Burger (2023)
# A demo of Langton's Ants in NCurses


from random import randint
from time import sleep
from itertools import cycle
SPEED = 0.001  # seconds per step
DIRECTIONS = cycle([[1, 0],[0, 1],[-1, 0],[0, -1]])  # R, D, L, U clockwise
STATE_TRANSITIONS = {   # current state and associated state transition
                        # see: https://en.wikipedia.org/wiki/Langton%27s_ant
    ' ': ('@', 'L'),
    '@': ('+', 'R'),
    '+': ('.', 'L'),
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


# TODO: switch to rendering with pygame for better and more grid tiles
def pygame_ants():
    import pygame
    SCREEN_DIMENSION = (640,480)
    WHITE, RED = (255,255,255), (255,0,0)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_DIMENSION)
    screen.fill(WHITE)
    pygame.display.set_caption("Langton's Ant")
    pygame.draw.rect(screen, RED, (30, 30, 60, 60))
    pygame.display.flip()
    sleep(5)


import curses
from curses import wrapper
def ncurses_ants(stdscr):
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


# TODO: command line switch for curses and pygame graphics mode
# TODO: checks to error out if curses or pygame unavailable
if __name__ == "__main__":
    option = int(input("curses (0) or pygame (1)? "))
    if option == 0:
        wrapper(ncurses_ants)
    if option == 1:
        pygame_ants()
