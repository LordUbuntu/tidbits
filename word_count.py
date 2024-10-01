# Jacobus Burger (2024-09-30)
# A program that counts the number of occurences of words in an input.
from collections import Counter

sentence = input("IN: ")
words = [word for word in sentence.split()]
print(Counter(words))
