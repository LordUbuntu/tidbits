#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   I wanted to build a program that converts between metric and imperial
#     measures of weight.
#   It's not very smart, and there's definitely room for improvement, but it
#     is a learning experience and a chance to do something, not matter how
#     small it is.
#   Inspired by google's magic search engine converters
import re
from sys import argv


def fahrenheit_to_celsius(f, c):
    return (f - 32) * (5/9)



def convert(from_unit, to_unit: str, value: float) -> float:
    """
    converts a given measure of one unit to another using ratios between units.
    from_unit, to_unit: str
    value: float
    returns: converted float
    """
    # there are ratios between units so we just need to match pairs
    ratios = [
        ("st", "gt", 6.35029318e-12),
        ("st", "mt", 6.35029318e-9),
        ("st", "t", 0.00635029),
        ("st", "kg", 6.35029),
        ("st", "g", 6350.29),
        ("st", "mg", 6.35e6),
        ("st", "ug", 6.35e9),
        ("lb", "gt", 4.5359237e-13),
        ("lb", "mt", 4.5359237e-10),
        ("lb", "t", 0.000453592),
        ("lb", "kg", 0.453592),
        ("lb", "g", 453.592),
        ("lb", "mg", 453592),
        ("lb", "ug", 4.536e8),
        ("oz", "gt", 2.8349523125e-14),
        ("oz", "mt", 2.8349523125e-11),
        ("oz", "t", 2.835e-5),
        ("oz", "kg", 0.0283495),
        ("oz", "g", 28.3495),
        ("oz", "mg", 28349.5),
        ("oz", "ug", 2.835e7),
    ]
    if not any(from_unit in ratio for ratio in ratios):
        quit(f"starting unit '{from_unit}' not recognized")
    if not any(to_unit in ratio for ratio in ratios):
        quit(f"destination unit '{to_unit}' not recognized")
    ratio = list(
        filter(lambda unit: (from_unit in unit) and (to_unit in unit), ratios)
    )[0]
    # calculation depends on which unit we start from
    if ratio[0] == from_unit:
        return value * ratio[2]
    if ratio[0] == to_unit:
        return value / ratio[2]


def main():
    if len(argv) < 3:
        quit("Usage: convert [from] [to]\nExample: convert 10lb kg")
    value, from_unit = [
        string for string in re.split(r"(\d+)", argv[1]) if string != ""
    ]
    to_unit = argv[2]
    result = convert(from_unit, to_unit, float(value))
    result = str(result) + to_unit
    print(result)


if __name__ == "__main__":
    main()
