# Jacobus Burger (2025-09-08)
# In media they portray snakes speaking with protracted s'
#   like thisssss, maybe they do, but I think it would be fun
#   to write a quick string formatter for that.


def ssspeak(phrase: str) -> str:
    return phrase.replace('s', "ssss").replace('x', "sss")


if __name__ == "__main__":
    phrase = input()
    print(ssspeak(phrase))
