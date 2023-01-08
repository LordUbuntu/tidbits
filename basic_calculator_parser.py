#!/usr/bin/env python3
# Created by Jacobus Burger (2018)
#
# Info:
#   This program parses and calculates a given string representing a
#   mathematical equation. This is done by using the shunting yard
#   algorithm by Edsgar Djikstra (who I owe my eternal thanks to)
#   to convert an infix string representation into a postfix list
#   (done with the lex function).
#   With the resulting list, the program then calculates the result
#   by pushing each symbol in the list onto a temporary stack, calculating
#   and re-pushing the result if two literals and an operand are on the stack.
#   To try and make it interactive, the program includes a problem
#   generator, a problem-solution checker, and a main loop that times and
#   records the correctness of each solution given by the player.
#   Since this was the very first parser-calculator I wrote (mind you
#   with minimal knowledge or outside help) it's rather janky and limited.
import time
from random import randint as randint
from math import sqrt as sqrt
from collections import deque as deque


def lex(string):
    """
    Takes an infix string as input and outputs a postfix list for
        given mathematical expressions (currently limited to arithmetic
        operators).
        Thanks to Edsgar Djikstra for inventing the shunting yard
        algorithm which I used in this funciton.
    Note that this function is limited to binary operators (*, /, +, -)
      and as a result cannot handle:
        - negative numbers
        - variables
        - brackets
        - exponents
        - non-binary operators
        - functions
    """
    op_priority = {"/": 2, "*": 2, "+": 1, "-": 1}
    op_stack = deque()
    output = deque()

    # iterate over each token in the string
    for token in string.split(" "):
        # if it is a number add it to the output
        if token.isdigit():
            output.append(int(token))

        # if it is an operator, push it to the stack
        elif token in op_priority.keys():
            # forall ops >= new op, pop it from the stack & add to output
            for op in op_stack.copy():
                if op_priority.get(op) >= op_priority.get(token):
                    output.append(op_stack.pop())
                else:
                    break
            # push new op to stack
            op_stack.append(token)
        else:
            # raise an error for illegal operators or literals
            raise SyntaxError("'{0}'".format(token)) from None
    # add remaining ops to output
    while len(op_stack) > 0:
        output.append(op_stack.pop())

    return output


def calculate(problem):
    """
    This algorithm calculates the result of lex by using a stack.
    """
    stack = deque()

    # for each token
    for token in problem:
        # if the token is a literal, then push it onto the stack
        if type(token) in [int, float]:
            stack.append(token)
        # if it is an op, then pop the previous two tokens
        elif token in ["/", "*", "+", "-"]:
            val1 = stack.pop()
            val2 = stack.pop()
            # if those tokens are both literals, then calculate & push to stack
            if type(val1) in [int, float] and type(val2) in [int, float]:
                if token == "/":
                    stack.append(val2 / val1)
                elif token == "*":
                    stack.append(val2 * val1)
                elif token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
            # otherwise push all back to stack and continue
            else:
                stack.append(val2)
                stack.append(val1)
                stack.append(token)
    # if the stack has only 1 token left
    if len(stack) == 1:
        # return the final value as a scalar
        return stack.pop()
    else:
        raise RuntimeError("Stack has more than one solution: ", stack)


def problem_generator(difficulty=3):
    """
    This function generates mathematical expressions as string. It is not very
      smart and will generate expressions that have answers the lex function
      cannot accept.
    """
    operators = ["/", "*", "+", "-"]
    numeric_lim = difficulty * 7
    output = ""
    for i in range(difficulty + 3):
        if i % 2 == 0:
            output += str(randint(1, numeric_lim)) + " "
        else:
            output += operators[randint(0, len(operators) - 1)] + " "
    if output[len(output) - 2] in operators:
        output += str(randint(1, numeric_lim))
    return output


def check(problem, user_solution):
    # This function simply checks if the user given solution is correct.
    soln1 = calculate(lex(problem))
    soln2 = calculate(lex(user_solution))
    return soln1 == soln2


def main():
    record = {}
    while True:
        # start problem
        problem = problem_generator()
        time0 = time.time()
        user_solution = input(problem + " = ")

        # quit if user gives Q
        if user_solution == "Q":
            break

        # end problem
        time1 = time.time()
        truth = check(problem, user_solution)

        # record solutions
        record.update({problem: (time0 - time1, user_solution, truth)})
    print(record)


if __name__ == "__main__":
    main()
