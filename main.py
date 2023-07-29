import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

icons = [rock, paper, scissors]
player = int(input("choose your weapon: 1 for Rock, 2 for paper, 3 for scissors : \n"))
computer = random.randint(0,3)
player_image = icons[player-1]
computer_image = icons[computer-1]
if player == computer:
    print(f"you chose {player} \n {player_image}")
    print(f"the computer chose {computer}\n {computer_image}")
    print("its a draw")
elif player == 1 and computer == 3:
    print(f"you chose {player}\n {player_image}")
    print(f"the computer chose {computer}\n {computer_image}")
    print("you win")
elif player == 3 and computer == 2:
    print(f"you chose {player}\n {player_image}")
    print(f"the computer chose {computer}\n {computer_image}")
    print("you win")
elif player == 2 and computer == 1:
    print(f"you chose {player}\n {player_image}")
    print(f"the computer chose {computer}\n {computer_image}")
    print("you win")
else:
    print(f"you chose {player}\n {player_image}")
    print(f"the computer chose {computer}\n {computer_image}")
    print("you loose")

