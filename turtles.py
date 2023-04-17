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
def spiral():
    turtle.home()
    for i in range(100):
        turtle.forward(i)
        turtle.left(15)
