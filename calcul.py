print("Hello and Welcome")
print("We're going to compute")
print("Give your first number")
#Taking the numbers from the user and convert them into float type
first_number = float(input())
print("give your second number")
second_number = float(input())

#Create functions to add, sub, mult, and div
def sub(a,b):
    c = a-b
    return c

def add(a,b):
    c = a+b
    return c

def mult(a,b):
    c = a*b
    return c

def div(a,b):
    c = a/b
    return c

#create a variable for each compute result, compute the numbers and assign the result to the corresponding variable
add_result = add(first_number,second_number)
substract_result = sub(first_number,second_number)
multiply_result = mult(first_number,second_number)
division_result = div(first_number,second_number)

#Create the total results printer function

def print_results():
    print(f"These are the results \n{first_number} + {second_number} = {add_result}\n{first_number} - {second_number} = {substract_result}\n{first_number} x {second_number} = {multiply_result}\n{first_number} / {second_number} = {division_result}")

print_results()