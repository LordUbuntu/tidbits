# Jacobus Burger (2024)
# I had a funny idea to make an RNG that selects a random digit of PI
#   using Python's builtin RNG to do so.
from math import pi
from random import choice


def rng():
    digits = [
        int(digit)
        if digit != '.' else 0
        for digit in str(pi)
    ]
    return choice(digits)


if __name__ == '__main__':
    print(rng())
