# Jacobus Burger (2024)
# I wondered if there was an algorithm to calculate if a number is 
#   geometrically symmetric with itself, effectively a geometric numeric
#   annagram while entertaining the idea with T.
# This was determined to be a matter of matching numbers of symmetric
#   opposites, splitting the number into two halves down its middle
#   (including its middle digit), and then reversing the second half
#   first in digit order, then replacing digits with their symmetric
#   opposites, and then finally comparing that with the first half for
#   a match.

# list of symmetric opposites
# notice that some numbers are their own symmetric opposites. This
# relation could be graphed into a FSA
sym = {
    0: 0,
    1: 1,
    2: 5,
    5: 2,
    6: 9,
    8: 8,
    9: 6
}


def cleave(n):
    """split a number into two numbers down the middle"""
    s = str(n)
    if len(s) % 2 == 0:
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
    else:
        a = s[:len(s) // 2 + 1]
        b = s[len(s) // 2:]
    return [int(a), int(b)]


def is_symmetric(n):
    a, b = 0, 0
    # cleave n into symmetric sides a and b
    # geometric reverse b
    # return comparison of a and b
    return a == b
