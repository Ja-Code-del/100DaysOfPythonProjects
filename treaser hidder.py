line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
my_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
index1 = index2 = 0
test1 = test2 = True
pseudo_code = position[1] + position[0]

if pseudo_code[1] == "A":
    index2 = 0
elif pseudo_code[1] == "B":
    index2 = 1
elif pseudo_code[1] == "C":
    index2 = 2
else:
    print("first coordinate not available")
    test1 = False
if pseudo_code[0] == "1":
    index1 = 0
elif pseudo_code[0] == "2":
    index1 = 1
elif pseudo_code[0] == "3":
    index1 = 2
else:
    print("second coordinate not available")
    test2 = False
if test1 and test2:
    my_map[index1][index2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
