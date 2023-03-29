#!/bin/python3
# Jacobus Burger (2022)
# Info:
#   Classic rot13 encoder. I have an idea that the Voynich manuscript
#   is encoded using a repeatedly shifting rotating encoder or
#   some other dynamically shifting encoding but that's just an
#   opinion until proven otherwise.
from string import ascii_lowercase


# note: only takes strings with no spaces or any non-letter ascii
def rot13(data: str) -> str:
    return ''.join(ascii_lowercase[(i + 13) % 26] for i in map(ascii_lowercase.index, data.lower()))


if __name__ == '__main__':
    string = input()
    print(rot13(string))
