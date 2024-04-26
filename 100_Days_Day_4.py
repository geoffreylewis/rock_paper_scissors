##########################
# Rock, Paper, Scissors! #
##########################

# Importing Module
import random

# Beginning of Game
print("Let's play \"Rock, Paper, Scissors!\"  You ready?\n")

# Hand Images (courtesy of https://replit.com/@appbrewery/rock-paper-scissors-start#main.py)
rock_image = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_image = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_image = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Hand Choices To Play
hand_words = ["rock", "paper", "scissors"]

# Player's Choices
player_choice = str(input("Type \"rock\", \"paper\", or \"scissors\":\n").lower())
print("You play: " + player_choice)
if player_choice == hand_words[0]:
    print(rock_image)
elif player_choice == hand_words[1]:
    print(paper_image)
else:
    print(scissors_image)

# Computer's Choices
computer_choice = random.choice(hand_words)
print("Computer plays: " + computer_choice)
if computer_choice == hand_words[0]:
    print(rock_image)
elif computer_choice == hand_words[1]:
    print(paper_image)
else:
    print(scissors_image)

# End of Game
if player_choice == computer_choice:
    print("You both draw.")
elif player_choice == hand_words[0] and computer_choice == hand_words[1]:
    print("You lose...")
elif player_choice == hand_words[0] and computer_choice == hand_words[2]:
    print("You win!")
elif player_choice == hand_words[1] and computer_choice == hand_words[0]:
    print("You win!")
elif player_choice == hand_words[1] and computer_choice == hand_words[2]:
    print("You lose...")
elif player_choice == hand_words[2] and computer_choice == hand_words[0]:
    print("You lose...")
elif player_choice == hand_words[2] and computer_choice == hand_words[1]:
    print("You win!")