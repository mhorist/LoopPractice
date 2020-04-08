import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number from 1 - 10: "))

while secret_number != "guess":
    if guess < secret_number:
        print("Too low.")
        guess = int(input("Try again: "))
    elif guess > secret_number:
        print("Too high.")
        guess = int(input("Try again: "))
    else:
        print("You guess it!")
        break
