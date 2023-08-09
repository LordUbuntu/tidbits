# Jacobus Burger (2023)
# The game of Tic Tac Toe on CLI
# I felt this wasn't sufficient on its own to justify a repository.
from os import system, name


def display(gamestate):
    system("cls" if name == "nt" else "clear")
    for i in range(3):
        print('|'.join(map(
            lambda item: 'X' if item == 1 else
                         'O' if item == 2 else
                         ' ',
            gamestate[i * 3 : i * 3 + 3])))
        print("-+-+-" if i != 2 else "\n\n")
    print("REMEMBER\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")
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
        if all(state == 2 for state in gamestate[i :: 4]):
            return 2
    return 0


def main():
    gamestate = [0] * 9
    while True:
        # update screen
        display(gamestate)
        # check who won and announce it
        outcome = winner(gamestate)
        if outcome == 1:
            print("X WINS!!!\n\n")
            break
        if outcome == 2:
            print("O WINS!!!\n\n")
            break
        # get player move and set tile to X if open (otherwise skip turn)
        X = int(input("Where should X go? "))
        gamestate[X - 1] = 1 if gamestate[X - 1] == 0 else gamestate[X - 1]
        # select first open tile and set as enemy O
        O = next(filter(lambda v: v[1] != 1 and v[1] != 2, enumerate(gamestate)))[0]
        gamestate[O] = 2


if __name__ == '__main__':
    main()
