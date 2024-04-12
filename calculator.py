def calculate(s):
    # todo: safety checks so this isn't just an interpreter
    return eval(s)


if __name__ == '__main__':
    print(calculate(input()))
