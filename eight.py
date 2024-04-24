# Jacobus Burger (2024)
# Magic eight ball on the command line!
# TODO: make into a package
from color50 import rgb, constants
from random import randint, choice
from sys import argv

FORTUNE = [
    "It is certain",
    "It is in the cards",
    "It's in the game",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Concentrate and ask again",
    "Did not hear, ask again",
    "Don't count on it",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
    "Not today"
]


def eightball(question: str) -> str:
    color = rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    fortune = choice(FORTUNE)
    print("You asked {}...".format(question))
    print(color + fortune + constants.RESET)


if __name__ == "__main__":
    question = ' '.join(argv[1:])
    eightball(question)
