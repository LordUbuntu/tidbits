#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   A simple simulation of craps (some dice rolling game).
from random import choice

roll_names = {
    (1, 1): "snake eyes 🐍",
    (1, 2): "ace deuce 🂡🂡",
    (2, 2): "hard four",
    (1, 3): "easy four",
    (2, 3): "fever five 🕺",
    (3, 3): "hard six",
    (1, 4): "fever five 🕺",
    (2, 4): "easy six",
    (3, 4): "natural 🦉",
    (4, 4): "hard eight",
    (1, 5): "easy six",
    (2, 5): "natural 🦉",
    (3, 5): "easy eight",
    (4, 5): "nine",
    (5, 5): "hard ten",
    (1, 6): "natural 🦉",
    (2, 6): "easy eight",
    (3, 6): "nine",
    (4, 6): "easy ten",
    (5, 6): "yo 🤩",
    (6, 6): "boxcars 🚂"
}
rolls = [
    (i, j)
    for i in range(1, 7)
    for j in range(1, 7)
]


def chance():
    roll = choice(rolls)
    if roll in roll_names:
        print(roll_names[roll])
    else:
        print("rolled a {} and {}".format(roll[0], roll[1]))


if __name__ == '__main__':
    number_of_rolls = int(input("how many rolls? "))
    for _ in range(number_of_rolls):
        chance()
