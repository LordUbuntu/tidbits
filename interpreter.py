# This could be improved
# I should rework this into a simplified Python 3 subset parser and
#   interpreter inferface.


def interpret(s):
    return eval(s)


if __name__ == '__main__':
    print(interpret(input()))
