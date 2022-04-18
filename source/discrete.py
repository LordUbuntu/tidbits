#! /bin/python3
# Created by Jacobus Burger (2018)
# Info:
#   This is a simple program I wrote during a discrete math class
#   to implement and better understand the Euler method for finding
#   the GCD and LCM of two numbers.


def gcd(A, B):
    a = A
    b = B
    if b > a:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(A, B):
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


def reduce(n, d):
    GCD = gcd(n, d)
    n = n / GCD
    d = d / GCD
    print("n: %i, d: %i, GCD: %i\n" % (n, d, GCD))


if __name__ == "__main__":
    for i in range(0, 100):
        for j in range(0, 100):
            print("gcd of %i and %i is %i" % (i, j, gcd(i, j)))
            print("lcm of %i and %i is %i" % (i, j, lcm(i, j)))
    print("end\n")
