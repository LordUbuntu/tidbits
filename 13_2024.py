# Jacobus Burger (2024-12-13)
# ... 12, 13 ...
# Prints multiples of 12, 13, and 12 and 13 with highlights
from time import sleep
from os import system, name
import termcolor


# this should really be a python default function at this point...
def clear(): system("cls" if name == "nt" else "clear")


def main():
    i = 0
    while True:
        if i % 12 == 0 or i % 13 == 0:
            print(termcolor.colored(i, "red", attrs=["blink"]))
        else:
            print(i)
        sleep(1)
        i += 1


if __name__ == "__main__":
    main()
