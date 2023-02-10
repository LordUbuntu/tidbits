#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   This is the game "snake" written in python using curses.
#   It is a simple game where the player (a snake) has to
#     eat food (red fruit) to grow in length, while avoiding the
#     running into the walls or eating itself.;w
#   I used [this video](https://www.youtube.com/watch?v=rbasThWVb-c)
#     as a reference for this.
#
from sys import argv
from os import system
from random import randint as rand
import curses


def snake():
    snake_x = width // 4
    snake_y = height // 2

    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2],
    ]

    food = [height // 2, width // 2]
    win.addch(int(food[0]),
              int(food[1]),
              "*",
              curses.color_pair(fruit_color))

    # counter to alternate snake colour between yello and blue
    stripe_color = 0  # 0 is yellow, 1 is blue

    curr_key = curses.KEY_RIGHT
    while True:
        # end if snake bites itself
        if snake[0] in snake[1:]:
            break
        # snake is out of bounds
        if snake[0][0] in [0, height - 1] or snake[0][1] in [0, width - 1]:
            break

        # render food (fruit) and snake
        win.addch(int(food[0]),
                  int(food[1]),
                  fruit_char,
                  curses.color_pair(fruit_color))
        if stripe_color == 0:
            win.addch(int(snake[0][0]),
                      int(snake[0][1]),
                      snake_char,
                      curses.color_pair(stripe_color_Y))
        else:
            win.addch(int(snake[0][0]),
                      int(snake[0][1]),
                      snake_char,
                      curses.color_pair(stripe_color_B))
        stripe_color = (stripe_color + 1) % 2

        # get next key
        next_key = win.getch()
        curr_key = next_key if next_key != -1 else curr_key

        # move snake to next head location
        head = [snake[0][0], snake[0][1]]
        if curr_key == curses.KEY_DOWN:
            head[0] += 1
        elif curr_key == curses.KEY_UP:
            head[0] -= 1
        elif curr_key == curses.KEY_LEFT:
            head[1] -= 1
        elif curr_key == curses.KEY_RIGHT:
            head[1] += 1
        snake.insert(0, head)

        # grow snake if food eaten
        if snake[0] == food:
            food = None
            while food is None:
                new_food = [
                    rand(1, height - 1),
                    rand(1, width - 1)
                ]
                if new_food not in snake \
                        and new_food not in [0, height - 1, width - 1]:
                    food = new_food
        else:
            tail = snake.pop()
            win.addch(int(tail[0]),
                      int(tail[1]),
                      blank_char,
                      curses.color_pair(blank_color))


if __name__ == '__main__':
    # get the update interval from the command line
    update_interval = int(argv[1]) if len(argv) > 1 else 100

    # initialize and setup curses
    stdscr = curses.initscr()
    curses.curs_set(False)
    curses.noecho()
    curses.cbreak()
    curses.start_color()

    # set up colors
    blank_color = 1
    blank_char = " "
    fruit_color = 2
    fruit_char = "*"
    stripe_color_Y = 3
    stripe_color_B = 4
    snake_char = "#"
    curses.init_pair(blank_color, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(fruit_color, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(stripe_color_Y, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(stripe_color_B, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # initialize game window
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)
    win.timeout(update_interval)
    win.border()

    # play game
    snake()

    # clean up and end
    curses.curs_set(True)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    system("clear")
