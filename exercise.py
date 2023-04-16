# Jacobus Burger (2023)
# Info:
#   Randomly reccomend some exercises in a routine with random numbers.
#   This may become a ChatGPT + Exercise Finder + React application
# See:
#   https://whitecoattrainer.com/blog/best-exercises
from random import choice, randint


EXERCISES = [
    # legs
    "Pistols",
]


def exercise():
    return ' '.join(
        [
            randint(1,5),      # number of sets
            "by",
            randint(1,15),       # number of reps
            "of",
            choice(EXERCISES)   # exercise
        ]
    )
