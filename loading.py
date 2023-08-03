# Jacobus Burger (2022)
# Info:
#   Varous random CLI loading animations done to get an idea of how they make
#   stuff update in place on the command line.
from time import sleep
from os import get_terminal_size as term_size
from string import ascii_letters
from random import choices


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


def bar(speed):
    for i in range(0, 101):
        if i < term_size()[0]:
            print(('=' * i) + '>', end='\r')
        sleep(1 / speed)
    print()


def bounce(speed):
    phase = [".", "o"]
    for i in range(0, 101):
        print(phase[i % 2], end='\r')
        sleep(1 / speed)
    print()


def glitch(speed):
    for i in range(0, 101):
        print(''.join(choices(ascii_letters, k=term_size()[0]//4)), end='\r')
        sleep(1 / speed)
    print()


def scroll(speed):
    for i in range(0, 101):
        print(('_' * (i % 3)) + ' '.join('='*(term_size()[0]//4)), end='\r')
        sleep(1 / speed)
    print()


def rotate(speed):
    message = "Loading...          "
    for i in range(0, 101):
        print(message, end='\r') 
        sleep(1 / speed)
        # rotate text by 1
        message = message[-1] + message[:-1]
    print()


def fira(speed):
    message = '\uee00' + ('\uee01' * 8) + '\uee02' + ' '
    message = list(message)
    offset = 0
    for i in range(0, 101):
        if i % 10 == 0:
            message[offset] = chr(ord(message[offset]) + 3)
            offset += 1
        print(''.join(message), end='\r')
        sleep(1 / speed)
    print()


if __name__ == '__main__':
    while True:
        choice = int(input(
                """Choose animation:
                    (1)  percent
                    (2)  loading
                    (3)  spin
                    (4)  orb
                    (5)  sweep
                    (6)  progress bar
                    (7)  bounce
                    (8)  glitch
                    (9)  scroll
                    (10) rotate
                    (11) fira code progress bar (need font)
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
        if choice == 6:
            bar(speed)
        if choice == 7:
            bounce(speed)
        if choice == 8:
            glitch(speed)
        if choice == 9:
            scroll(speed)
        if choice == 10:
            rotate(speed)
        if choice == 11:
            fira(speed)
