from quiz_game.levels import *
from quiz_game.data import *

#variable to check if the user wants to reload a quiz he loses
reload_game = True

#TODO - CREER LA FONCTION PLAY_GAME(reload_game, level) QUI ENCAPSULE LES 4 PREMIERES PARTIES DE CHAQUE PARTIE
while reload_game:
    #creating the first level as a Levels object. User must score 7 to pass to next level
    first_level = Levels(level_one, 7)
    #initialize the principle variable : its questions bank
    first_level.initialize()
    #the real processing and ending of the game
    first_level.process()
    #check if user has enough score to go to next level
    if first_level.user_passed(first_level.quiz):
        # LEVEL TWO
        while reload_game:
            second_level = Levels(level_two, 6)
            second_level.initialize()
            second_level.process()
            if second_level.user_passed(second_level.quiz):
                print("LEVEL 3")
                third_level = Levels(level_three, 5)
                third_level.initialize()
                third_level.process()

                if third_level.user_passed(third_level.quiz):
                    while reload_game:
                        print("LEVEL 4")

                    print("GAME OVER")
            else:
                reload_game = second_level.check_reload(second_level.quiz)
        print("GAME OVER")
    #if user can't pass maybe does he want to replay this quiz if no : exit and print : GAME OVER
    else:
        reload_game = first_level.check_reload(first_level.quiz)
print("GAME OVER")
