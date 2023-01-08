#!/bin/python3
# Jacobus Burger (2022)
# Info:
#   The famous Commodor 64 Basic program that generated a neat pattern
#   Done in python.
from random import choice


def print10(chars):
    while True:
        print(choice(chars), end="")


if __name__ == '__main__':
    chars = [char for char in input().split()]
    print10(chars)
