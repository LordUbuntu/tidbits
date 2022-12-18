# Jacobus Burger (2022)
# Info:
#   Varous random CLI loading animations done to get an idea of how they make
#   stuff update in place on the command line.
from time import sleep


def percent(speed):
    for i in range(101):
        print(f"{i}%", end='')
        print('\r', end='')
        sleep(1 / speed)


def loading(speed):
    for i in range(101):
        print("Loading" + ('.' * (i % 3)), end='')
        print('\r', end='')
        sleep(1 / speed)


if __name__ == '__main__':
    percent(10)
    loading(10)
