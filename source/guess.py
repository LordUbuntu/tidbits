from random import randint as rand


if __name__ == '__main__':
    number = rand(1, 100)
    while True:
        guess = int(input("Guess a number: "))
        if guess == number:
            print("You did it!")
            break
        if guess < number:
            print("Higher...")
        if guess > number:
            print("Lower...")
