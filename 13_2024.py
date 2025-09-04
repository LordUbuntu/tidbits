# Jacobus Burger (2024-12-13)
# Prints multiples of 13
from time import sleep
from os import system, name
import termcolor


# this should really be a python default function at this point...
def clear(): system("cls" if name == "nt" else "clear")


def main():
    i = 0
    while True:
        if i % 13 == 0:
            print(termcolor.colored(i, "red"))
            sleep(0.5)
        i += 1


if __name__ == "__main__":
    main()
