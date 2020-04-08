# create a guess a number game that requires user input
# add lines to limit the user to 3 guesses

# import the random function to create a random number

# i am stumped on this one. 
'''
If I use secret_number as an int, it won't read it into the guess variable.
If I convert it to a string, which i did below, it still won't read it into the guess variable.
my loop keeps saying 'Sorry that is not the number" even if I type the correct number. ugh!
'''

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


