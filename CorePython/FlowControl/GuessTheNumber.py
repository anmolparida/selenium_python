# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.


import math
import random

number = random.randint(1, 9)
guess = 0
guess_count = 0

while guess != number or guess != 'exit':
    guess = int(input('Guess the Number between 1,9: '))

    if guess == 'exit':
        break
    guess_count = guess_count + 1
    if guess < number:
        print('Guessed Lower than Number')
    elif guess > number:
        print('Guessed Higher than Number')
    else:
        print('** Guessed it Correctly **')
        print('guess_count:', guess_count)
        exit()




