#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   I wanted to draw a shape out of ASCII characters.
#   Enjoy!


def sign(symbol: str, height: int):
    for row in range(height):
        # create spaces on left
        for _ in range(height - row):
            print(" ", end="")
        # print symbol on row
        for _ in range(row + 1):
            print(" ", end=symbol)
        print()


sign(".", 4)
