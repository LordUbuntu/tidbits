# Jacobus Burger (2025-06-12)
# Random Ball in Terminal
import os
import random
from time import sleep


def clear():
    os.system("cls" if os.name == "nt" else "clear")

width, height = os.get_terminal_size()
CHARACTER = "*"
TIMEOUT = 1


while True:
    clear()
    x = random.randint(0, width)
    y = random.randint(0, height)
    # print preceding space (vertical)
    # note: this could be generalized for a TUI renderer
    print((' ' * width) * (y - 1))
    # print character line
    print((' ' * (x - 1)) + CHARACTER + (' ' * (width - (x - 1))))
    # print remaining space (vertical)
    print(' ' * (height - (y - 1)))
    sleep(TIMEOUT)
