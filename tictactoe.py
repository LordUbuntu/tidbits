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


def main():
    while True:
        # update screen
        # get user input
        # get enemy input
        # check for winners
            # announce winners and end
