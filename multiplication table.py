#greet
print("Hello\nDo you want to know the multiplication table of a number?")
#ask for a number
#create a variable to handle the given number
numb = int(input("Just give the number "))
terms = int(input("How many terms?\n"))
for i in range(terms):
    print(f"{numb} x {i} = {numb * i}")
