# create a guess a number game that requires user input
# add lines to limit the user to 3 guesses

# import the random function to create a random number

# i am stumped on this one. 
'''
If I use secret_number as an int, it won't read it into the guess variable.
If I convert it to a string, which i did below, it still won't read it into the guess variable.
my loop keeps saying 'Sorry that is not the number" even if I type the correct number. ugh!

This is fixed.  I needed to convert the guess variable to an integer correctly.
Example:  guess = int(input("Enter a number between 1 - 10: ")
I was using this Incorrect syntax:  guess = input(int("Enter a number....")
'''

import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1-10: "))
guess_count = 1
guess_limit = 3
print(secret_number)

while guess_count <= guess_limit:
    if guess == secret_number:
        print("Nice!  You guessed it!")
        break
    elif guess != secret_number:
        print("Sorry that is not the number")
        guess = int(input("Guess another number: "))
        guess_count += 1
    else:
        print("Sorry you are out of guesses.")



