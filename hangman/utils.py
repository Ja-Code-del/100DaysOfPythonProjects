import random
import feedbacks
import stages
from hangman.ascii_art import looser_message
from data import *


def list_selector(item):
    themes_name = ["fruits", "music", "animaux"]
    themes = [fruits, musique, animaux]
    themes_dict = dict(zip(themes_name, themes))
    a_list = themes_dict.get(item, [])
    return a_list


def alert_box(something_to_print):
    print(something_to_print)


def play_game(word_list):
    #Randomly choose a word from the word_list and assign it to a variable called chosen_data.
    message = ""
    chosen_data = word_list[random.randint(0, len(word_list) - 1)]
    chosen_word_hint = chosen_data["indice"]
    chosen_word_name = chosen_data["nom"]
    word_length = len(chosen_word_name)

    #for the test
    print(f"C'est un mot de {word_length} lettres")
    print(f"Voici un indice qui pourrait t'aider : {chosen_word_hint}")
    #Create variables called 'lives' & 'score' to keep track of the number of lives left and the score
    #Set 'lives' to equal 6.
    lives = 6
    #Create an empty List called display.
    #For each letter in the chosen_data, add a "_" to 'display'.
    display = []
    #word_to_display is the string,

    for i in range(word_length):
        display.append('_')
        #now every element of display are _ display look like ['_', '_',...., '_']
    #Loop and ask the player to guess the correct letter until he or she finds the correct word; will use while loop
    end_of_game = False
    while not end_of_game:
        # reinitialize word_to_display
        word_to_display = ""
        message = ""
        if lives > 0:
            #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess
            #  lowercase.
            guess = input("Devine une lettre dans ce mot ").lower()
            #if the player has already guessed the word
            if guess in display:
                print(f"Tu as déjà déviné : {guess}")
            #Loop through each position in the chosen_data;
            #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
            for i in range(word_length):
                if guess == chosen_word_name[i]:
                    display[i] = guess
                    message = random.choice(feedbacks.congrats)
                word_to_display = ''.join(display)  # to display it more like a word and not a table
            #check now if the game can end if all the letter of display match with the chosen word
            end_of_game = (word_to_display == chosen_word_name)
            print(word_to_display)
            #Check if guess match not a letter in the word then reduce lives by 1
            if guess not in chosen_word_name:
                message = ""
                lives -= 1
                message = random.choice(feedbacks.encouragements)
        else:
            end_of_game = True
        print(message)
        #print the ASCII art
        print(stages.stages[lives])
    #out of while now
    final_congratulation = random.choice(feedbacks.final_congrats)
    if lives <= 0:
        print(looser_message)
        print(f"Le mot à deviner était: {chosen_word_name}")
    else:
        alert_box(final_congratulation)
        alert_box(f"Ton score est de : {(6 - (6 - lives))*100/6}%")
