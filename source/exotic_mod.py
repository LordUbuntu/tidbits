# Jacobus Burger (2022)
# I thought about exotic ways of doing a simple evenness test in python
# Might add more

def index_even(n):
    return ["Even", "Odd"][n % 2]


def recursive_even(n):
    if n == 0:
        return "Even"
    if n == 1 or n == -1:
        return "Odd"
    return recursive_even(n - 2)
