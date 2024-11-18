# Jacobus Burger (2024-10-30)
# A fun tradition I do every Halloween, like how "Grinch's Ultimatum" is
#   a tradition for Christmas.
# This year, the "Monster Mash" song inspired me to make a cute little
#   dance and lyrics thing for it from ascii
from time import sleep
from os import system, name
import termcolor


monster_mash = termcolor.colored("~monster mash~", "red", attrs=["reverse", "blink"])
graveyard_smash = termcolor.colored("~graveyard smash~", "red", attrs=["reverse"])
lyric = [
    "(It did the mash)",
    f"It did the {monster_mash}",
    "(A graveyard smash)",
    f"It was a {graveyard_smash}"
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


def main():
    while True:
        for a in range(4):
            for b in range(4):
                clear()
                print(f"{lyric[a]}\n\n{animation[b]}\n\n\nHappy Halloween 2024!")
                sleep(0.4)


if __name__ == "__main__":
    main()
