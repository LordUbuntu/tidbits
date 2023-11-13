# Jacobus Burger (2023)
# A demo of Langton's Ants


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
    import pygame

    # define data
    SCREEN_DIMENSION = (512,512)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    TILES = 16  # tiles^2 == total tiles
    tile_data = {
        # (x,y): symbol
        (0, 0): SYM2,
        (2, 3): SYM3,
    }
    ant_position = [TILES // 2, TILES // 2]
    move = [1, 0]

    # initialize pygame
    pygame.init()
    pygame.time.Clock().tick(1)  # fps
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

    # draw a grid of tiles with colors based on tile_data
    #   scale refers to how far we zoom out.
    #   scale == 1 is a 16x16 grid
    #   scale == 2 is a 32x32 grid
    #   etc.
    def draw_grid(tile_data, tiles: int = 1):
        tile_size = SCREEN_DIMENSION[0] // tiles
        for i in range(tiles):
            for j in range(tiles):
                pygame.draw.rect(
                    screen,
                    tile_color(tile_data.get((i,j))),
                    (i * tile_size, j * tile_size, tile_size * tiles, tile_size * tiles),
                    0)
                if tiles < 64:
                    pygame.draw.rect(
                        screen,
                        BLACK,
                        (i * tile_size, j * tile_size, tile_size * tiles, tile_size * tiles),
                        1)

    # run
    running = True
    while running:
        # deal with state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        # get current character
        symbol = tile_data.get((ant_position[0], ant_position[1]))
        if symbol is None:
            symbol = SYM1
        # update state of automata
        symbol, move = next_state(symbol, move)
        # update screen
        draw_grid(tile_data, TILES)
        pygame.display.flip()
        # move to next position
        ant_position = [
            (ant_position[0] + move[0]) % TILES,
            (ant_position[1] + move[1]) % TILES,
        ]
        print(symbol, move, ant_position, tile_data)
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
