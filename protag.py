#!/bin/python3
# Jacobus Burger (2022)
# Info:
# Generates a description of a story protagonist randomly.
from random import choice

composure = [
    "adventurous",
    "angry",
    "anxious",
    "artistic",
    "bitter",
    "brave",
    "busy",
    "erroneous",
    "friendly",
    "funny",
    "generous",
    "greedy",
    "happy",
    "melancholic",
    "peaceful",
    "quarky",
    "spontaneous",
    "stalward",
    "strange",
    "vitriolic",
]

creature = [
    "balrog",
    "basilisk",
    "bee",
    "bird",
    "bottle of water",
    "calculus textbook",
    "cat",
    "computer",
    "dragon",
    "elf",
    "eraser with a face drawn on it",
    "flamingo",
    "flea",
    "flying tree",
    "gingerbread man",
    "human",
    "leopard",
    "pixar lamp",
    "planet",
    "quantum soup",
    "snake",
    "the color red",
    "tree",
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
    "python programmer",
    "roboticist",
    "quantum physicist",
    "pen pusher",
    "spearman",
    "sniper",
    "genius"
]

strength = [
    "twig",
    "sprig",
    "snake",
    "steel rod",
    "log",
    "statue",
    "collosus",
    "moutain",
    "TNT",
    "Atom bomb"
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
    "the world",
    "the number 42",
    "the light at the end of the tunnel",
    "a bird",
    "their long lost nickel",
    "the platonic forms",
    "a time travelling caveman"
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
