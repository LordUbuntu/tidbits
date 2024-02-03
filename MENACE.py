# Jacobus Burger (2024)
# MENACE (short for Matchbox Educable Noughts and Crosses Engine) was
#   an early convolutional neural network. This program is a replication
#   of the basic principle of MENACE in Python 3.
# see: https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
from os.path import exists
from random import randint as rand
import json  # for persistent memory

# check if memory exists and load it in
if exists("matchboxes.json"):
    with open("matchboxes.json", "r") as file:
        matchboxes = json.load(file)
# otherwise use default empty head
else:
    matchboxes = [[rand(0, 8) for i in range(9)]]

# start the game of tic-tac-toe
running = True
move = 0
while running:
    # menace goes first as O
    # update board
    # player goes next


# overwrite matchbox memory
with open("matchboxes.json", "w") as file:
    json.dump(matchboxes, file)

print(matchboxes)
