# Jacobus Burger (2025-06-12)
# Random Ball in Terminal
import keyboard  # dependency
import os
import random
from time import sleep



def clear():
    os.system("cls" if os.name == "nt" else "clear")

width, height = os.get_terminal_size()
screen = [' ' * width] * height
PONG = "*"
TIMEOUT = 1


try:
    print('\033[?25l', end='')  # hide cursor
    while True:
        # refresh screen
        clear()

        # update ball position

        # update paddle position from input

        # display screen
        for h in range(height):
            print(screen[h])

        # wait for next step
        sleep(TIMEOUT)
except KeyboardInterrupt:
    print('\033[?25h', end='')  # reveal cursor again
    clear()
