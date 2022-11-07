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
    "generous",
    "funny",
    "busy",
    "happy"
]

creature = [
    "human",
    "cat",
    "bee",
    "bird",
    "snake",
    "computer",
    "flamingo",
    "flea",
    "tree",
    "dragon"
]

occupation = [
    "ninja",
    "wizard",
    "sewer worker",
    "astrofreighter",
    "hacker",
    "carpenter",
    "mathematician",
    "boxer",
    "time traveler",
    "mecha mechanic",
    "EVA Pilot",
    "astronaught",
    "linguist",
    "robot ethicist",
    "python programmer"
]

strength = [
    "twig",
    "serpent",
    "rebar",
    "slenderman",
    "log",
    "statue",
    "collosus",
    "moutain"
]

quest = [
    "themselves",
    "an ancient dragon",
    "a city",
    "a building",
    "a serpent",
    "a beehive",
    "the cosmos",
    "monsieur ubu",
    "the towers of hanoi",
    "a planet",
    "a long forgotten language",
    "a friendly robot singing \"Hello World\"",
    "the collatz conjecture",
    "the world"
]

def describe():
    print(
        "A {} {} {} built like a {}, on a quest to save {}".format(
            choice(composure),
            choice(creature),
            choice(occupation),
            choice(strength),
            choice(quest)
        ),
        end=' '
    )


if __name__ == '__main__':
    print("type [enter] to generate a description.")
    print("type [q] to quit!")
    while True:
        if input() == "q":
            exit(0)
        describe()
