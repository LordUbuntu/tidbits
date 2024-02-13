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


CHAR_MAP = {
    0: ' ',
    1: 'O',
    2: 'X',
}
open_tiles = [*range(9)]  # tiles that can still be selected from
board_state = [0] * 9
actions = []    # A list of tuples to remember which beads were chosen
                #   from which board state. Ephemeral, lifetime is the
                #   span of the current game only.
                # (bead_number, board_state)
# MENACE memory, the matchboxes.
#   Chooses a random bead based on board state.
#   Each bead is a number representing a possible tile, 9 choices are
#   generated based on what tiles are open, basically just a range of all
#   open spaces on novel board states
matchboxes = {
    "         ": [0, 1, 2, 3, 4, 5, 6, 7, 8],
}


def board_string(board_state):
    return ''.join(CHAR_MAP[n] for n in board_state)

def show_board(board_state):
    board = board_string(board_state)
    for i in range(2):
        print('|'.join(board[i * 3 : i * 3 + 3]))
        print("-+-+-")
    print('|'.join(board[6:9]))





print(open_tiles, board_state, actions, matchboxes)
show_board(board_state)
exit()



# FIXME:
def load_memory():
    # load memory if it exists
    if exists("matchboxes.json"):
        with open("matchboxes.json", "r") as file:
            matchboxes = json.load(file)
    # otherwise use default empty head
    else:
        matchboxes = {
            # all tiles possible to start
            tuple(board_state): list(range(9)),
        }
    return matchboxes


# FIXME:
def save_memory(matchboxes):
    with open("matchboxes.json", "w") as file:
        json.dump(matchboxes, file)



# TODO:
# - MENACE picks a move
# - update open_tiles, board_state, actions, and generate a new element in boxes that
# excludes occupied tiles (generate from open_tiles as many elements as len of
# open_tiles)
# - check for wins, ties, or losses
#   - update menace weights based on actions and outcome
# - while player input
#   - clear screen
#   - display board
#   - get input until valid


print("tiles, board, actions, matchboxes")
print(open_tiles, board_state, actions, matchboxes)
show_board(board_state)


exit()
