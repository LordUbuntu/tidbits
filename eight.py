# Jacobus Burger (2024)
# Magic eight ball on the command line!
from color50 import rgb, constants
from random import randint, choice

FORTUNE = [
    "It is certain",
    "It is in the cards",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful"
]


def eightball(question: str) -> str:
    color = rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    fortune = choice(FORTUNE)
    print("You asked {}".format(question))
    print("Eightball says:" + color + fortune + constants.RESET)


if __name__ == "__main__":
    question = input()
    eightball(question)
