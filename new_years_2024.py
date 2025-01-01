# Jacobus Burger (2024->2025)
# This new years program prints ascii simulated fire using a similar
#   principle to the winter snowfall program `snow.py`. Inspired by
#   a desire to come on a year anew like a phoenix (🐦‍🔥) and
#   "keep that fire alive"
import os
from time import sleep
from collections import deque


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
