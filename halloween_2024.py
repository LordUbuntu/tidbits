# Jacobus Burger (Oct 30, 2024)
# A fun tradition I do every Halloween, like how "Grinch's Ultimatum" is
#   a tradition for Christmas.
# This year, the "Monster Mash" song inspired me to make a cute little
#   dance and lyrics thing for it from ascii
from time import sleep
from os import system, name


lyrics = [
    "(It did the mash)",
    "It did the ~monster mash~",
    "(A graveyard smash)",
    "It was a ~graveyard smash~"
]

animation = [
    """
    <(._.<)
    """,
    """
    <(._.)>
    """,
    """
    (>._.)>
    """,
    """
    <(._.)>
    """
]


def clear():
    system("cls" if name == "nt" else "clear")
