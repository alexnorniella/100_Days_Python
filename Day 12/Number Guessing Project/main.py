import random
from art2 import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

lives = 0
number = random.randrange(1, 101)


# Normalize the input
level_difficulty = input("Type 'easy' or 'hard':").strip().lower()

if level_difficulty == 'easy':
    lives = 10
elif level_difficulty == 'hard':
    lives = 5
else:
    print("Invalid input. Please type 'easy' or 'hard'.")

print(f"You have {lives} attempts remaining to guess the number.")


def guess():
    """Prompts the user to make a guess and returns it as an integer."""
    return int(input("Make a guess: "))


def number_too_low_or_high(user_guess):
    """Checks if the guess is too high, too low, or correct."""
    if user_guess > number:
        print("Too High")
    elif user_guess < number:
        print("Too Low")
    else:
        print("Correct!")


# Main game loop
while lives > 0:
    user_guess = guess()

    if user_guess == number:
        print("You guessed it! Well done!")
        break
    else:
        number_too_low_or_high(user_guess)
        lives -= 1
        if lives > 0:
            print(f"You have {lives} attempts remaining.")
        else:
            print("You've run out of lives! Game over.")
            print(f"The correct number was {number}.")
