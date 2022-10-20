#!/bin/python3
# Jacobus Burger (2022)
# Info:
#   Classic rot13 encoder. I have an idea that the Voynich manuscript
#   is encoded using a repeatedly shifting rotating encoder or
#   some other dynamically shifting encoding but that's just an
#   opinion until proven otherwise.

def rot13(data: str) -> str:
    result = []
    for char in data.upper():
        result.append( chr(((ord(char) - 65 + 13) % 25) + 65) )
    return result
