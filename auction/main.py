from art import logo
from algo import get_the_max_of

#logo
print(logo)

#greetings and presentation
print("WELCOME TO THIS ONLINE AUCTION\nMAY THE WINNER WIN!!")


#this a function which create a dictionary
def register(username, user_bid):
    user_info = {
        "name": username,
        "bid": user_bid
    }
    return user_info

#creating an empty list of user
user_list = []
registration_is_over = False
# Ask the name of the player, ask his bid and ask for another person information
while not registration_is_over:
    name = input("What's your name?")
    bid = int(input("What's your bid?"))
    add_other = input("Is there other player? Type 'yes' or 'no'").lower()
    if add_other == 'yes':

        registration_is_over = False
    else:
        registration_is_over = True
    # Use a function to create a dictionary that contain the users informations and put them into a List of dictionary.
    user_list.append(register(name, bid))
# Clear the screen after each registration
#print(user_list)

user_bid_list = []
for item in user_list:
    user_bid_list.append(item["bid"])
#print("these are the bids : ", user_bid_list)
higher_bid = get_the_max_of(user_bid_list)
#print(f"This is the higher bid : {higher_bid}")

for item in user_list:
    if item["bid"] == higher_bid:
        print(f'The winner of this auction is : {item["name"]}')
