# Jacobus Burger (2024-09-12)
# generates a string of random words of a random length from a text file
# inspired by oracles, a fascination with procedural generation, and terry davis
from sys import argv
from random import choice, randint


if len(argv) < 2:
    print("Need a file!")
    exit()
with open(argv[1], 'r') as file:
    words = [
        word for word in line
        line for line in file.readlines()
    ]
    for _ in range(randint(1, 50)):
        print(choice(words), end='')
print("")
