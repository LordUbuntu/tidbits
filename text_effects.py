# Jacobus Burger (2025-02-28)
# Thought about and imagined a program made to do all sorts of effects
#   on bits of text in a terminal.  I'll take the vapourtext program
#   and others and combine them, add new ones, and more
# This will become a library for TUI. I'll make it's own repo later
from random import randint


def vapourwave(sentence: str) -> str:
    return ' '.join([*sentence])


def randomcaps(sentence: str) -> str:
    return ''.join([char.upper() if randint(0, 1) else char for char in sentence])


def abbreviate(sentence: str) -> str:
    return '.'.join([word[0].upper() for word in sentence.split(" ,-")])
