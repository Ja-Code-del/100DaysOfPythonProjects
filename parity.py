#greet
print("Hello\nDo you want to know if a number is pair or ODD?")
#ask for a number
print("Give the number")
#create a variable to handle the rest of division by 2
number_to_test = int(input())
# make the test if the rest of its division by 2 is null or not
if number_to_test % 2 == 0 :
    message = "Your number is pair"
else:
    message = "Your number is odd"
#print the final message
print(message)