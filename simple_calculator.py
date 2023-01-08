#!/bin/python3.9
# Created by Jacobus Burger (2022)
#
# Info:
#   This is a newer simpler calculator I wrote really quickly
#   that uses Python's `eval` function to do the math.
key = ""
while True:
    key = input("expr (Q to quit): ")
    if key == "Q":
        quit()
    print(eval(key))
