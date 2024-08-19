from Coffee_machineOOPversion.menu import Menu
from Coffee_machineOOPversion.coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from errorHandler import *

barista = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()
running = True
user_choice = ""
check_error = True

print("Hello welcome on my super coffee machine\n")

while running:

    while check_error:
        try:
            user_choice = choose_right_option()
            print(f"Your choice is {user_choice}")
            break
        except NonValidEntry as e:
            print(e)
            print("Please try again.\n")

    if user_choice == 'report':
        print("AVAILABLE RESOURCES ARE :\n")
        barista.report()

    elif user_choice in my_menu.get_items():
        #create a MenuItem called coffee_choice with the function find_drink
        coffee_choice = my_menu.find_drink(user_choice)
        # Check resources
        if barista.is_resource_sufficient(coffee_choice):
            print("I Can make it for you 😊")
        else:
            break

            # Process coins
            #Check transaction successful
        if money_machine.make_payment(coffee_choice.cost):
            #Serve coffee and ask if user wants another one
            barista.make_coffee(coffee_choice)
            run_again = input("\nDo you want another thing?\nType 'yes' or 'no' to exit").lower()
            if run_again == 'no':
                running = False
    elif user_choice == 'off':
        running = False
        break
