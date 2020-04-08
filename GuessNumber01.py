# create a guess a number game that requires user input

secret_number = range(1, 10)
guess = input("Guess a number between 1-10: ")
if guess == secret_number:
    print("Nice!  You guessed it!")
elif guess != secret_number:
    print("Sorry that is not the number")