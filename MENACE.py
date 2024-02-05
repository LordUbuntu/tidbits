# Jacobus Burger (2024)
# MENACE (short for Matchbox Educable Noughts and Crosses Engine) was
#   an early convolutional neural network. This program is a replication
#   of the basic principle of MENACE in Python 3.
# see: https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
from os.path import exists
from random import randint as rand
import json  # for persistent memory


def print_board(board):
    for i in range(len(board) - 1):
        print('|'.join(board[i]))
        print("-+-+-")
    print('|'.join(board[len(board) - 1]))

# check if memory exists and load it in
if exists("matchboxes.json"):
    with open("matchboxes.json", "r") as file:
        matchboxes = json.load(file)
# otherwise use default empty head
else:
    matchboxes = [[rand(0, 8) for i in range(9)]]

# start the game of tic-tac-toe
board = [[' '] * 3 for i in range(3)]  # _, X, or O
running = True
move = 0
print(matchboxes, board)  # DEBUG
while running:
    # menace goes first as O
    O = matchboxes[move][rand(0, 8)]
    move += 1
    # update board
    board[O // 3][O % 3] = 'O'
    # show board
    print_board(board)
    # player goes next
    break


# overwrite matchbox memory
with open("matchboxes.json", "w") as file:
    json.dump(matchboxes, file)
