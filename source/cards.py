# Jacobus Burger (2022)
# Info:
#   A card game where you win if you pull an ace of clubs!


# each card and suit can be represented as an index and value
# EG: Ace of Clubs == (0, 0)
# Ace, 2, 3, 4, 5, 6, 7, 8, 9, J,  K,  Q
# 0,   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
cards = [card for card in range(13)]
# Club, Heart, Clover, Diamond
# 0,    1,     2,      3
suits = [suit for suit in range(4)]


def print_card(card, suit: int):
    string = ""

    # determine the card type
    if card == 0:
        string += "Ace "
    elif 1 <= card <= 8:
        string += f"{card[0] + 1} "
    elif card == 9:
        string += "Jack "
    elif card == 10:
        string += "Queen "
    elif card == 11:
        string += "King "
    else:
        string += "Aster "  # something's gone wrong

    # determine the card suit
    if suit == 0:
        string += "of Clubs"
    if suit == 1:
        string += "of Hearts"
    if suit == 2:
        string += "of Clovers"
    if suit == 3:
        string += "of Diamonds"
    else:
        string += "the King in Yellow"  #something's gone wrong

    return string


def game(draws: int):
    pass


if __name__ == '__main__':
    draws = int(input("How many times do you want to draw? "))
    game(draws)
