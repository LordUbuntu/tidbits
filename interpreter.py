# This could be improved
# I should rework this into a simplified Python 3 subset parser and
#   interpreter inferface.
# I'll make this a stack machine interpreter to calculate maths in
#   polish (prefix) notation. (remember shunting yard to show as infix)
# This should be built upon and given it's own repo. I will make a very
#   simple stack based programming language as a subset of some Python
#   with a couple of neat features. Name to be decided. Serpet? Egg?
#   something to indicate the snakishness and a beginning.
# I'll share this project once I've gotten it to a stable basic state
# This initial version is made based on "500 Lines or Less: A Python
#   Interpreter in Python"
#   https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html
# I think among egg, drake, serpent, and snek that I'll settle of snek
#   as the name and .snk as the file extension because the name evokes
#   tinyness/cuteness and simplicity which is the ethos of this language

class StackMachine:
    def __init__(self):
        self.stack = []

    def ADD(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a + b)

    def PUSH(self, value):
        self.stack.append(value)

    def POP(self):
        if self.stack:
            return self.stack.pop()
        return None

    def PEEK(self):
        print("peek: {}".format(self.stack[-1]))

    def DEBUG(self):
        print(self.stack)

    # NOTE:
    # - minimal basic instruction set
    # - easy metaprogramming to build upon and modify instructions
    # - written very simply
    # TODO:
    # - write a list of (mutable) instructions
    # - write a parser for the basic starting instructions
    # - write a runner

    def parse(self):
        pass

    def run(self, instructions):
        pass





# potential instruction set
# + - * / // %
sm = StackMachine()
sm.PUSH(6)
sm.PUSH(7)
sm.PUSH('+')
while sm.stack:
    sm.DEBUG()
    input()
    symbol = sm.POP()
    if symbol == '+':
        sm.ADD()
    else:
        print(symbol)
sm.DEBUG()
