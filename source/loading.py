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
    print()


def loading(speed):
    for i in range(101):
        print("Loading{}".format('.' * (i % 4)), end='\r', flush=True)
        sleep(1 / speed)
    print()


def spin(speed):
    for i in range(101):
        phase = ["\\", "|", "/", "-"]
        print(phase[i % 4], end='\r')
        sleep(1 / speed)
    print()


def orb(speed):
    for i in range(101):
        phase = ['.', 'o', 'O']
        print(phase[i % 3], end='\r')
        sleep(1 / speed)
    print()


if __name__ == '__main__':
    percent(30)
    loading(30)
    spin(30)
    orb(30)
