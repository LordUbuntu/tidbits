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
    phase = ["\\", "|", "/", "-"]
    for i in range(101):
        print(phase[i % 4], end='\r')
        sleep(1 / speed)
    print()


def orb(speed):
    phase = ['.', 'o', 'O']
    for i in range(101):
        print(phase[i % 3], end='\r')
        sleep(1 / speed)
    print()


def sweep(speed):
    phase = ["*..", ".*.", "..*", "..."]
    for i in range(0, 101, 3):
        print(phase[i % 4], end='\r')
        sleep(1 / speed)
    print()


if __name__ == '__main__':
    while True:
        choice = int(input(
                """Choose animation:
                    (1) percent
                    (2) loading
                    (3) spin
                    (4) orb
                    (5) sweep
                """
        ))
        speed = int(input("What speed? "))
        if choice == 1:
            percent(speed)
        if choice == 2:
            loading(speed)
        if choice == 3:
            spin(speed)
        if choice == 4:
            orb(speed)
        if choice == 5:
            sweep(speed)