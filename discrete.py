#!/bin/python3
# Created by Jacobus Burger (2018)
# Prologue:
#   This was originally written in 2018/2022 to better understand 
#   and learn discrete math. This was done for fun and practice,
#   and i was inspired by the great influence of my discrete math
#   Professors Richard J Sutcliffe.
#
#   Thank you to Professor Richard J. Sutcliffe for being such an awesome
#   teacher and inspiration in both my discrete math courses.
#   I had a lot of fun taking those courses (though it was hard) and
#   through taking them I developed a better understanding and love
#   for mathematics that I hope to carry into my future. I hope to
#   continue to learn and improve because of it. I will grow and
#   transform.
#
#   I had a great time and formed some good memories. I hope for more.
#
# Info:
#   This is a collection of various math-specific functions and programs
#   written for discrete mathematics to better understand concepts.
#   Everything herein was written for fun and practice.
#
#   I stand on the shoulders of giants, so I claim none of it as my own.
#
import math
import operator as op
from functools import cache
from sys import maxsize as maxsize


# euclidean division (modulo)
# a = bq + r, => r = a - bq
def mod(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return math.nan
    return a - (b * (a // b))


# this shows the steps taken by GCD as it runs
def gcd_reduction(n, d):
    GCD = gcd(n, d)
    n = n / GCD
    d = d / GCD
    print("n: %i, d: %i, GCD: %i\n" % (n, d, GCD))


# this gcd was a procedural example given by professor sutcliffe
def gcd_proc(A, B):
    a = A
    b = B
    if b > a:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# this gcd is a simplified iterative one I learned through more research
def gcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# this gcd is a recursive alternative to the iterative one
@cache
def gcd_rec(a, b):
    if b == 0:
        return a
    return gcd_rec(b, a % b)


# this lcm is a procedural example given by professor sutcliffe
def lcm_proc(A, B):
    big = A if A > B else B
    small = A if A < B else B
    for i in range(1, big + 2):
        for j in range(1, small + 2):
            a = big * i
            b = small * j
            if b == a:
                return b
            elif b > a:
                continue


# this lcm is a direct calculation that depends on the use of gcd
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# iterative power function a**b
def pow_iter(a, b):
    for i in range(b - 1):
        a = a + a
        print(a, i)
    return a


# division
# recursive division
def div_rec(a, b):
    if a - b == 0:
        return 1
    if a - b < 0:
        return 0
    return 1 + div(a - b, b)


# iterative division
def div_iter(a, b):
    count = int(a - b == 0)
    while a - b > 0:
        a, count = a - b, count + 1
    return count


# maximal flow network backtracking algorithm
def max_flow():
    pass  # TODO
