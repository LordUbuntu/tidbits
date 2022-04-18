#! /bin/python3.9
# Created by Jacobus Burger (2022)
# info:
#   Various functions written for my other discrete math course.
#   Thank you to Professor Richard J. Sutcliffe for being such an awesome
#   teacher and inspiration for both my discrete math courses.
#   I had a lot of fun taking that course (though it was hard) and hope to
#   carry this knowledge into my future, and continue to learn and improve
#   because of it. Hopefully I will grow and transform.
#
#   Everything herein was written for fun and practice.
#   I stand on the shoulders of giants, so I claim none of it as my own.
from functools import cache


# factorial function
@cache
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


# binomial equation (combination)
def C(n, k):
    return fact(n) // (fact(k) * fact(n - k))


# permutation equation (permutation)
def P(n, k):
    return fact(n) // fact(n - k)


# maximal flow network backtracking algorithm
def max_flow():
    pass  # TODO
