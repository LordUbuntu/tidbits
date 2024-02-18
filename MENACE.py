# Jacobus Burger (2024)
# MENACE (short for Matchbox Educable Noughts and Crosses Engine) was
#   an early convolutional neural network. This program is a replication
#   of the basic principle of MENACE in Python 3.
# see: https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
from time import sleep
from itertools import chain
from os.path import exists
from os import system, name
from random import randint as rand
from random import sample, choice, choices
import json  # for persistent memory


DELAY = 0.5  # number of seconds to wait before displaying MENACE's move


REWARD = 2
TIE = 1
PUNISH = 1


NO_ONE = 0
MENACE = 1
PLAYER = 2
CHAR_MAP = {
    NO_ONE: ' ',
    MENACE: 'O',
    PLAYER: 'X',
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
# NOTE: interestingly, don't need to remember move order or number at all!


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def board_string(board_state):
    return ''.join(CHAR_MAP[n] for n in board_state)


def show_board(board_state):
    board = board_string(board_state)
    for i in range(2):
        print('|'.join(board[i * 3 : i * 3 + 3]))
        print("-+-+-")
    print('|'.join(board[6:9]))


def load_memory():
    # load memory if it exists
    if exists("matchboxes.json"):
        with open("matchboxes.json", "r") as file:
            matchboxes = json.load(file)
    # otherwise use default empty head
    else:
        matchboxes = { "         ": [0, 1, 2, 3, 4, 5, 6, 7, 8] }
    return matchboxes


def save_memory(matchboxes):
    with open("matchboxes.json", "w") as file:
        json.dump(matchboxes, file)


def winner(board_state):
    # I love snake lang 🐍
    for i in range(3):
        # check for rows
        if all(state == MENACE for state in board_state[i * 3 : i * 3 + 3]):
            return MENACE
        if all(state == PLAYER for state in board_state[i * 3 : i * 3 + 3]):
            return PLAYER
        # check for columns
        if all(state == MENACE for state in board_state[i :: 3]):
            return MENACE
        if all(state == PLAYER for state in board_state[i :: 3]):
            return PLAYER
        # check for diagonals
        if all(state == MENACE for state in board_state[i :: 4]):
            return MENACE
        if all(state == PLAYER for state in board_state[i :: 4]):
            return PLAYER
    return NO_ONE



def main():
    # retrieve any memory if it exists
    matchboxes = load_memory()
    # start the game
    game_running = True
    while game_running:
        # MENACE takes its turn

        # show board state before
        clear()
        show_board(board_state)
        sleep(DELAY)
        # generate a matchbox if it doesn't exist for this board state
        if board_string(board_state) not in matchboxes:
            matchboxes.update({
                board_string(board_state): [*open_tiles]
            })
        # menace picks a bead from the matchbox for the current state
        # and action is recorded for later backpropogation
        bead = choice(matchboxes[board_string(board_state)])
        actions.append((bead, board_string(board_state)))
        # remove from open_tiles
        open_tiles.remove(bead)
        # menace updates board state with its move
        board_state[bead] = MENACE

        # Player takes their turn

        # validate and retrieve player input
        # (must be int and in open_tiles)
        valid_input = False
        while not valid_input:
            # display board state after MENACE move before player move
            clear()
            show_board(board_state)
            try:
                X = int(input("""
                1|2|3
                -+-+-
                4|5|6
                -+-+-
                7|8|9
                """))
                X -= 1  # correct offset
            except:
                exit()
            if X not in open_tiles:
                continue
            else:
                valid_input = True
        # remove from open_tiles
        open_tiles.remove(X)
        # update board state with player move
        board_state[X] = PLAYER

        # Check for winners


        # show board state before winner decided or not
        clear()
        show_board(board_state)
        # determine winners and train MENACE based on that
        win = winner(board_state)
        # reward MENACE for winning (more of the same beads)
        if win == MENACE:
            # add REWARD beads in the states that realized the win
            for bead, state in actions:
                for _ in range(REWARD):
                    matchboxes[state].append(bead)
            # show MENACE win
            print("===== MENACE WINS =====")
            break
        # punish MENACE for losing (remove beads from matchboxes)
        elif win == PLAYER:
            # remove PUNISH beads in the states that realized the loss
            for bead, state in actions:
                for _ in range(PUNISH):
                    matchboxes[state].remove(bead)
            # show player win
            print("===== YOU WIN =====")
            break
        # add a random bead for a tie
        elif len(open_tiles) <= 2:
            # add TIE beads to everything anyways
            for bead, state in actions:
                for _ in range(TIE):
                    matchboxes[state].append(bead)
            # show tie
            print("===== TIE =====")
            break
    # store any learned memory
    save_memory(matchboxes)



if __name__ == '__main__':
    main()
