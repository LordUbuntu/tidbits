# Jacobus Burger (2023)
# Info:
#   Randomly reccomend some exercises in a routine with random numbers.
#   This may become a ChatGPT + Exercise Finder + React application
# See:
#   https://whitecoattrainer.com/blog/best-exercises
from random import choice, randint


# TODO:
# - add exercises besides bodyweight
# - add drop sets and other types of sets
EXERCISES = [
    # Legs
    "Pistol Squats",
    "Bulgarian Split Squat",
    "Sumo Squat",
    "Romanian Squat",
    "Laying Hamstring Curl",
    "Quadracep Extension",
    # Arms
    "Diamond Pushup",
    "Tricep Dips",
    "Archer Pushup",
    "Handstand Pushup",
    "Handstand Shoulder Dip",
    "Spider Curls",
    # Core
    "RDL Plank",
    "V Sit",
    "Leg Raises",
    "Dragon Flag",
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
    print(exercise())
