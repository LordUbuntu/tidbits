#!/bin/python3
# Jacobus Burger (2022)
# Info:
#   The famous Commodor 64 Basic program that generated a neat pattern
#   Done in python.
from random import choice
char = [r"\", r"/"]
while True:
    print(choice(char), end="")
