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


def C(f):
    """Convert from Farenheit to Celcius"""
    return (f - 32) * (5/9)


def kg(lb):
    return lb * 0.45359237
