# Jacobus Burger (2023)
# A demo of Langton's Ants using NCurses
from random import randint
from time import sleep
from itertools import cycle
SPEED = 0.1  # seconds per step
DIRECTIONS = cycle([[1, 0],[0, 1],[-1, 0],[0, -1]])  # R, D, L, U clockwise
SYM1 = ' '
SYM2 = '@'
SYM3 = '+'
SYM4 = '.'
# current state and associated state transition
# see: https://en.wikipedia.org/wiki/Langton%27s_ant
STATE_TRANSITIONS = {
    SYM1: (SYM2, 'L'),
    SYM2: (SYM3, 'R'),
    SYM3: (SYM4, 'L'),
    SYM4: (SYM1, 'R'),
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
        # there must be a better way
        for _ in range(3):  # jump forward 3 on the 4-cycle in
                            # DIRECTIONS to go backwards once in
                            # the cycle
            next_move = next(DIRECTIONS)
    # return state change tuple
    return (next_symbol, next_move)


def ants():
    global SPEED
    # begin curses
    import curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    # init application
    stdscr.refresh()
    stdscr.nodelay(True)
    ant_position = [randint(0, curses.COLS), randint(0, curses.LINES)]
    move = [1, 0]
    # start main loop
    while True:
        # receive user interrupts
        c = stdscr.getch()
        if c == ord('q'):
            break  # quit
        if c == ord('='):
            SPEED = max(SPEED - 0.01, 0.01)
        if c == ord('-'):
            SPEED = min(SPEED + 0.1, 0.1)
        # get current character
        symbol = chr(stdscr.inch(ant_position[1], ant_position[0]) & 0xFF)
        # update state of automata
        symbol, move = next_state(symbol, move)
        # update screen
        stdscr.addch(ant_position[1], ant_position[0], symbol)
        stdscr.refresh()
        # wait until next frame
        sleep(SPEED)
        # move to next position
        ant_position = [
            (ant_position[0] + move[0]) % curses.COLS,
            (ant_position[1] + move[1]) % curses.LINES,
        ]
    # end curses
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    ants()
