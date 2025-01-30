# Jacobus
# Burger
# (2024-08-03)
# Desc:
#   I was inspired by the esoteric beauty when visiting SFU with the TWU
#   research lab teams for an outing. Decided to make this cute little
#   animated banner to comemorate.
from time import sleep
from os import name, system


def clear():
    system("cls" if name == "nt" else "clear")


banner = [
        """
 ____  _____ _   _
/ ___||  ___| | | |
\___ \| |_  | | | |
 ___) |  _| | |_| |
|____/|_|    \___/


        """,
        """
 ____  _____ _   _
/ ___||  ___| | | |
\___ \| |_  | | | |
 ___) |  _| | |_| |
|____/|_|    \___/

Home of SciFi Brutalist Architecture
        """,
        """
 ____  _____ _   _
/ ___||  ___| | | |
\___ \| |_  | | | |
 ___) |  _| | |_| |
|____/|_|    \___/

Home of SciFi Brutalist Architecture
(and lucky golden koi fish)
        """,
]


while True:
    clear()
    print(banner[0])
    sleep(1)
    clear()
    print(banner[1])
    sleep(1)
