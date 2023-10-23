import art
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to check user's answer against actual number.
def check_answer(guess, answer,attempts):
    """ Checks the guess against answer and returns the number of attempts remaining. """
    if guess > answer:
        print("Too High")
        return attempts -1
    elif guess < answer:
        print("Too Low")
        return attempts - 1
    else:
        print(f"You got it right, the correct answer is {answer} ")


# Make function to set the difficulty.
def set_difficulty():
    level = input("choose the level as easy or hard. ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    # Choose a Random Number between 1 and 100.
    print(art.logo)
    print("Welcome to the Mind Reader Numbers")
    print("Im thinking of a number between 0 and 100 .")
    answer = random.randint(0, 100)
    print(f"Psst,  here's the hint {answer}")

    # Let the user guess the number.
    attempts = set_difficulty()
    # Repeat the guessing if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"your remaining attempts are {attempts}")
        guess = int(input("Make a Guess. : "))
        attempts = check_answer(guess, answer, attempts)


    # Track the number of turns and reduce it by 1 if they chose wrong.
game()