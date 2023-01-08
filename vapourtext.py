#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   Code golf to print vapour-ware strings eg "h e l l o"
from random import randint as rnd


def vapourize(sentence):
    return ' '.join([*sentence])


def VAPOURIZE(sentence):
    return ' '.join([*sentence.upper()])


def random_vapourize(sentence):
    return ' '.join([char if rnd(0, 1) else char.lower() for char in sentence.upper()])

if __name__ == '__main__':
    sentence = input()
    print(vapourize(sentence))
    print(VAPOURIZE(sentence))
    print(random_vapourize(sentence))
