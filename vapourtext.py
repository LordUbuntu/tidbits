#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   Code golf to print vapour-ware strings eg "h e l l o"
# TODO: merge into text effects library
from random import randint as rnd




def VaPoUrIzE(sentence):
    return ' '.join([sentence[i].upper() if i % 2 else sentence[i].lower() for i in range(len(sentence))])


def random_vapourize(sentence):
    return ' '.join([char if rnd(0, 1) else char.lower() for char in sentence.upper()])


if __name__ == '__main__':
    sentence = input()
    print(vapourize(sentence))
    print(VAPOURIZE(sentence))
    print(random_vapourize(sentence))
