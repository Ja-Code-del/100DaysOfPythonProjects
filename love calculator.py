print("The Love Calculator is calculating your score...")
name1 = input("What is the man name?")
name2 = input("What is the girl name?")

name1 = name1.lower()
name2 = name2.lower()

# concatenate the names
couple_name = name1 + name2

#counting each letter in the combined name
T_occ = couple_name.count("t")
R_occ = couple_name.count("r")
U_occ = couple_name.count("u")
E_occ = couple_name.count("e")

first_total = T_occ + R_occ + U_occ + E_occ

L_occ = couple_name.count("l")
O_occ = couple_name.count("o")
V_occ = couple_name.count("v")
E_occ = couple_name.count("e")

second_total = L_occ + O_occ + V_occ + E_occ

#combining the numbers to make a two-digit number
love_score = int(str(first_total) + str(second_total))

#checking the love score and displaying the proper message
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
