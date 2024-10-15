# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("new_file2.txt", mode="a") as file:
    file.write("New text")
    file.write("second line")
