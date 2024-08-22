from quiz_game.levels import *
from quiz_game.data import *

#creating the first level as an Levels object
first_level = Levels(level_one)
#initialize the principle variable : its questions bank
first_level.initialize()
#the real processing and ending of the game
first_level.process()
#check if user has enough score to go to next level
if first_level.user_can_pass(first_level.cerebro):
    # LEVEL TWO
    second_level = Levels(level_two)
    second_level.initialize()
    second_level.process()
    if second_level.user_can_pass(second_level.cerebro):
        print("LEVEL 3")
        third_level = Levels(level_three)
        third_level.initialize()
        third_level.process()

        if third_level.user_can_pass(third_level.cerebro):
            print("LEVEL 4")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")
