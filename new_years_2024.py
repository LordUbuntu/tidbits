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


DELAY = 0.3  # number of seconds between each frame

grid = deque([], 8)  # 16 rows maximum
width, height = os.get_terminal_size()
flame = ["#", "@", "&", "?", "-", "^", "'", " "]


def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')


# I want this to run whether imported or called as a script
while True:
    # clear screen
    # add a row on the back of the grid queue (bottom of display)
    #   in that row, add elements in a normal (bell curve) distribution
    #   across the terminal width (more likely in middle than edges)
    # iterate through each row
    #   update "pixel" to be "colder" as it gets higher
    # pause until next frame
    sleep(DELAY)
