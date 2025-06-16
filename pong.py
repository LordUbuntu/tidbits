#!/bin/python3
# Created by Jacobus Burger (2025-06-14)
# Info:
#   Play the game Pong in terminal!
# See:
#   https://en.wikipedia.org/wiki/Pong
from time import sleep
from sys import argv
from os import system
from random import choice
import curses


def pong():
    scores = [0, 0]
    game = True
    while game:
        # set initial position and direction at start of each round
        x, y = width // 2, height // 2
        dx = choice([-1, 1])
        dy = choice([-1, 1])

        round = True
        while round:
            # score when on left or right walls
            # bounce against floor and ceiling
            if y + dy <= 1 or y + dy >= height - 1:
                dy = dy * -1
            # bounce against paddle
            # move paddle up or down based on player input
            # note: a bounce is dx * -1 or dy * -1


if __name__ == '__main__':
    # get the update interval from the command line
    speed = int(argv[1]) if len(argv) > 1 else 100

    # initialize ncurses
    stdscr = curses.initscr()
    curses.curs_set(False)
    curses.noecho()
    curses.cbreak()
    curses.start_color()

    # set up colors
    blank_color = 1
    blank_char = " "
    ball_color = 2
    ball_char = "*"
    paddle_color_A = 3
    paddle_color_B = 4
    paddle_char = "I"
    curses.init_pair(blank_color, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(ball_color, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(paddle_color_A, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(paddle_color_B, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # initialize game window
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)
    win.timeout(speed)
    win.border()

    # play game
    pong()

    # clean up and end
    curses.curs_set(True)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    system("clear")
