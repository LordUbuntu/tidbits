# Jacobus Burger (2025)
# An ascii animation of the sun, because today is a nice sunny day
import os
from time import sleep


sun = [
    """

       \\|/
       -O-
       /|\\

    """,
    """
      \\ | /
       \\|/
     ---O---
       /|\\
      / | \\
    """,
]


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    while True:
        for i in range(2):
            clear()
            print(sun[i])
            sleep(1)
