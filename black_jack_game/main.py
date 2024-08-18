import random
#import emoji
from art import logo
from os import system, name
from time import sleep
#from colorama import Fore, Back


#FUNCTIONS
def clear():
    _ = system('cls')


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card(deck):
    """Pick one element of deck of cards and return it"""
    return random.choice(deck)


def calculate_scores(deck):
    """Calculate the score of players. Taking as arguments the cards value"""
    score = sum(deck)
    if deck == [11, 10] or deck == [10, 11]:
        print("Black Jack")
        return 0
    else:
        if 11 in deck and score > 21:
            deck.remove(11)
            deck.append(1)
            score = sum(deck)
    return score


def compare(user, computer):
    """To compare the value of scores and print something"""
    # If the computer and user both have the same score, then it's a draw.
    if calculate_scores(user) == calculate_scores(computer):
        print("DRAW")
        print("------------------------------------------------------------------------")
    # If the computer has a blackjack (0), then the user loses.
    elif calculate_scores(computer) == 0:
        print("YOU LOSE")
        print("------------------------------------------------------------------------")
    # If the user has a blackjack (0), then the user wins.
    elif calculate_scores(user) == 0:
        print("YOU WIN :smile: ")
        print("------------------------------------------------------------------------")
    # If the user_score is over 21, then the user loses.
    elif calculate_scores(user) > 21:
        print("YOU LOSE :thumbs_down: ")
        print("------------------------------------------------------------------------")
    # If the computer_score is over 21, then the computer loses.
    elif calculate_scores(computer) > 21:
        print("YOU WIN :smile: ")
        print("------------------------------------------------------------------------")
    # If none of the above, then the player with the highest score wins.
    else:
        if calculate_scores(user) > calculate_scores(computer):
            print("YOU WIN :smile: ")
            print("------------------------------------------------------------------------")
        else:
            print("DEALER WINS")
            print("------------------------------------------------------------------------")


def cards_and_score(user, computer):
    """print the cards and the score of each hand passed into argument"""
    print("------------------------------------------------------------------------")
    print(f"Your cards : {user}")
    print(f"Your score is : {calculate_scores(user)}")

    print(f"Computer's card : {computer}")
    print(f"Computer score is : {calculate_scores(computer)}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

end_game = False
while not end_game:
    user_cards = []
    computer_cards = []
    end_of_session = False
    #print logo with color
    #print(Back.LIGHTMAGENTA_EX + Fore.BLACK + logo)
    choice_to_play = input("Do you want to play to Black Jack with me? \nType 'y' for yes or 'n' for no\n").lower()
    if choice_to_play == 'y':
        for i in range(2):
            user_cards.append(deal_card(cards))
            computer_cards.append(deal_card(cards))

        computer_turn = False
        while (calculate_scores(user_cards) < 21 and calculate_scores(computer_cards) < 21) and not computer_turn:
            if (calculate_scores(user_cards) == 0 or calculate_scores(user_cards) > 21 or calculate_scores(
                    computer_cards) == 0 or
                    calculate_scores(computer_cards) > 21):
                end_of_session = True
            #show to user the cards
            else:
                cards_and_score(user_cards, computer_cards)
                # Hint 10: If the game has not ended, ask the user if they want to draw another card.
                user_choice = input("Do you want to draw another card? Type 'y' for yes or 'n' for no\n").lower()
                # If yes,deal_card() function to add another card to the user_cards List.
                # If no, then the game has ended.
                # Hint 11: The score will need to be rechecked with every
                # new card drawn and the checks in Hint 9 need to be repeated until the game ends.
                if user_choice == 'y':
                    user_cards.append(deal_card(cards))
                else:
                    computer_turn = True

        end_of_session = True
        if computer_turn:
            # Hint 12: Once the user is done, it's time to let the computer play.
            # The computer should keep drawing cards as long as it has a score less than 17.
            while calculate_scores(computer_cards) < 17:
                computer_cards.append(deal_card(cards))

            end_of_session = True
        if end_of_session:
            cards_and_score(user_cards, computer_cards)
            compare(user_cards, computer_cards)

    else:
        print("Ok fine")

        # Hint 14: Ask the user if they want to restart the game.
    choice_to_restart = input("Do you want to restart the game? Type 'y' for yes and 'n' for no\n").lower()
    if choice_to_restart == 'y':
        clear()
        print(logo)
    else:
        end_game = True

print("GoodBye")
