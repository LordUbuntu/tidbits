#!/bin/python3
# Created by Jacobus Burger (2021)
#
# Info:
#   This is a program written in python that I created to calculate the
#   frequency of different ASCII symbols commonly found in programming
#   languages. I did this so that I could create a keyboard layout layer
#   that keeps the most used symbols near the strongest fingers to improve
#   typing experience and reduce RSI.
#
# Usage:
#   To run this program you need to create a file called `files.txt` that
#   contains the relative path from this file of every source file you want
#   to have it parse. After that, to run the program you type
#   `./language_symbol_occurences.py | sort --numeric-sort --reverse > output_file`.
#   Once it has completed (it can take a while on very large batches) it will
#   produce an output file containing the summary of each symbol and it's
#   cumulative frequency in the heap.
from collections import Counter

programming_symbols = [
    '+', '-', '=', '_',
    '!', '`', '~', '@',
    '#', '$', '%', '*',
    '|', '<', '(', '[',
    '{', '}', ']', ')',
    '>', ';', ':', "'",
    '"', '?', '/', '\\',
    ',', '.', '^', '&'
]
total_symbols = 0
occurences = Counter([])

# list files to parse though
files = [file.strip("\n") for file in open("files.txt", "r").readlines()]

# count occurences in each file
for file in files:
    try:
        with open(file, "r") as f:
            symbols = [
                char
                for line in f.readlines()
                for char in line
                if char in programming_symbols
            ]
            total_symbols += len(symbols)
            occurences += Counter(symbols)
    except UnicodeDecodeError:
        continue
    except FileNotFoundError:
        continue

# output results
for symbol, occurence in occurences.items():
    print("%i => %s (%03f%%)" % (
            occurence,
            symbol,
            (occurence / total_symbols) * 100
        )
    )
