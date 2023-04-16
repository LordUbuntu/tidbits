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
    "Box Squat",
    "Bulgarian Split Squat",
    "Sumo Deadlift",
    "Romanian Deadlift",
]


def exercise():
    return ' '.join(
        [
            str(randint(1,5)),  # number of sets
            "by",
            str(randint(1,15)), # number of reps
            "of",
            choice(EXERCISES)   # exercise
        ]
    )


if __name__ == '__main__':
    for i in range(randint(1, 3)):
        print(exercise())
