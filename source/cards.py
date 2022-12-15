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


def game(draws: int):
    pass


if __name__ == '__main__':
    draws = int(input("How many times do you want to draw? "))
    game(draws)
