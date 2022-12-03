#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   Code golf to print vapour-ware strings eg "h e l l o"

def vapourize(sentence):
    return " ".join([*sentence])


if __name__ == '__main__':
    sentence = input()
    print(vapourize(sentence))
