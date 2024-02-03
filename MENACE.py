# Jacobus Burger (2024)
# MENACE (short for Matchbox Educable Noughts and Crosses Engine) was
#   an early convolutional neural network. This program is a replication
#   of the basic principle of MENACE in Python 3.
# see: https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
from os.path import exists
from random import randint as rand
import json  # for persistent memory


def print_board(board):
    for row in board:
        print('|'.join(row))
        print("-+-+-")

# check if memory exists and load it in
if exists("matchboxes.json"):
    with open("matchboxes.json", "r") as file:
        matchboxes = json.load(file)
# otherwise use default empty head
else:
    matchboxes = [[rand(0, 8) for i in range(9)]]

# start the game of tic-tac-toe
board = ["   ", "   ", "   "]  # _, X, or O
running = True
move = 0
print(matchboxes, board)  # DEBUG
while running:
    # show board
    print_board(board)
    # menace goes first as O
    O = matchboxes[move][rand(0, 8)]
    move += 1
    # update board
    board[O] = 'O'
    print_board(board)
    # player goes next


# overwrite matchbox memory
with open("matchboxes.json", "w") as file:
    json.dump(matchboxes, file)
