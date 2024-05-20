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


def cleave(n):
    """split a number into two numbers down the middle including the overlapping middle digit in both if its length is odd"""
    s = str(n)
    if len(s) % 2 == 0:
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
    else:
        a = s[:len(s) // 2 + 1]
        b = s[len(s) // 2:]
    return [int(a), int(b)]


# list of symmetric opposites
# notice that some numbers are their own symmetric opposites. This
# relation could be graphed into a FSA
sym_opp = {
    0: 0,
    1: 1,
    2: 5,
    5: 2,
    6: 9,
    8: 8,
    9: 6
}
def geometric_reverse(n):
    """reverse a number after converting its digits to their geometric opposites"""
    ds = [int(d) for d in str(n)]
    # substitute digits with their symmetric opposite
    for i in range(len(ds)):
        if ds[i] in sym_opp:
            ds[i] = sym_opp[ds[i]]
    # reverse the order of the digits
    ds.reverse()
    # return the geometric reversed number
    return int(''.join(map(str, ds)))


def is_symmetric(n):
    # cleave n into symmetric sides a and b
    a, b = cleave(n)
    # geometric reverse b
    b = geometric_reverse(b)
    # return comparison of a and b
    return a == b
