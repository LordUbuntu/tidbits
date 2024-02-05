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
    matchboxes = []

# start the game of tic-tac-toe
board = [[' '] * 3 for i in range(3)]  # _, X, or O
running = True
move = 0
print(matchboxes, board)  # DEBUG
while running:
    # menace generates a new matchbox
    matchboxes.append([rand(0, 8) for i in range(9)])
    # menace goes first as O
    empty_tile_found = False
    while not empty_tile_found:
        O = matchboxes[move][rand(0, 8)]
        if board[O // 3][O % 3] == ' ':
            empty_tile_found = True
    move += 1
    # update board
    board[O // 3][O % 3] = 'O'
    # show board
    print_board(board)
    # check if all tiles are filled and end game
    # check if any lines are made and end game
        # update weights of MENACE based on win/loss
    # player goes next
    empty_tile_found = False
    while not empty_tile_found:
        try:
            X = int(input("""
            1|2|3
            -+-+-
            4|5|6
            -+-+-
            7|8|9
            """))
            X -= 1
        except:
            exit()
        else:
            if board[X // 3][X % 3] == ' ':
                empty_tile_found = True
    board[X // 3][X % 3] = 'X'


# overwrite matchbox memory
with open("matchboxes.json", "w") as file:
    json.dump(matchboxes, file)
