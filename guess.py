from random import randint as rand


if __name__ == '__main__':
    low, high = rand(1, 100), rand(2, 200)
    number = rand(low, high)
    while True:
        guess = int(input("Guess a number between {} and {}: ".format(low, high)))
        if guess == number:
            print("You did it!")
            break
        if guess < number:
            print("Higher...")
        if guess > number:
            print("Lower...")
