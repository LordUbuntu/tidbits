# Jacobus Burger (2023)
# Just for fun, based on a video from Engineer Man
import os
import random
from time import sleep

DENSITY = 5
DELAY = 0.3

flakes = ['λ', '•', '.', '❆', '❅', '❄', '*']
width, height = os.get_terminal_size()
# initialize display to all empty characters
grid = [[' '] * width for _ in range(height)]


while True:
    # draw grid
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[?25l')  # ANSI clear cursor code
    display = ''
    for row in grid:
        display += ''.join(row) + '\n'
    display = display.strip('\n')
    print(display, end='')

    # scroll everything down once
    row = []
    for _ in range(width):
        if random.random() < DENSITY / 100:
            row.append(random.choice(flakes))
        else:
            row.append(' ')
    grid.insert(0, row)
    grid.pop()

    # wait
    sleep(DELAY)
