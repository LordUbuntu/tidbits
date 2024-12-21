# Jacobus Burger (2022)
# I thought about exotic ways of doing a simple evenness test in python
from random import randint as random


def index_even(n):
    return ["Even", "Odd"][n % 2]


def recursive_even(n):
    if n == 0:
        return "Even"
    if n == 1 or n == -1:
        return "Odd"
    return recursive_even(n - 2)


def iterative_even(n):
    for i in range(0, n + 1, 2):
        if i == n:
            return "Even"
    return "Odd"


def membership_even(n):
    even_numbers = [i for i in range(0, n + 1, 2)]
    if n in even_numbers:
        return "Even"
    return "Odd"


def curry_even(n):
    # npm joke
    def is_odd(n):
        def is_even(n):
            return n % 2 == 0
        return is_even
    return "Even" if is_odd(n)(n) == True else "Odd"


# precondition: user must know if n is even and specify ahead of time
def insist_even(n, is_even):
    return is_even


def not_odd(n):
    if n % 2 != 1:
        return "Even"
    return "Odd"


def probably_even(n):
    if random(0, 1) == 0:
        return "Even"
    else:
        return "Odd"


def guess_even(n):
    return "Even"  # This will be right 50% of the time!
