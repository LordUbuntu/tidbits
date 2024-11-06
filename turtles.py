# Jacobus Burger (2023)
# Info:
#   A bunch of turtle graphics goofing
from math import sqrt
from random import randint as rand
import turtle


# monte carlo turtle simulation
def simulate(n):
    # box is -100 to 100 on x and y
    square_dots = 0
    circle_dots = 0
    # setup turtle
    turtle.penup()
    turtle.hideturtle()
    turtle.home()
    turtle.speed(0)
    for _ in range(n):
        # set next random position and move turtle to it
        pos = (rand(-100, 100), rand(-100, 100))
        turtle.setpos(pos)
        # if turtle in circle
        if sqrt(pos[0]**2 + pos[1]**2) <= 100:
            turtle.dot(5, "red")
            circle_dots += 1
            square_dots += 1
        else:
            turtle.dot(5, "blue")
            square_dots += 1
    # display approximation of PI
    turtle.setpos((-100, -120))
    turtle.write("approximation: {}".format((circle_dots / square_dots) * 4))
    turtle.exitonclick()


# draw a spiral going out from the inside
def spiral(delta_theta=15):
    turtle.home()
    for i in range(100):
        turtle.forward(i)
        turtle.left(delta_theta)


# draw a circle without using circle
def circle():
    turtle.home()
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)


# creates patterns from cycles of unequal opposing rotation and action
# noticed patterns:
# - multiples of 6 create lines
# - multiples of 4 create triangles
# - others (especially primes) create spikey flowers
# - by 25 the direction of the circles created reverses
# - after 25 the cycle of patterns repeats
def odd(amplitude, fast=False):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.home()
    for i in range(360):
        if i % 2 == 0:
            turtle.forward(10)
            turtle.right(15 * amplitude)
        else:
            turtle.forward(10)
            turtle.left(30 * amplitude)
        turtle.forward(10)
        # TODO: figure out a way to stop the loop early when the shape is drawn!


def knight(steps):
    turtle.hideturtle()
    if steps > 100:
        turtle.speed(0)
    for i in range(steps):
        if rand(0, 1):
            turtle.forward(3)
        else:
            turtle.backward(3)
        if rand(0, 1):
            turtle.right(90)
        else:
            turtle.left(90)


def bishop(steps):
    turtle.hideturtle()
    if steps > 100:
        turtle.speed(0)
    turtle.setheading(45)
    for i in range(steps):
        turtle.right(90 * rand(0, 4))
        turtle.forward(3)


def queen(steps):
    turtle.hideturtle()
    if steps > 100:
        turtle.speed(0)
    turtle.right(rand(0, 8) * 45)
    for i in range(steps):
        turtle.forward(3)


def king(steps):
    turtle.hideturtle()
    if steps > 100:
        turtle.speed(0)
    for i in range(steps):
        turtle.right(rand(0, 8) * 45)
        turtle.forward(3)


def line():
#   This is it, somebody has to draw the line somewhere!!1! >:(
#   Sorry :^) (not sorry).
    turtle.hideturtle()
    turtle.pencolor("red")
    turtle.forward(100)
    turtle.exitonclick()
