print("hello\n This is a program to check if a year is a leap year or not")
year = int(input("Give a year to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")
