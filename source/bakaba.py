#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   I had a shower thought about triangular repeating words like
#   bakaba, bakakakaba, etc, maintaining some symmetry no matter how
#   long it might be. I wondered if there was an algorithm to accompish
#   this dumb passing thought.
#
#   here is my attempt at that.


def bakaba(repetitions, string):
    ka = string[2 : len(string) - 2]
    return string[:2] + ka * repetitions + string[len(string) - 2 :]


if __name__ == "__main__":
    while True:
        string = input("what string like 'bakaba' do you want to repeat? ")
        repetitions = int(input("how many times should the middle repeat? "))
        print(bakaba(repetitions, string))
