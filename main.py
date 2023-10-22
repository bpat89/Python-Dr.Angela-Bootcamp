import art
import random

EASY_LEVEL = 10
HARD_LEVEL = 5
# Function to check user's answer against actual number.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else:
        print(f"You got it! The answer was {answer}.")
# Make function to set the difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    # Choose a Random Number between 1 and 100.
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(0,100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")
    # Repeat the guessing if they get it wrong.
    guess = 0
    while guess != answer:
        # Let the user guess the number.
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)

# Track the number of turns and reduce it by 1 if they chose wrong.
game()

