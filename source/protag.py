#!/bin/python3
# Jacobus Burger (2022)
# Info:
# Generates a description of a story protagonist randomly.
from random import choice

composure = [
    "stalward",
    "anxious",
    "brave",
    "vitriolic",
    "angry",
    "greedy",
    "friendly",
    "generous"
]

creature = [
    "human",
    "cat",
    "bee",
    "bird",
    "snake",
    "computer"
]

skill = [
    "ninja",
    "wizard",
    "sewer worker",
    "astrofreighter",
    "hacker"
]

strength = [
    "slenderperson",
    "bodybuilder",
    "spinach-eater"
]

def describe():
    print(
        "A {} {} {} built like a {}".format(
            choice(composure),
            choice(creature),
            choice(skill),
            choice(strength)),
        end=' '
    )


if __name__ == '__main__':
    print("type [enter] to generate a description.")
    print("type [q] to quit!")
    while True:
        if input() == "q":
            exit(0)
        describe()
