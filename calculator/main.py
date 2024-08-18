from operators import *
import art

#greet
print(art.logo)
print("Welcome")
def calculator():
    #initialyze the continue variable to True
    nextCalcul = True
    #ask for first number
    number_one = float(input("first number"))
    result = 0
    while nextCalcul:
        #ask for operator
        operator = input("operator : ")
        #ask for second
        number_two = float(input("second number"))
        #print the result
        if operator == "+":
            result = add(number_one, number_two)
        elif operator == "x":
            result = mlt(number_one, number_two)
        elif operator == "/":
            result = div(number_one, number_two)
        elif operator == "-":
            result = sub(number_one, number_two)
        else:
            print("operator not taken in charge")
            break
        print(f"{number_one} {operator} {number_two} = {result}")
        continueToCalculate = input(
            f"Do you want to continue the calculus with {result}?, "
            f"type 'y' for yes or 'n' if you want to start a new one").lower()
        if continueToCalculate == 'y':
            number_one = result
        elif continueToCalculate == 'n':
            nextCalcul = False
            calculator()

calculator()