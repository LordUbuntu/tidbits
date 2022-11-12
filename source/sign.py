#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   I wanted to draw a shape out of ASCII characters.
#   Enjoy!


def sign_delta(char: str, height: int):
    for row in range(height):
        # create spaces on left
        for _ in range(height - row):
            print(" ", end="")
        # print char on row
        for _ in range(row + 1):
            print(" ", end=char)
        print()


def sign_chi(char: str, height: int):
    for row in range((height * 2) + 1):
        # print horizontal, middle
        if row >= height and row < height + 1:
            for _ in range(2):
                print(f"{char*(height*2)}{char*2}")
        # print vertical, ends
        else:
            print(" "*height, end=f"{char*2}\n")
    print()


def sign_sq(char: str, height: int):
    for row in range(height):
        print(char * height)
    print()


if __name__ == '__main__':
    print("delta")
    sign_delta(".", 5)
    print("chi")
    sign_chi("#", 3)
    print("sq")
    sign_sq("*", 5)
