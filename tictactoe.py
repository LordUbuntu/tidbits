# Jacobus Burger (2023)
# The game of Tic Tac Toe on CLI
# I felt this wasn't sufficient on its own to justify a repository.
from os import system, name


def display(gamestate):
    system("cls" if os.name == "nt" else "clear")
    for i in range(3):
        print('|'.join(map(
            lambda item: 'X' if item == 1 else
                         'O' if item == 2 else
                         ' ',
            gamestate[i * 3 : i * 3 + 3])))
        print("-+-+-" if i != 2 else "\n\n")
    print("""
    REMEMBER
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)
    print("\n\n")


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
        for all(state == 2 for state in gamestate[i :: 4]):
            return 2
    return 0


def main():
    gamestate = [0] * 9
    while True:
        # update screen
        display(gamestate)
        # get user input
        X = int(input("Where should X go? "))
        # get enemy input
        O = bot_move(gamestate)
        # check for winners
        winner(gamestate)
