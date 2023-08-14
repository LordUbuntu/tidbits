# Jacobus Burger (2023)
# A program that generates panagrams, maybe could be used to preview fonts without it getting boring?
from random import choice

def basic_panagram():
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
  ]
  return choice(PANAGRAMS)


if __name__ == '__main__':
  print(basic_panagram())
