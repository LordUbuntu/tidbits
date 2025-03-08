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
        print(self.stack.pop())

    def PEEK(self):
        print("peek: {}".format(self.stack[-1]))

    def DEBUG(self):
        print(self.stack)


sm = StackMachine()

sm.PUSH(6)
sm.PUSH(7)
sm.PUSH('+')    # need some way to add symbols that can be executed
                #   and modified (metaprogramming)
sm.DEBUG()
while sm.stack:
    if sm.POP() == '+':
        sm.ADD()
    else:
        sm.POP()
sm.DEBUG()
