# Jacobus Burger (2023)
# A program that generates panagrams, maybe could be used to preview fonts without it getting boring?
from random import choice


# TODO: find a way to autogenerate these from dictionary files
def basic_panagram():
    """Shows one of a set of fixed panagrams"""
    PANAGRAMS = [
        "Waltz, bad nymph, for quick jigs vex.",
        "Glib jocks quiz nymph to vex dwarf.",
        "Sphinx of black quartz, judge my vow.",
        "How quickly daft jumping zebras vex!",
        "The five boxing wizards jump quickly.",
        "Jackdaws love my big sphinx of quartz.",
        "Pack my box with five dozen liquor jugs.",
        "Amazingly few discotheques provide jukeboxes.",
        "Brawny gods just flocked up to quiz and vex him.",
        "The quick onyx goblin jumps over the lazy dwarf.",
        "Six big devils from Japan quickly forgot how to waltz.",
    ]
    return choice(PANAGRAMS)


if __name__ == '__main__':
  print(basic_panagram())
