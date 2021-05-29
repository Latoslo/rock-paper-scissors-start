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
game_images = [rock, paper, scissors]
player_choice = int(input('choose 0 for "Rock", 1 for "Paper" and 2 for "Scissors" '))
computer = random.randint(0,2)
if (player_choice >= 3 or player_choice < 0 ):
  print(f"You types an invalid number, You lose! 😀")
else:
  if (player_choice == 0 and computer == 2 ) or (player_choice > computer):
    print(f"You chose: {player_choice} {game_images[player_choice]}")
    print(f"Computer chose: {computer} {game_images[computer]}")
    print(f"You Win! 💪🏻")  
  elif (computer == 0 and player_choice == 2 ) or (computer > player_choice):
    print(f"You chose: {player_choice} {game_images[player_choice]}")
    print(f"Computer chose: {computer} {game_images[computer]}")
    print(f"You lose! 😀")
  else:
    print("It\'s a draw!")  



