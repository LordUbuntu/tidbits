# Jacobus Burger (2024-12-24)
# A quick and simple one to celebrate christmas (coming in a few minutes)
from time import sleep
from os import system, name
import termcolor


# this should really be a python default function at this point...
def clear(): system("cls" if name == "nt" else "clear")


def main():
    print(termcolor.colored("!MERRY CHRISTMAS!", "red", attrs=["blink", "reverse"]))


if __name__ == "__main__":
    main()
