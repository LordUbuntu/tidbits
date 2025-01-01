# Jacobus Burger (2024->2025)
# This new years program prints ascii simulated fire using a similar
#   principle to the winter snowfall program `snow.py`. Inspired by
#   a desire to come on a year anew like a phoenix (🐦‍🔥) and
#   "keep that fire alive"
# Next time I could do this with ncurses and have the characters move
#   asyncronously with variant colour and more.
import os
from time import sleep
from collections import deque
from random import randint


DELAY = 0.3  # number of seconds between each frame

width, height = os.get_terminal_size()
grid = deque([], 32)  # 32 rows max
heat = ["$", "@", "%", "&",
        "#", "*", "a", "?",
        "+", "~", "!", ";",
        "^", "'", ".", " "]


def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')


# I want this to run whether imported or called as a script
while True:
    # clear screen
    clear()
    print("\033[?25l")  # hide cursor with ANSI code

    # display fire from top to bottom
    display = ""
    for row in grid:
        display += "".join([heat[value] for value in row]) + "\n"
    display = display.strip("\n")
    print(display, end="")

    # insert a new layer of fire at the bottom (reason for using a queue)
    # I'll skip on the idea of a normal distribution of the flames (KISS)
    # I'll represent flame heat by a number
    row = []
    for _ in range(width):
        if randint(0, 1):
            row.append(0)  # values 0 through 7 are heat level of cinder
        else:
            row.append(-1) # values < 0 are ignored
    grid.append(row)  # put on bottom of screen

    # update past cinders by "cooling" them by 1 value
    for row in grid:
        for i in range(len(row)):
            if row[i] >= 0:
                row[i] += 1
            if row[i] == len(heat) - 1:
                row[i] = -1
    
    # pause until next frame
    sleep(DELAY)
