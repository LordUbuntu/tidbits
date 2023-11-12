# Jacobus Burger (2023)
# A demo of Langton's Ants in NCurses


from random import randint
from time import sleep
from itertools import cycle
SPEED = 0.001  # seconds per step
DIRECTIONS = cycle([[1, 0],[0, 1],[-1, 0],[0, -1]])  # R, D, L, U clockwise
SYM1 = ' '
SYM2 = '@'
SYM3 = '+'
SYM4 = '.'
STATE_TRANSITIONS = {   # current state and associated state transition
                        # see: https://en.wikipedia.org/wiki/Langton%27s_ant
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
        for _ in range(3):  # 3 forward on a 4-cycle is the same as 1 backward
            next_move = next(DIRECTIONS)
    # return state change tuple
    return (next_symbol, next_move)


# TODO: switch to rendering with pygame for better and more grid tiles
def pygame_ants():
    # setup
    import pygame
    SCREEN_DIMENSION = (480,480)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    tile_data = {
        # (x,y): symbol
        (0, 0): SYM2,
    }
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_DIMENSION)
    screen.fill(WHITE)
    pygame.display.set_caption("Langton's Ant")

    # get color from tile symbol
    def tile_color(symbol):
        if symbol == SYM1:
            return BLACK
        if symbol == SYM2:
            return RED
        if symbol == SYM3:
            return GREEN
        if symbol == SYM4:
            return BLUE
        return WHITE

    # 16x16 grid of tiles on a 480x480 pixel screen
    def draw_grid(tile_data):
        for i in range(16):
            for j in range(16):
                pygame.draw.rect(screen, tile_color(tile_data.get((i,j))), (i * 30, j * 30, 30, 30), 0)
                pygame.draw.rect(screen, BLACK, (i * 30, j * 30, 30, 30), 1)

    # run
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        draw_grid(tile_data)
        pygame.display.flip()
        # sleep(5)
    pygame.quit()


def ncurses_ants(stdscr):
    import curses
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
    option = int(input("curses (0) or pygame (1)? "))
    if option == 0:
        from curses import wrapper
        wrapper(ncurses_ants)
    if option == 1:
        pygame_ants()
