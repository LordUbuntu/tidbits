# Jacobus Burger (2023)
# Just for fun, based on a video from Engineer Man
import os
import random
import time

DENSITY = 5
DELAY = 0.3

flakes = ['λ', '•', '.', '❆', '❅', '❄', '*']

# get terminal width
# for ever
    # create a string `s` that is `width` wide with `DENSITY` random `flakes` in it.
    # concatenate that to the current string
    # print it
# This will cause the flakes to "fall" using terminal wrapping. Building the display by row.
