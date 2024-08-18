from utils import *

#add a logo
in_service = True
profit = 0
start = True

while start:
    choice_of_user = input("What would you like? (espresso/latte/cappuccino): "
                           "\n******************FOR MAINTENANCE******************"
                           "\nType 'report' ------ to see the resources"
                           "\nType 'Off' ------ to switch the machine off"
                           "\nType 'profit' ----- to see the profit\n").lower()
    if choice_of_user == "report":
        report()
    elif choice_of_user == "off":
        in_service = False
        start = False
    else:
        if choice_of_user in MENU:
            # Check Resources
            ingredients = MENU[choice_of_user]["ingredients"]
            cost_of_coffee = MENU[choice_of_user]["cost"]

            # check if resources are enough to make the coffee
            for coffee_resource, valueCoffee in ingredients.items():
                if ingredients[coffee_resource] > resources[coffee_resource]:
                    # print(f"{coffee_resource} is not sufficient")
                    in_service = False
                else:
                    in_service = True
            #Process coins
            serving_coffee(in_service, choice_of_user)
            profit += cost_of_coffee
            #ask if the user wants another coffee if not set start to False,
            want_another_coffee = input("Do you want another coffee?\nType 'yes' or 'no' ")
            if want_another_coffee == 'yes':
                start = True
                in_service = True
            elif want_another_coffee == 'no':
                start = False
            elif want_another_coffee == 'report':
                report()
            elif want_another_coffee == 'off':
                in_service = False
                start = False
            #or does he want to see the report? call function report and ask il he wants a coffee,
            #think of a while loop

        #if the choice of coffee is not available
        else:
            print("Sorry we don't have this coffee")

print("GOOD BYE")
