import art
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    """ checks guess against answer and returns the turns remaining. """
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You've got it right ! {guess} is the correct answer. ")

def set_difficulty():
    level = input("Choose your difficult level. Type 'easy' or 'hard' : \n")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():
    print(art.logo)
    print("Welcome to the Numbers Game.")
    print("I'm guessing a number between 0 and 100. ")
    answer = random.randint(0, 100)
    print(f"The hint is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} turns remaining.")
        guess = int(input("Please make a guess. \n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you are out of turns. You Loose. ")
            return
        elif guess != answer:
            print("Guess again. ")

game()
