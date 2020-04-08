# create a guess a number game that requires user input
# add lines to limit the user to 3 guesses

# import the random function to create a random number

import random

secret_number = random.randrange(1, 10)
x = (str(secret_number))
guess = input("Guess a number between 1-10: ")
guess_count = 0
guess_limit = 3

print(x)

while guess != x and guess_count < guess_limit:
    if guess == x:
        print("Nice!  You guessed it!")
    elif guess != x:
        print("Sorry that is not the number")
        guess_count += 1
        guess = input("Guess another number: ")
else:
    print("Out of guesses.")
    print("The secret number is: " + x)


