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
import random
player_name = input('What is your name? Please type it ')
player = int(input('choose 0 for "Rock", 1 for "Paper" and 2 for "Scissors" '))
computer = random.randint(0,2)
if player == 0 or computer == 0:
  print(f"{player_name}:\ncomputer: {rock}")
if player == 1 or computer == 1:
  print(f"{player_name}:\ncomputer:{paper}")
if player == 2 or computer == 2:
  print(f"{player_name}:\ncomputer:{scissors}")
print(player, computer)
if player == computer:
  print("It\'s a draw!'")

