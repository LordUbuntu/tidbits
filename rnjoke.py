# Jacobus Burger (2024)
# I had a funny idea to make an RNG that selects a random digit of PI
#   using Python's builtin RNG to do so.
from math import pi
from random import choice


def rng():
    """ generates random numbers by randomly picking digits of pi """
    digits = [
        int(digit)
        if digit != '.' else 0
        for digit in str(pi)
    ]
    return choice(digits)


def randomness():
    """ returns a totally random number that can't be predicted! """
    return 13


if __name__ == '__main__':
    print(rng())
