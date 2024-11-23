#!/bin/python3
# Jacobus Burger (2022)
# Info:
#   Classic rot13 encoder. I have an idea that the Voynich manuscript
#   is encoded using a repeatedly shifting rotating encoder or
#   some other dynamically shifting encoding but that's just an
#   opinion until proven otherwise.
from random import randint as random
from string import ascii_lowercase


# note: only takes strings with no spaces or any non-letter ascii
def rot13(s: str) -> str:
    string = map(ascii_lowercase.index, s.lower())
    return ''.join(ascii_lowercase[(i + 13) % 26] for i in string)


def rot_rand(s: str) -> str:
    N = random(1, 100)
    string = map(ascii_lowercase.index, s.lower())
    return ''.join(ascii_lowercase[(i + N) % 26] for i in string)


def rot_chaos(s: str) -> str:
    string = map(ascii_lowercase.index, s.lower())
    return ''.join(ascii_lowercase[(i + random(1, 100)) % 26] for i in string)


def rot(data: str, n: int = 13) -> str:
    return ''.join(ascii_lowercase[(i + n) % 26] for i in map(ascii_lowercase.index, data.lower()))


if __name__ == '__main__':
    string = input().strip()
    print("note: whitespaces removed")
    print("ROT13: {}".format(rot13(string)))
    print("ROTN: {}".format(rotN(string)))
