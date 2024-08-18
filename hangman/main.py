from utils import *
from hangman.ascii_art import logo

#print the logo
logo()
play = True
while play is True:
    ##Menu and choice of the theme
    theme = input("Quel thème préfères-tu?\nType fruits, musique, animaux\n")

    #choice of the list of word according to the theme chosen
    chosen_list = list_selector(theme)

    play_game(chosen_list)

    play_again = input("Tu veux jouer encore?\nTape 'oui' ou 'non'")

    if play_again == 'non':
        play = False
    else:
        print("C'est parti pour un autre tour")
