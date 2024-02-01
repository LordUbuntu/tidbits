# Jacobus Burger (2024)
# MENACE (short for Matchbox Educable Noughts and Crosses Engine) was
#   an early convolutional neural network. This program is a replication
#   of the basic principle of MENACE in Python 3.
# see: https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
from random import randint as rand
import json  # for persistent memory

# check if memory exists and load it in
# otherwise use default empty head
matchboxes = [[rand(0, 8) for i in range(9)]]

# start the game of tic-tac-toe
    # menace goes first as O
