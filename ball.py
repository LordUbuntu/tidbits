# Jacobus Burger (2025-06-12)
# Random Ball in Terminal
import os
import random
from time import sleep


def clear():
    os.system("cls" if os.name == "nt" else "clear")

width, height = os.get_terminal_size()
BALL = "*"
TIMEOUT = 1


try:
    print('\033[?25l', end='')  # hide cursor
    while True:
        clear()
        x = random.randint(0, width)
        y = random.randint(0, height)
        # print preceding space (vertical)
        # note: this could be generalized for a TUI renderer
        print((' ' * width) * (y - 1))
        # print character line
        print((' ' * (x - 1)) + BALL + (' ' * (width - (x - 1))))
        # print remaining space (vertical)
        print(' ' * (height - (y - 1)))
        sleep(TIMEOUT)
except KeyboardInterrupt:
    print('\033[?25h', end='')  # reveal cursor again
    clear()
