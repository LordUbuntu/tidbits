#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   I wanted to draw a shape out of ASCII characters.
#   Enjoy!


def sign_delta(symbol: str, height: int):
    for row in range(height):
        # create spaces on left
        for _ in range(height - row):
            print(" ", end="")
        # print symbol on row
        for _ in range(row + 1):
            print(" ", end=symbol)
        print()


def sign_chi(symbol: str, height: int):
    for row in range((height * 2) + 1):
        # print horizontal, middle
        if row >= height and row < height + 1:
            for _ in range(2):
                print(f"{symbol*(height*2)}{symbol*2}")
        # print vertical, ends
        else:
            print(" "*height, end=f"{symbol*2}\n")
    print()



if __name__ == '__main__':
    print("delta")
    sign_delta(".", 5)
    print("chi")
    sign_chi("#", 3)
