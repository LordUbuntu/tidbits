#!/bin/python3
# Created by Jacobus Burger (2025-06-14)
# Info:
#   Play the game Pong in terminal!
# See:
#   https://en.wikipedia.org/wiki/Pong
# TODO: add music and sfx to make it nicer
# probably move this to its own repository at some point...
from time import sleep
from sys import argv
from os import system
from random import choice
import curses


# TODO:
# - add variable for paddle height
# - interestingly, logic lets paddles move on x too. So maybe as a bonus feature add that mode (konami code activation?)


def pong():
    # [player, opponent]
    scores = [0, 0]
    game = True
    while game:
        # set initial position and direction at start of each round
        x, y = width // 2, height // 2
        dx = choice([-1, 1])
        dy = choice([-1, 1])

        # y, x
        player_paddle = [height // 2, 2]
        opponent_paddle = [height // 2, width - 2]

        # each round
        while True:
            # get input
            key = win.getch()
            # quit on q key
            if key == ord('q'):
                game = False
                break
            # move paddle up or down based on input
            #   move player paddle up
            if key == ord('w'):
                player_paddle[0] -= 1
            #   move player paddle down
            if key == ord('s'):
                player_paddle[0] += 1
            #   move opponent paddle up
            if key == ord('i'):
                opponent_paddle[0] -= 1
            #   move opponent paddle down
            if key == ord('k'):
                opponent_paddle[0] += 1

            # update pong
            #   update ball position
            y = y + dy
            x = x + dx
            # bounce ball against floor and ceiling
            if y + dy <= 1 or y + dy >= height - 1:
                dy = dy * -1
            # bounce against paddles
            #   bounce from player paddle
            if x == player_paddle[1] and y in [*range(player_paddle[0] - 1, player_paddle[0] + 2)]:
                dx = dx * -1
            #   bounce from opponent paddle
            if x == opponent_paddle[1] and y in [*range(opponent_paddle[0] - 1, opponent_paddle[0] + 2)]:
                dx = dx * -1
            # update scores and start next round when hitting walls
            #   if on left wall (player, score to opponent)
            if x <= 1:
                scores[1] += 1
                break
            #   if on right wall (opponent, score to player)
            if x >= width - 1:
                scores[0] += 1
                break

            # render
            #   clear and draw window
            win.clear()
            win.border()
            #   write scores
            win.addstr(int(height // 2), int(width // 8), "player: {}".format(scores[0]), curses.color_pair(player_color))
            win.addstr(int(height // 2), int(width // 4 * 3), "opponent: {}".format(scores[1]), curses.color_pair(opponent_color))
            #   draw ball
            win.addch(int(y), int(x), ord(ball_char), curses.color_pair(ball_color))
            #   draw paddles
            for player_y in range(player_paddle[0] - 1, player_paddle[0] + 2):
                win.addch(int(player_y), int(player_paddle[1]), ord(paddle_char), curses.color_pair(player_color))
            for opponent_y in range(opponent_paddle[0] - 1, opponent_paddle[0] + 2):
                win.addch(int(opponent_y), int(opponent_paddle[1]), ord(paddle_char), curses.color_pair(opponent_color))
            #   show visuals
            win.refresh()


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
    player_color = 3
    opponent_color = 4
    paddle_char = "I"
    curses.init_pair(blank_color, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(ball_color, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(player_color, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(opponent_color, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # initialize game window
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)
    win.timeout(speed)

    # play game
    pong()

    # clean up and end
    curses.curs_set(True)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    system("clear")
