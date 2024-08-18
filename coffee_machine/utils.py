from calculator import operators
from data import MENU, resources


def report():
    """Shows off the content of resources"""
    print(f"These are the available resources : ")
    for ingredient, value in resources.items():
        print(f"{ingredient} : {value}")


def fund_calculator(q, d, n, p):
    """Convert the coins in dollar and return the sum"""
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    coins = {"quarters": 0.25, "dime": 0.10, "nickles": 0.05, "pennies": 0.01}
    quarter_in_dollar = operators.mlt(coins["quarters"], q)
    dime_in_dollar = operators.mlt(coins["dime"], d)
    nickels_in_dollar = operators.mlt(coins["nickles"], n)
    pennies_in_dollar = operators.mlt(coins["pennies"], p)
    fund = operators.add(operators.add(operators.add(pennies_in_dollar, nickels_in_dollar), dime_in_dollar),
                         quarter_in_dollar)
    return fund


def serving_coffee(right_condition, coffee):
    """Perform the service of the coffee if there are enough resources"""

    if right_condition:
        print("Please insert coin")
        # Record how much of each coin the machine receive
        quarters_numb = float(input("How many quarters?\n"))
        dime_numb = float(input("How many dime?\n"))
        nickles_numb = float(input("How many nickles?\n"))
        pennies_numb = float(input("How many pennies?\n"))
        # Compute the user fund
        user_fund = fund_calculator(quarters_numb, dime_numb, nickles_numb, pennies_numb)
        print(f"You own ${user_fund}")
        #Check transaction successful
        ingredients = MENU[coffee]["ingredients"]
        cost_of_coffee = MENU[coffee]["cost"]
        # if the user fund is greater than his coffee price so variable user_change is positive
        # the coffee is made and the change is calculated and given
        user_change = operators.sub(user_fund, cost_of_coffee)
        if user_change >= 0:
            print("Hold your coffee")
            print(f"And here is your change : ${user_change}")

            # decrease the volume of the ingredient into the machine
            for key in ingredients:
                resources[key] = resources.get(key) - ingredients.get(key)
            print(f"These are the available resources : ")
            for new_key, new_value in resources.items():
                print(f"{new_key} : {new_value}")
        else:
            print("You don't have enough fund to buy this coffee")
    else:
        print("Resources of the machine are not sufficient")

