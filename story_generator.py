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
    "hyperactive",
    "serendipitous",
    "eccentric",
    "stoic",
    "careful",
    "chaotic",
    "clumsy",
    "talented",
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
    "lamp",
    "planet",
    "quantum soup",
    "snake",
    "the color red",
    "tree",
    "painting",
    "don quixote",
    "horse",
    "fortress",
    "flower",
    "supercomputer",
    "calculator",
    "moth",
    "butterfly",
    "farmer",
    "computer virus",
    "teacup",
]

occupation = [
    "EVA Pilot",
    "astrofreighter",
    "astronaught",
    "astrophysicist",
    "boxer",
    "carpenter",
    "chocolatier",
    "genius",
    "hacker",
    "hole digger",
    "hole filler",
    "librarian",
    "linguist",
    "mathematician",
    "mecha mechanic",
    "neuromancer",
    "ninja",
    "pen pusher",
    "python programmer",
    "quantum physicist",
    "robot ethicist",
    "roboticist",
    "rubber duck debugger",
    "sewer worker",
    "snake charmer",
    "sniper",
    "spearman",
    "tea enthusiast",
    "time traveler",
    "wizard",
    "bioethicist",
    "geologist",
    "historian",
    "therapist",
    "conman",
    "author",
    "tea farmer",
    "goat milker",
    "hunter",
    "smith",
    "necromancer"
]

strength = [
    "Atom bomb",
    "TNT",
    "Collosus",
    "Log",
    "Moutain",
    "Snake",
    "Sprig",
    "Statue",
    "Steel rod",
    "Twig",
]

quest = [
    "a beehive",
    "a bird",
    "a building",
    "a cat",
    "a city",
    "a dark notion",
    "a friendly robot singing \"Hello World\"",
    "a hypothetical connundrum",
    "a logical paradox",
    "a long forgotten language",
    "a planet",
    "a serpent",
    "a time travelling caveman",
    "an ancient dragon",
    "magical sword",
    "monsieur ubu",
    "the collatz conjecture",
    "the cosmos",
    "the essence of lambda calculus",
    "the laundry",
    "the letter 'A'",
    "the light at the end of the tunnel",
    "the number 42",
    "the platonic forms",
    "the towers of hanoi",
    "the world",
    "their long lost nickel",
    "their long lost twin",
    "themselves",
]

def describe():
    print(
        "A {} {} working as a {} and built like a {} on a quest to save {}".format(
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
