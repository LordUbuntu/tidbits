# Jacobus Burger (2023)
# Demonstration of the Church-Turing thesis as it relates to iteration.
# Any given loop can be expressed as a recursive function, and vice-versa


def rloop(i = 0, f, *args):
    if i <= 0:
        return
    f(args[0])
    return rloop(i - 1, f, *args[1:])


def iloop(i = 0, f, *args):
    while i > 0:
        f(args[0])
        args = args[1:]
