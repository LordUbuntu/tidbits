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
    "King"
]
suits = ["Club", "Heart", "Clover", "Diamond"]


def show_card(card, suit: int):
    string = ""
    # determine the card type
    if card == 0:
        string += "Ace "
    elif 1 <= card <= 8:
        string += f"{card + 1} "
    elif card == 9:
        string += "Jack "
    elif card == 10:
        string += "Queen "
    elif card == 11:
        string += "King "
    # determine the card suit
    if suit == 0:
        string += "of Clubs"
    if suit == 1:
        string += "of Hearts"
    if suit == 2:
        string += "of Clovers"
    if suit == 3:
        string += "of Diamonds"
    return string


def game(draws: int):
    guess = [randint(0, len(cards) - 1), randint(0, len(suits) - 1)]  # [card, suit]
    for _ in range(draws):
        card, suit = choice(cards), choice(suits)
        print(show_card(card, suit))
        if card == guess[0] and suit == guess[1]:
            print("Congatrulaions! You got the winning card!\n\n")
            quit()
    else:
        print("You lose!")


if __name__ == '__main__':
    draws = int(input("How many times do you want to draw? "))
    game(draws)
