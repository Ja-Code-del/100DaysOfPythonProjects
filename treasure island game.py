print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._/_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

question_one = ("You are running into a forest and are now at the crossroad, where do you want to go? type 'left' or "
                "'right'")
question_two = "You are now in front of a big lake. Would you like to swim or to wait for a boat. type 'swim' or 'wait'"
question_three = ("Excellent! But now There is no other way but four mysterious gates with different colors. type "
                  "'red' 'blue' 'yellow' or"
                  "'anything else' to choose the door ypu pick")

first_choice = input(question_one)
if first_choice != "left":
    print("you Fall into a hole.\nGame Over.")
else:
    second_choice = input(question_two)
    if second_choice != "wait":
        print("Attacked by trout.\nGame Over")
    else:
        third_choice = input(question_three)
        if third_choice == "yellow":
            print("You Win\nWELCOME TO THE LEVEL TWO")
        elif third_choice == "blue":
            print("Eaten by beasts.\nGame Over")
        elif third_choice == "red":
            print("Burned by fire.\nGame Over")
        else:
            print("Game Over")
