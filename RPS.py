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

#Write your code below this line 👇
computer_choice = user_choice = "default"
print("You are going to play at Rock, Paper and Scissor with the computer with me :)")
computer_numb = random.randint(0, 2)

#check the computer_numb and assign a choice to each number
if computer_numb == 0:
    computer_choice = rock
elif computer_numb == 1:
    computer_choice = paper
elif computer_numb == 2:
    computer_choice = scissors

user_answer = input(
    "What do you choose to play? I have already made my own choice. Type 'rock', 'paper', or 'scissors'").lower()

if user_answer == "rock":
    user_choice = rock
elif user_answer == "paper":
    user_choice = paper
elif user_answer == "scissors":
    user_choice = scissors
else:
    user_choice = "error"
    print("unavailable choice")

if user_choice == rock:
    if computer_choice == scissors:
        print(scissors, "\nComputer", rock, "\nUser", "\n\nRESULT: YOU W0N")
    elif computer_choice == paper:
        print(paper, "\nComputer", rock, "\nUser", "I WON!\n\nRESULT: GAME OVER")
    elif computer_choice == rock:
        print(rock, "\nComputer", rock, "\nUser", "\n\nRESULT: EQUALITY")
elif user_choice == paper:
    if computer_choice == rock:
        print(rock, "\nComputer", paper, "\nUser", "\n\nRESULT: YOU WIN")
    elif computer_choice == scissors:
        print(scissors, "\nComputer", paper, "\nUser", "I WON!\n\nRESULT: GAME OVER")
    elif computer_choice == paper:
        print(paper, "\nComputer", paper, "\nUser", "\n\nRESULT: EQUALITY")
elif user_choice == scissors:
    if computer_choice == paper:
        print(paper, "\nComputer", scissors, "\nUser", "\n\nRESULT: YOU WIN")
    elif computer_choice == rock:
        print(rock, "\nComputer", scissors, "\nUser", "I WON!\n\nRESULT: GAME OVER")
    elif computer_choice == scissors:
        print(scissors, "\nComputer", scissors, "\nUser", "\n\nRESULT: EQUALITY")
else:
    print("Error : Unavailable choice")
