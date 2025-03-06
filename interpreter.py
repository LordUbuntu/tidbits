# This could be improved
# I should rework this into a simplified Python 3 subset parser and
#   interpreter inferface.
# I'll make this a stack machine interpreter to calculate maths in
#   polish (prefix) notation. (remember shunting yard to show as infix)

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


interpreter = StackMachine()

interpreter.PUSH(6)
interpreter.PUSH(7)
interpreter.PUSH(interpreter.ADD)
interpreter.POP()

interpreter.DEBUG()
interpreter.ADD()
interpreter.DEBUG()
