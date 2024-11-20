# Jacobus Burger (2022)
# Info:
#   A card game where you win if you pull an ace of clubs!
from random import choice


# direct representation
cards = [
    "Ace",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
    "Joker"
]
suits = ["Club", "Heart", "Clover", "Diamond"]


def get_card():
    return ' '.join([choice(cards), "of", choice(suits)])


def game(draws: int):
    answer = ' '.join([choice(cards), "of", choice(suits)])
    print("=== Winning Card is", answer, "===")
    for _ in range(draws):
        card = get_card()
        print("You got", card)
        if card == answer:
            print("You won!!")
            break
        else:
            print("Try again...")


if __name__ == '__main__':
    draws = int(input("How many times do you want to draw? "))
    game(draws)
