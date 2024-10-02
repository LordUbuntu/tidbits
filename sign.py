#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   I wanted to draw shapes out of ASCII characters.
#   Enjoy!


def sign_pythagoras(char: str, height: int):
    for row in range(1, height + 1):
        print(char*row)
    print()


def sign_delta(char: str, height: int):
    for row in range(height):
        for _ in range(height - row):
            print(" ", end="")
        for _ in range(row + 1):
            print(" ", end=char)
        print()


def sign_del(char: str, height: str):
    for row in range(height):
        for _ in range(row + 1):
            print(" ", end="")
        for _ in range(height - row):
            print(" ", end=char)
        print()


def sign_chi(char: str, height: int):
    for row in range((height * 2) + 1):
        if row >= height and row < height + 1:
            for _ in range(2):
                print(f"{char*(height*2)}{char*2}")
        else:
            print(" "*height, end=f"{char*2}\n")
    print()


def sign_sq(char: str, height: int):
    for row in range(height):
        print(char * height)
    print()


def sign_disc(char: str, radius: int):
    from math import sin
    for row in range(radius + 1):
        print(" "*int(radius * sin(row)), end=f"{char}\n")


def sign_worm():
    print("""
               ##_
   ###        #
  #   #       #
##     #######
    """)


def sign_cross():
    print("""
  #
  #
#####
  #
  #
  #
  #
    """)


if __name__ == '__main__':
    print("pythagoras")
    sign_pythagoras("-", 3)
    print("delta")
    sign_delta(".", 5)
    print("chi")
    sign_chi("#", 3)
    print("sq")
    sign_sq("*", 5)
    print("zero")
    sign_disc("-", 3)
