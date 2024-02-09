# Jacobus Burger (2024)
# MENACE (short for Matchbox Educable Noughts and Crosses Engine) was
#   an early convolutional neural network. This program is a replication
#   of the basic principle of MENACE in Python 3.
# see: https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
from itertools import chain
from os.path import exists
from random import randint as rand
from random import sample, choice, choices
import json  # for persistent memory


# TODO: update the way menace stores and selects data
# - a dictionary with each board state as a string, adding new ones when encountered
# - selecting beads and remembering which matchbox they're in, so that the same colour can be added or removed based on win/lose

open_tiles = {*range(9)}  # tiles that can still be selected from
board_state = [0] * 9
actions = []    # A list of tuples to remember which beads were chosen
                #   from which board state. Ephemeral, lifetime is the
                #   span of the current game only.
                # (bead_number, board_state)
# MENACE memory, the matchboxes.
#   Chooses a random bead based on board state.
#   Each bead is a number representing a possible tile, 9 choices are
#   generated based on what tiles are open.
# tuple: list because I want to remember board state correctly
boxes = {
    # how each box is generated on each new state
    tuple(board_state): choices(board_state, k=9),
}

print(open_tiles, board_state, actions, boxes)




def print_board(board):
    for i in range(len(board) - 1):
        print('|'.join(board[i]))
        print("-+-+-")
    print('|'.join(board[len(board) - 1]))


def end_game():
    # overwrite matchbox memory
    with open("matchboxes.json", "w") as file:
        json.dump(matchboxes, file)
    # stop program
    exit()


    
def winner(gamestate):
    # if no line, return 0
    # if X line, return 1
    # if O line, return 2
    # for each row
    for i in range(3):
        # I love snake lang 🐍
        # check for a row line
        if all(state == 1 for state in gamestate[i * 3 : i * 3 + 3]):
            return 1
        if all(state == 2 for state in gamestate[i * 3 : i * 3 + 3]):
            return 2
        # check for a column line
        if all(state == 1 for state in gamestate[i :: 3]):
            return 1
        if all(state == 2 for state in gamestate[i :: 3]):
            return 2
        # check for a diagonal line
        if all(state == 1 for state in gamestate[i :: 4]):
            return 1
        if all(state == 2 for state in gamestate[i :: 4]):
            return 2
    return 0



# load memory if it exists
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
while running:
    # check if all tiles are filled and end game
    if ''.join(chain.from_iterable(board)).count(' ') <= 1:
        print("= = = TIE = = =")
        end_game()
    # menace generates a new matchbox
    if move >= len(matchboxes):
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
    # check for wins
    # winner()
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
            end_game()
        else:
            if board[X // 3][X % 3] == ' ':
                empty_tile_found = True
    board[X // 3][X % 3] = 'X'


